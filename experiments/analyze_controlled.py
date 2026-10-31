"""Descriptive and matched analysis; no expert annotations or intrusion-rate claims."""
from pathlib import Path
from collections import defaultdict,Counter
import argparse,csv,json,re,math,hashlib

def exact_p(a,b):
    n=a+b
    return min(1.,2*sum(math.comb(n,k) for k in range(min(a,b)+1))/2**n) if n else 1.

def main(run_dir):
    design=json.loads((run_dir/'design.json').read_text())
    cells={x['record_id']:x for x in map(json.loads,(run_dir/'schedule.jsonl').read_text().splitlines())}
    raw=[json.loads(x) for x in (run_dir/'predictions.jsonl').read_text().splitlines()]
    assert len(raw)==len({x['record_id'] for x in raw})
    answers=[];indexed={}
    for r in raw:
        c=cells[r['record_id']];p=r.get('parsed',{});p=p if isinstance(p,dict) else {}
        facts=p.get('complaint_facts',[]);facts=facts if isinstance(facts,list) and all(isinstance(x,str) for x in facts) else []
        explanation=p.get('explanation','');explanation=explanation if isinstance(explanation,str) else ''
        valid=r['status']=='ok';marker=bool(re.search(r'\b(?:47|2019)\b',' '.join(facts)))
        row={'record_id':r['record_id'],'scenario_id':c['scenario_id'],'script':c['script'],'context_condition':c['context_condition'],'policy':c['policy'],'gold_primary':c['gold_primary'],'status':r['status'],'prediction':p.get('category',''),'primary_correct':valid and p.get('category')==c['gold_primary'],'nonempty_fact_array':valid and bool(facts),'complaint_facts':json.dumps(facts,ensure_ascii=False),'explanation':explanation,'literal_marker_echo':marker,'done_reason':r.get('response',{}).get('done_reason',''),'elapsed_seconds':r['elapsed_seconds']}
        answers.append(row);indexed[c['scenario_id'],c['script'],c['context_condition'],c['policy']]=row
    if answers:
        with (run_dir/'answers.csv').open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(answers[0]),lineterminator='\n');w.writeheader();w.writerows(answers)
    groups=defaultdict(list)
    for row in answers:groups[row['script'],row['context_condition'],row['policy']].append(row)
    summary=[]
    for (script,condition,policy),g in sorted(groups.items()):
        valid=[x for x in g if x['status']=='ok']
        summary.append({'script':script,'context_condition':condition,'policy':policy,'attempts':len(g),'valid_outputs':len(valid),'invalid_outputs':len(g)-len(valid),'nonempty_fact_arrays':sum(x['nonempty_fact_array'] for x in g),'primary_correct_all_attempts':sum(x['primary_correct'] for x in g),'marker_echo_valid_outputs':sum(x['literal_marker_echo'] for x in valid),'marker_echo_valid_denominator':len(valid),'expert_intrusion_count':None})
    pairs=[]
    scenarios=design['scenario_ids']
    # These accuracy policy contrasts are secondary descriptive comparisons.
    # Marker comparisons retain only valid paired structured outputs; coverage is explicit.
    for script in ['english','romanized','kannada']:
        for context in ['none','relevant','relevant_source_details','irrelevant_source_details']:
            both=[(indexed.get((i,script,context,'baseline')),indexed.get((i,script,context,'fidelity_guard'))) for i in scenarios]
            if not all(a is not None and b is not None for a,b in both):continue
            for metric in ['primary_correct','literal_marker_echo']:
                if metric=='literal_marker_echo' and 'source_details' not in context:continue
                eligible=both if metric=='primary_correct' else [(a,b) for a,b in both if a['status']=='ok' and b['status']=='ok']
                up=sum(not a[metric] and b[metric] for a,b in eligible);down=sum(a[metric] and not b[metric] for a,b in eligible)
                pairs.append({'script':script,'context_condition':context,'metric':metric,'paired_cases':len(eligible),'baseline_only':down,'guard_only':up,'guard_minus_baseline_pp':100*(up-down)/len(eligible) if eligible else None,'p_exact':exact_p(up,down) if eligible else None,'p_holm_within_metric':None})
    for metric in ['primary_correct','literal_marker_echo']:
        family=sorted([p for p in pairs if p['metric']==metric and p['p_exact'] is not None],key=lambda x:x['p_exact']);running=0
        for i,p in enumerate(family):
            running=max(running,min(1.,(len(family)-i)*p['p_exact']));p['p_holm_within_metric']=running
    complete=len(raw)==len(cells)
    hashes={name:hashlib.sha256((run_dir/name).read_bytes()).hexdigest() for name in ['schedule.jsonl','predictions.jsonl','design.json','model_metadata.json']}
    result={'status':'completed' if complete else 'partial','planned_calls':len(cells),'attempted_calls':len(raw),'valid_calls':sum(x['status']=='ok' for x in raw),'invalid_or_error_calls':sum(x['status']!='ok' for x in raw),'expert_annotation_status':'not performed; user requested experiments only','summary':summary,'secondary_exploratory_pairs':pairs,'hashes':hashes,'analysis_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'interpretation_limits':design['limits']+['Marker comparisons condition on valid paired outputs and can be selection-biased.','Exact literal screening misses spelled-out equivalents, paraphrase and untranslated numeric representations.','Markers in complaint_facts can be negated or quoted; the signal does not establish attribution or hallucination.','Post-generation analysis; no confirmatory preregistration or validated causal fidelity measurement.','Exact paired tests assume independent scenario units; shared authoring templates can violate this assumption, and the 16 cases are not population-representative.','All-attempt accuracy requires both complete valid structure and label agreement; it conflates output completion with classification and cannot diagnose comprehension alone.','Relevant synthetic context repeats the scenario English gloss and can act as an oracle semantic scaffold; it is not naturally retrieved evidence.']}
    (run_dir/'analysis.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    meta=json.loads((run_dir/'model_metadata.json').read_text())
    lines=['# New controlled-context experiment results','',f"Status: {result['status']}. {len(raw)}/{len(cells)} calls recorded; {result['valid_calls']} structurally valid outputs; {result['invalid_or_error_calls']} invalid/error outputs.",'',f"Model: `{meta['model']['name']}`; digest `{meta['model']['digest']}`. {design['n_scenarios']} existing development scenarios, two per existing category. New model generations, not a new held-out dataset. No expert annotations.",'','## Design','', 'Three query representations (English gloss, romanized Tulu, Kannada-script Tulu), four English synthetic-context conditions, and baseline versus fidelity-guard instruction. Context is identical across query representations. `relevant_source_details` adds age 47 and year 2019 to a separate illustrative case. These are absent from selected complaint glosses. The irrelevant condition uses a different category. No real court documents were sent to the model.','', 'One generation per cell, fixed seed and temperature. Order and all 384 inputs were frozen before this run. Two earlier 180-token smoke-test calls truncated; they remain in the v1 directory. The main v2 generation budget is 512. This is exploratory, not an independent replication of the original three models.','', '## Condition summary','', '| Query | Context | Policy | Attempts | Valid | Correct primary | Literal marker echo / valid |','|---|---|---|---:|---:|---:|---|']
    for x in summary:lines.append(f"| {x['script']} | {x['context_condition']} | {x['policy']} | {x['attempts']} | {x['valid_outputs']} | {x['primary_correct_all_attempts']} | {x['marker_echo_valid_outputs']}/{x['marker_echo_valid_denominator']} |")
    lines+=['','Invalid outputs count as category errors. Marker results are not expert-annotated intrusion rates; inspect raw facts and denominators. Rows with no source details are negative-control screens, not exposure contrasts.','', '## Paired exploratory prompt comparisons','', 'Differences are fidelity guard minus baseline. Accuracy retains all 16 attempts per cell; marker comparisons require both structured outputs to be valid. Holm correction is separate for the 12 accuracy and six marker comparisons when complete. Negative marker differences mean fewer literal echoes, not proven safer assistance.','', '| Query | Context | Metric | Paired n | Baseline only | Guard only | Delta pp | Exact p | Holm p |','|---|---|---|---:|---:|---:|---:|---:|---:|']
    for x in pairs:
        delta='NA' if x['guard_minus_baseline_pp'] is None else f"{x['guard_minus_baseline_pp']:+.1f}";p='NA' if x['p_exact'] is None else f"{x['p_exact']:.5f}";h='NA' if x['p_holm_within_metric'] is None else f"{x['p_holm_within_metric']:.5f}"
        lines.append(f"| {x['script']} | {x['context_condition']} | {x['metric']} | {x['paired_cases']} | {x['baseline_only']} | {x['guard_only']} | {delta} | {p} | {h} |")
    lines+=['','## Interpretation boundaries','']+['- '+x for x in result['interpretation_limits']]+['','The manuscript incorporates these outputs as an exploratory development diagnostic, not validated fidelity evidence. Human fidelity labels and referral outcomes remain absent.']
    (run_dir/'EXPERIMENT_REPORT.md').write_text('\n'.join(lines)+'\n')
    if complete:(run_dir/'RESULTS.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({k:result[k] for k in ['status','attempted_calls','valid_calls','invalid_or_error_calls']}))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('run_dir',type=Path);a=p.parse_args();main(a.run_dir)
