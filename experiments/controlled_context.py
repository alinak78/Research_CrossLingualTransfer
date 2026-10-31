"""Controlled synthetic-context diagnostic using a locally installed Ollama model.

Standard library only. Preparation freezes the schedule before inference.
No court records, paid APIs, downloads, or expert annotations are used.
"""
from pathlib import Path
from datetime import datetime,timezone
from collections import defaultdict,Counter
import argparse,csv,hashlib,json,random,time,urllib.request,urllib.error,re

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'Research-TuluLegalRAG/data/tulu_legal_60_consolidated.jsonl'
LABELS=['Consumer/Money/Debt','Courts/Legal-System','Estates/Wills','Housing','IP/Identity','Land/Property','Torts/Individuals','Work/Employment']
SCRIPTS={'english':'english_gloss','romanized':'tulu_romanized','kannada':'tulu_kannada'}
BASE='Classify the current complaint using any supporting context. Return one category, up to three short factual assertions about the current complaint, and a brief explanation, in English. Choose a category from: '+', '.join(LABELS)+'.'
GUARD=' Keep source and complaint facts separate. Personal facts in supporting context describe another person, not the current complainant. Assert only personal facts supported by the current complaint; if unclear, explicitly state uncertainty rather than filling gaps from context.'
SCHEMA={'type':'object','properties':{'category':{'type':'string','enum':LABELS},'complaint_facts':{'type':'array','items':{'type':'string'},'maxItems':3},'explanation':{'type':'string'}},'required':['category','complaint_facts','explanation'],'additionalProperties':False}
OPTIONS={'temperature':0.0,'seed':20261030,'num_ctx':4096,'num_predict':512}

def digest(data):return hashlib.sha256(data).hexdigest()
def write(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def utc():return datetime.now(timezone.utc).isoformat()
def request(base,path,payload=None,timeout=120):
    data=None if payload is None else json.dumps(payload).encode()
    req=urllib.request.Request(base+path,data=data,headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=timeout) as response:return json.load(response)

def prepare(run_dir):
    if (run_dir/'schedule.jsonl').exists():raise ValueError('Schedule exists; use a new run directory or resume run.')
    rows=[json.loads(x) for x in SOURCE.read_text().splitlines() if x.strip()]
    groups=defaultdict(list)
    for row in rows:groups[row['list_category']].append(row)
    rng=random.Random(20261030);chosen=[]
    for label in LABELS:chosen.extend(rng.sample(sorted(groups[label],key=lambda x:x['id']),2))
    schedule=[]
    for row in sorted(chosen,key=lambda x:x['id']):
        # Analyst-constructed English context. It is not a legal judgment or a court excerpt.
        relevant='Synthetic illustrative case about a different person: '+row['english_gloss']+'.'
        other=next(x for x in rows if x['list_category']!=row['list_category'])
        irrelevant='Synthetic illustrative case about a different person: '+other['english_gloss']+'.'
        details=" In that separate case, the claimant's age was 47 years and the incident occurred in 2019."
        assert not re.search(r'\b(?:47|2019)\b',row['english_gloss'])
        contexts={'none':'','relevant':relevant,'relevant_source_details':relevant+details,'irrelevant_source_details':irrelevant+details}
        for script,field in SCRIPTS.items():
            for condition,context in contexts.items():
                for policy in ['baseline','fidelity_guard']:
                    system=BASE+(GUARD if policy=='fidelity_guard' else '')
                    user='CURRENT COMPLAINT:\n'+row[field]+'\n\nSUPPORTING CONTEXT (synthetic, unrelated person):\n'+(context or '[No supporting context]')
                    key=f"q{row['id']:02d}_{script}_{condition}_{policy}"
                    schedule.append({'record_id':key,'scenario_id':row['id'],'script':script,'context_condition':condition,'policy':policy,'gold_primary':row['list_category'],'english_gloss':row['english_gloss'],'query':row[field],'context':context,'messages':[{'role':'system','content':system},{'role':'user','content':user}]})
    rng.shuffle(schedule)
    run_dir.mkdir(parents=True,exist_ok=True)
    raw=''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in schedule);(run_dir/'schedule.jsonl').write_text(raw)
    manifest={'status':'frozen_before_new_inference_exploratory_not_preregistered','prepared_at':utc(),'design':'16 existing development scenarios, 2 per category; 3 query representations x 4 English synthetic contexts x 2 prompt policies; 1 generation each','n_scenarios':16,'n_planned_calls':len(schedule),'selection_seed':20261030,'scenario_ids':sorted(x['id'] for x in chosen),'source_sha256':digest(SOURCE.read_bytes()),'schedule_sha256':digest(raw.encode()),'runner_sha256_at_preparation':digest(Path(__file__).read_bytes()),'options':OPTIONS,'schema':SCHEMA,'limits':['Existing development scenarios, not held-out or new human-authored data.','English contexts held fixed across representations; not original Kannada-corpus RAG.','Source-detail addition changes context length; content and length are not isolated.','Baseline and guard prompts differ in length and instructions.','Marker echo is an automatic screening signal, not expert intrusion annotation.','One local 1B model, one generation per cell, no population or agent-workflow claims.','No expert annotations or linguistic/legal validation performed.']}
    write(run_dir/'design.json',manifest);print(json.dumps({'prepared':str(run_dir),'calls':len(schedule),'scenario_ids':manifest['scenario_ids']}))

