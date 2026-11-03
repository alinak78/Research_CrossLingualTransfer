"""Offline sensitivity audit. No inference, expert labels, or population inference.

Missing marker outcomes are bounded over all attempts, without imputing them.
Lexical connected components are stress-test groups, not validated templates.
"""
from pathlib import Path
from collections import defaultdict,Counter
import csv,hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
RUN=ROOT/'experiments/runs/2026-10-30_local1b_v2'
SOURCE=ROOT.parent/'Research-TuluLegalRAG/data'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bounds(b_echo,b_valid,g_echo,g_valid,n):
    assert 0<=b_echo<=b_valid<=n and 0<=g_echo<=g_valid<=n
    return [100*(g_echo-b_echo-(n-b_valid))/n,100*(g_echo+(n-g_valid)-b_echo)/n]
def tokens(t):return set(re.findall(r'[a-z]+',t.lower()))
def components(rows,threshold):
    ids=sorted(rows);parent={i:i for i in ids}
    def root(i):
        while parent[i]!=i:i=parent[i]
        return i
    sets={i:tokens(rows[i]['english_gloss']) for i in ids}
    for j,a in enumerate(ids):
        for b in ids[j+1:]:
            union=sets[a]|sets[b];score=len(sets[a]&sets[b])/len(union) if union else 1
            if score>=threshold:parent[root(a)]=root(b)
    groups=defaultdict(list)
    for i in ids:groups[root(i)].append(i)
    return sorted(groups.values(),key=lambda g:g[0])
