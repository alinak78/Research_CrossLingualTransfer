"""Offline matched audit of archived predictions. No model calls or third-party packages."""
from pathlib import Path
import csv, json, hashlib, math
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / 'Research-TuluLegalRAG'
PAIRS = [('H','G','script_unprimed'), ('E_sparse','M_sparse','script_sparse'),
         ('E_full','M_full','script_full'), ('F','H','retrieval_unprimed'),
         ('D_sparse','E_sparse','retrieval_sparse'), ('D_full','E_full','retrieval_full')]

def exact_p(b, c):
    n = b+c
    return min(1.0, 2*sum(math.comb(n,k) for k in range(min(b,c)+1))/2**n) if n else 1.0

def wilson(k,n):
    z=1.959963984540054; p=k/n; d=1+z*z/n
    mid=(p+z*z/(2*n))/d
    half=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return [mid-half,mid+half]

def main():
    gold = {str(r['id']):r['list_category'] for r in map(json.loads,(SOURCE/'data/tulu_legal_60_consolidated.jsonl').read_text().splitlines())}
    rows={}; manifest=[]; groups=defaultdict(dict)
    for path in sorted((SOURCE/'outputs').glob('tulu_mega_*.csv')):
        manifest.append({'path':str(path.relative_to(ROOT.parent)), 'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
        for row in csv.DictReader(path.open()):
            key=(row['model'],row['condition'],row['id'])
            if key in rows: raise ValueError(f'Duplicate prediction: {key}')
            if row['list_primary'] != gold[row['id']]: raise ValueError(f'Gold mismatch: {key}')
            row['correct']=row['pred_top1']==gold[row['id']]
            if row['correct'] != (row['hits1']=='True'): raise ValueError(f'Score mismatch: {key}')
            rows[key]=row; groups[key[:2]][key[2]]=row
    for key,g in groups.items():
        if set(g)!=set(gold): raise ValueError(f'Incomplete group: {key}')
    assert len(groups)==57 and len(rows)==3420
    summary=[]
    for (model,condition),g in sorted(groups.items()):
        k=sum(r['correct'] for r in g.values()); n=len(g)
        summary.append(dict(model=model,condition=condition,n=n,correct=k,accuracy=k/n,
                            wilson95=wilson(k,n),invalid=sum(r['pred_top1'] in {'ERROR','PARSE_FAILURE_NO_ANSWER',''} for r in g.values())))
    comparisons=[]
    for model in sorted({k[0] for k in groups}):
        for a,b,label in PAIRS:
            ga,gb=groups[model,a],groups[model,b]
            wins=sum(ga[i]['correct'] and not gb[i]['correct'] for i in gold)
            losses=sum(gb[i]['correct'] and not ga[i]['correct'] for i in gold)
            flips=sum(ga[i]['pred_top1']!=gb[i]['pred_top1'] for i in gold)
            comparisons.append(dict(model=model,a=a,b=b,contrast=label,n=len(gold),
                a_only_correct=wins,b_only_correct=losses,label_flips=flips,
                delta_pp=100*(wins-losses)/len(gold),p_exact=exact_p(wins,losses)))
    running=0
    for rank,r in enumerate(sorted(comparisons,key=lambda x:x['p_exact'])):
        running=max(running,min(1,(len(comparisons)-rank)*r['p_exact']))
        r['p_holm']=running
    out=ROOT/'analysis'; out.mkdir(exist_ok=True)
    (out/'results.json').write_text(json.dumps(dict(status='exploratory reanalysis; contrasts selected after inspecting prior paper',
        n_unique_scenarios=len(gold),n_predictions=len(rows),summary=summary,comparisons=comparisons,manifest=manifest),indent=2)+'\n')
    lines=['# Recomputed pilot audit','', 'Unit: 60 authored scenarios, reused across conditions. Invalid outputs count as errors.',
           'Intervals are descriptive Wilson intervals over these scenarios, not population guarantees.',
           'Exact paired McNemar tests; Holm correction across all 18 selected contrasts. Exploratory, not preregistered.','',
           '| Model | A | H | G | E_sparse | E_full | F | D_sparse | D_full |',
           '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    lookup={(r['model'],r['condition']):r for r in summary}
    for model in ['llama3','hex1','sarvam']:
        lines.append('| '+model+' | '+' | '.join(f"{lookup[model,c]['correct']}/60" for c in ['A','H','G','E_sparse','E_full','F','D_sparse','D_full'])+' |')
    lines+=['','A: English + RAG; H/G: Kannada/romanized unprimed without RAG; E: Kannada primed without RAG; F: Kannada unprimed + RAG; D: Kannada primed + RAG.','',
            '| Model | A vs B | Contrast | Delta pp | A only correct | B only correct | Label flips | Exact p | Holm p |',
            '|---|---|---|---:|---:|---:|---:|---:|---:|']
    for r in comparisons:
        lines.append(f"| {r['model']} | {r['a']} vs {r['b']} | {r['contrast']} | {r['delta_pp']:+.1f} | {r['a_only_correct']} | {r['b_only_correct']} | {r['label_flips']} | {r['p_exact']:.5f} | {r['p_holm']:.5f} |")
    lines+=['','English without RAG is absent: A cannot establish the effect of retrieval in English.',
            'All 3,420 source rows have unique model/condition/scenario keys and agree with JSONL primary labels and archived hits1 scores.',
            f"Invalid primary outputs: {sum(r['invalid'] for r in summary)}. No API calls were made."]
    (out/'RESULTS.md').write_text('\n'.join(lines)+'\n')
    print('\n'.join(lines))

if __name__=='__main__': main()