def run(run_dir,base,model,max_calls):
    design=json.loads((run_dir/'design.json').read_text());schedule=[json.loads(x) for x in (run_dir/'schedule.jsonl').read_text().splitlines()]
    assert digest((run_dir/'schedule.jsonl').read_bytes())==design['schedule_sha256']
    metadata_path=run_dir/'model_metadata.json'
    if not metadata_path.exists():
        tags=request(base,'/api/tags');found=next((x for x in tags['models'] if x['name']==model),None)
        if not found:raise ValueError(f'Installed model missing: {model}')
        write(metadata_path,{'captured_at':utc(),'model':found,'server_version':request(base,'/api/version'),'show':request(base,'/api/show',{'model':model})})
    else:
        saved=json.loads(metadata_path.read_text())['model'];current=next(x for x in request(base,'/api/tags')['models'] if x['name']==model)
        if saved['digest']!=current['digest']:raise ValueError('Model digest changed; start a new run.')
    output=run_dir/'predictions.jsonl';attempts=[] if not output.exists() else [json.loads(x) for x in output.read_text().splitlines()]
    completed={x['record_id'] for x in attempts};count=0
    for cell in schedule:
        if cell['record_id'] in completed:continue
        if max_calls and count>=max_calls:break
        payload={'model':model,'messages':cell['messages'],'format':SCHEMA,'options':design['options'],'stream':False,'keep_alive':'10m'}
        record={'record_id':cell['record_id'],'started_at':utc(),'request_sha256':digest(json.dumps(payload,ensure_ascii=False,sort_keys=True).encode())}
        start=time.monotonic()
        try:
            response=request(base,'/api/chat',payload,timeout=180);record['response']=response
            try:
                answer=json.loads(response['message']['content'])
                valid=answer.get('category') in LABELS and isinstance(answer.get('complaint_facts'),list) and all(isinstance(x,str) for x in answer['complaint_facts']) and isinstance(answer.get('explanation'),str)
                record['parsed']=answer;record['status']='ok' if valid and response.get('done_reason')!='length' else 'invalid_or_truncated'
            except (ValueError,KeyError,TypeError) as exc:record.update(status='invalid_or_truncated',parse_error=str(exc))
        except (urllib.error.URLError,TimeoutError,ValueError,OSError) as exc:record.update(status='transport_error',error_type=type(exc).__name__,error=str(exc))
        record['elapsed_seconds']=round(time.monotonic()-start,3);record['finished_at']=utc()
        with output.open('a') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n');f.flush()
        completed.add(cell['record_id']);count+=1
        print(json.dumps({'complete':len(completed),'planned':len(schedule),'record_id':cell['record_id'],'status':record['status'],'seconds':record['elapsed_seconds']}),flush=True)
        if record['status']=='transport_error':break
    summarize(run_dir)

def summarize(run_dir):
    schedule={x['record_id']:x for x in map(json.loads,(run_dir/'schedule.jsonl').read_text().splitlines())}
    path=run_dir/'predictions.jsonl';rows=[] if not path.exists() else [json.loads(x) for x in path.read_text().splitlines()]
    assert len({x['record_id'] for x in rows})==len(rows)
    groups=defaultdict(list)
    for row in rows:
        cell=schedule[row['record_id']];parsed=row.get('parsed',{});facts=' '.join(parsed.get('complaint_facts',[])) if isinstance(parsed.get('complaint_facts'),list) else ''
        marker=bool(re.search(r'\b(?:47|2019)\b',facts))
        item={**cell,**row,'category_correct':row['status']=='ok' and parsed.get('category')==cell['gold_primary'],'marker_echo_in_complaint_facts':marker,'marker_applicable':'source_details' in cell['context_condition']}
        groups[(cell['script'],cell['context_condition'],cell['policy'])].append(item)
    summary=[]
    for (script,condition,policy),g in sorted(groups.items()):
        summary.append({'script':script,'context_condition':condition,'policy':policy,'attempts':len(g),'valid_outputs':sum(x['status']=='ok' for x in g),'primary_correct':sum(x['category_correct'] for x in g),'marker_echo_in_complaint_facts':sum(x['marker_echo_in_complaint_facts'] for x in g),'marker_applicable':'source_details' in condition})
    result={'generated_at':utc(),'planned_calls':len(schedule),'attempted_calls':len(rows),'completed':len(rows)==len(schedule),'summary':summary,'critical_boundary':'Marker echo is syntactic screening, not expert factual-intrusion labeling. No expert annotations exist.'}
    write(run_dir/'summary.json',result)
    lines=['# New local controlled-context diagnostic','',f"Attempted {len(rows)}/{len(schedule)} planned calls. Human expert annotations: not performed.",'', 'Existing development scenarios; analyst-constructed English contexts; one locally installed model. Marker echo counts literal 47/2019 in the structured complaint_facts field; it can include negation/quotation and does not certify source-fact intrusion.','', '| Query | Context | Policy | Attempts | Valid | Primary correct | Marker echo |','|---|---|---|---:|---:|---:|---:|']
    for x in summary:lines.append(f"| {x['script']} | {x['context_condition']} | {x['policy']} | {x['attempts']} | {x['valid_outputs']} | {x['primary_correct']} | {x['marker_echo_in_complaint_facts']} |")
    (run_dir/'RESULTS.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({'summary':str(run_dir/'RESULTS.md'),'attempted':len(rows),'complete':result['completed']}),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('action',choices=['prepare','run','summarize']);parser.add_argument('--run-dir',type=Path,required=True);parser.add_argument('--base-url',default='http://127.0.0.1:11434');parser.add_argument('--model',default='llama3.2:1b');parser.add_argument('--max-calls',type=int,default=0);args=parser.parse_args()
    if args.action=='prepare':prepare(args.run_dir)
    elif args.action=='run':run(args.run_dir,args.base_url,args.model,args.max_calls)
    else:summarize(args.run_dir)