def span(xs):return [min(xs),max(xs)]
def main():
    # Extreme missingness cases and known complete pairs must agree with direct arithmetic.
    assert bounds(0,0,0,0,16)==[-100,100]
    assert bounds(11,16,5,12,16)==[-37.5,-12.5]
    assert bounds(2,16,5,16,16)==[18.75,18.75]
    rows={r['id']:r for r in map(json.loads,(SOURCE/'tulu_legal_60_consolidated.jsonl').read_text().splitlines())}
    answers=list(csv.DictReader((RUN/'answers.csv').open()))
    analysis=json.loads((RUN/'analysis.json').read_text())
    lookup={(x['script'],x['context_condition'],x['policy']):x for x in analysis['summary']}
    failures=Counter((a['script'],a['policy']) for a in answers if a['status']!='ok')
    marker=[]
    for script in ['english','romanized','kannada']:
        for ctx in ['relevant_source_details','irrelevant_source_details']:
            b=lookup[script,ctx,'baseline'];g=lookup[script,ctx,'fidelity_guard']
            marker.append({'script':script,'context':ctx,'attempts_per_policy':16,'baseline_echo':b['marker_echo_valid_outputs'],'baseline_valid':b['valid_outputs'],'guard_echo':g['marker_echo_valid_outputs'],'guard_valid':g['valid_outputs'],'guard_minus_baseline_marker_bounds_pp':bounds(b['marker_echo_valid_outputs'],b['valid_outputs'],g['marker_echo_valid_outputs'],g['valid_outputs'],16)})
    # All-attempt label score has a defined failure-as-error convention; omission
    # stress tests assess leverage and do not turn failures into latent correctness.
    indexed={(int(a['scenario_id']),a['script'],a['context_condition'],a['policy']):a for a in answers}
    ids=sorted({int(a['scenario_id']) for a in answers});categories=sorted({rows[i]['list_category'] for i in ids})
    leverage=[]
    for script in ['english','romanized','kannada']:
        for ctx in ['none','relevant','relevant_source_details','irrelevant_source_details']:
            delta={i:int(indexed[i,script,ctx,'fidelity_guard']['primary_correct']=='True')-int(indexed[i,script,ctx,'baseline']['primary_correct']=='True') for i in ids}
            loo=[100*sum(v for j,v in delta.items() if j!=i)/15 for i in ids]
            loc=[100*sum(v for j,v in delta.items() if rows[j]['list_category']!=c)/14 for c in categories]
            leverage.append({'script':script,'context':ctx,'delta_pp':100*sum(delta.values())/16,'leave_one_scenario_out_range_pp':span(loo),'leave_one_category_out_range_pp':span(loc)})
    old={}
    for path in sorted((ROOT.parent/'Research-TuluLegalRAG/outputs').glob('tulu_mega_*.csv')):
        for a in csv.DictReader(path.open()):
            if a['model']=='llama3' and a['condition'] in ['D_full','E_full']:
                old[int(a['id']),a['condition']]=a['pred_top1']==a['list_primary']
    assert len(old)==120
    diff={i:int(old[i,'D_full'])-int(old[i,'E_full']) for i in rows}
    cluster=[]
    for threshold in [.3,.4,.5,.7,1.]:
        groups=components(rows,threshold)
        means=[sum(diff[i] for i in g)/len(g) for g in groups]
        cluster.append({'jaccard_threshold':threshold,'components':groups,'n_components':len(groups),'largest_component':max(map(len,groups)),'equal_component_weight_delta_pp':100*sum(means)/len(means),'leave_one_component_out_delta_range_pp':span([100*sum(diff[j] for j in rows if j not in g)/(60-len(g)) for g in groups])})
    # A rights/provenance inventory records files and hashes, not court narratives.
    corpus=SOURCE/'kannada_legal_corpus_list.jsonl'
    provenance={'source_file':'kannada_legal_corpus_list.jsonl','sha256':sha(corpus),'record_count':sum(bool(x.strip()) for x in corpus.read_text().splitlines()),'extraction_verification':'not independently verified; source reports model-assisted correction','personal_information':'known risk; not copied into this audit','redistribution_rights':'unresolved; corpus excluded from public package','new_local_experiment_uses_corpus':False,'release_gate':'Do not distribute court text until rights, redaction, and extraction checks are completed.'}
    result={'status':'post-hoc descriptive sensitivity audit; no confirmatory inference','marker_bounds':marker,'failure_counts':[{'script':s,'policy':p,'invalid':failures[s,p],'attempts':64} for s in ['english','romanized','kannada'] for p in ['baseline','fidelity_guard']],'category_leverage':leverage,'archive_lexical_stress_test':cluster,'corpus_provenance':provenance,'demographics':{'observed_speaker_demographics':None,'participant_count':0,'authored_scenarios':60,'new_experiment_reused_scenarios':16,'dialect_literacy_and_service_experience':'not collected; do not infer from text'},'inputs':{str(p.relative_to(ROOT.parent)):sha(p) for p in [RUN/'predictions.jsonl',RUN/'schedule.jsonl',RUN/'answers.csv',SOURCE/'tulu_legal_60_consolidated.jsonl']},'code_sha256':sha(Path(__file__))}
    out=ROOT/'analysis';(out/'robustness.json').write_text(json.dumps(result,indent=2)+'\n')
    lines=['# Post-hoc robustness and provenance audit','','No new model calls, expert annotations, demographic observations, or court excerpts. These checks narrow claims; they do not validate complaint fidelity.','','## Missing-output bounds','','All 16 attempts per policy remain in the estimand. Each invalid output can have either marker outcome. Bounds describe an unknown full-output literal-marker outcome, not intrusion or an estimate of what a longer generation would produce. They are identification bounds, not confidence intervals.','','| Query | Context | Baseline echo / valid | Guard echo / valid | Guard minus baseline bound (pp) |','|---|---|---|---|---|']
    for x in marker:
        lo,hi=x['guard_minus_baseline_marker_bounds_pp'];lines.append(f"| {x['script']} | {x['context']} | {x['baseline_echo']}/{x['baseline_valid']} | {x['guard_echo']}/{x['guard_valid']} | [{lo:+.2f}, {hi:+.2f}] |")
    lines+=['','A bound excluding zero concerns this finite sample and literal marker only, without sampling uncertainty. It does not override nonsignificant paired tests or establish a safeguard effect.','','## Completion by representation and policy','','| Query | Policy | Invalid / attempts |','|---|---|---|']
    for x in result['failure_counts']:lines.append(f"| {x['script']} | {x['policy']} | {x['invalid']}/{x['attempts']} |")
    lines+=['','## Category leverage','','All-attempt scoring retains invalids as errors. Omission is a descriptive sensitivity analysis, not a new statistical test. Category groups are stress-test strata, not verified authoring templates.','','| Query | Context | Guard minus baseline (pp) | Leave one scenario range | Leave one category range |','|---|---|---|---|---|']
    for x in leverage:lines.append(f"| {x['script']} | {x['context']} | {x['delta_pp']:+.2f} | {x['leave_one_scenario_out_range_pp']} | {x['leave_one_category_out_range_pp']} |")
    lines+=['','## Archive lexical dependence stress test','','English glosses are lowercased and tokenized to letter-only sets. Undirected edges join Jaccard scores at or above the threshold; connected components are deterministic stress-test groups. Transitivity can merge dissimilar endpoints. These are not validated semantic or authoring-template clusters. No independence claim, cluster p-value, or population interval is attached. The archived Llama3 D_full minus E_full difference is -36.67 pp.','','| Threshold | Components | Largest | Equal-component-weight delta (pp) | Leave one component range |','|---|---|---|---|---|']
    for x in cluster:lines.append(f"| {x['jaccard_threshold']} | {x['n_components']} | {x['largest_component']} | {x['equal_component_weight_delta_pp']:+.2f} | {x['leave_one_component_out_delta_range_pp']} |")
    lines+=['','## Corpus and representation boundaries','',json.dumps(provenance,indent=2),'','No speaker demographics, dialect balance, linguistic equivalence, category validity, or legal routes are inferred. Review status remains unverified. The original 60 cases and the selected 16 are authored development materials, not samples of 60 or 16 participants. Pinned local metadata improves auditability of the new run but does not reconstruct historical services.']
    (out/'ROBUSTNESS.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({'marker_bounds':marker,'failures':result['failure_counts'],'cluster_stress':[{k:v for k,v in x.items() if k!='components'} for x in cluster]},indent=2))
if __name__=='__main__':main()
