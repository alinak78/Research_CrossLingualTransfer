"""Verify and package a completed local experiment. No inference or annotations."""
from pathlib import Path
from collections import Counter
from zipfile import ZipFile,ZIP_DEFLATED
import csv,hashlib,json,re,subprocess,sys

ROOT=Path(__file__).resolve().parents[1]
RUN=ROOT/'experiments/runs/2026-10-30_local1b_v2'

def sha(data):return hashlib.sha256(data).hexdigest()
def main():
    design=json.loads((RUN/'design.json').read_text())
    cells={x['record_id']:x for x in map(json.loads,(RUN/'schedule.jsonl').read_text().splitlines())}
    rows=[json.loads(x) for x in (RUN/'predictions.jsonl').read_text().splitlines()]
    assert len(rows)==384 and len(cells)==384
    assert {x['record_id'] for x in rows}==set(cells) and len({x['record_id'] for x in rows})==384
    assert sha((RUN/'schedule.jsonl').read_bytes())==design['schedule_sha256']
    for row in rows:
        cell=cells[row['record_id']]
        payload={'model':'llama3.2:1b','messages':cell['messages'],'format':design['schema'],'options':design['options'],'stream':False,'keep_alive':'10m'}
        assert sha(json.dumps(payload,ensure_ascii=False,sort_keys=True).encode())==row['request_sha256']
        assert row['started_at']>=design['prepared_at']
        assert row.get('response',{}).get('eval_count',0)>0
    assert all(v==24 for v in Counter(x['scenario_id'] for x in cells.values()).values())
    # Preserve exact original metadata locally; canonical shareable metadata replaces home paths only.
    for run in [ROOT/'experiments/runs/2026-10-30_local1b_v1',RUN]:
        path=run/'model_metadata.json'
        if not path.exists():continue
        original=path.read_bytes();obj=json.loads(original)
        if 'local_path_redaction' in obj:continue
        private=ROOT/'tmp/experiments_exact_metadata'/run.name;private.mkdir(parents=True,exist_ok=True)
        (private/'model_metadata.json').write_bytes(original)
        def clean(x):
            if isinstance(x,str):return re.sub(r'/Users/[^/\s\"\']+', '/Users/[local-user]',x)
            if isinstance(x,list):return [clean(v) for v in x]
            if isinstance(x,dict):return {k:clean(v) for k,v in x.items()}
            return x
        public=clean(obj);public['local_path_redaction']={'change':'Local home-directory names replaced only; model digest, template, parameters and response data unchanged.','exact_capture_sha256':sha(original),'exact_capture_preserved_locally':True}
        path.write_text(json.dumps(public,ensure_ascii=False,indent=2)+'\n')
    subprocess.run([sys.executable,str(ROOT/'experiments/analyze_controlled.py'),str(RUN)],check=True)
    subprocess.run([sys.executable,str(ROOT/'experiments/robustness_audit.py')],check=True,stdout=subprocess.DEVNULL)
    report=json.loads((RUN/'analysis.json').read_text());assert report['status']=='completed'
    assert len(report['summary'])==24 and all(x['attempts']==16 for x in report['summary'])
    assert len(report['secondary_exploratory_pairs'])==18
    assert all(x['expert_intrusion_count'] is None for x in report['summary'])
    for p in report['secondary_exploratory_pairs']:
        if p['p_exact'] is not None:assert 0<=p['p_exact']<=p['p_holm_within_metric']<=1
    files=[p for p in (ROOT/'experiments').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='ARTIFACT_MANIFEST.json']
    files.extend([ROOT/'analysis/ROBUSTNESS.md',ROOT/'analysis/robustness.json',ROOT/'docs/LIMITATION_MITIGATIONS.md'])
    manifest={str(p.relative_to(ROOT)):sha(p.read_bytes()) for p in files}
    (RUN/'ARTIFACT_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
    files.append(RUN/'ARTIFACT_MANIFEST.json')
    archive=ROOT/'output/facct_new_experiments_2026-10-30.zip';archive.parent.mkdir(exist_ok=True)
    with ZipFile(archive,'w',ZIP_DEFLATED) as z:
        for path in files:z.write(path,str(path.relative_to(ROOT)))
    with ZipFile(archive) as z:
        assert z.testzip() is None
        assert z.read(str((RUN/'predictions.jsonl').relative_to(ROOT)))==(RUN/'predictions.jsonl').read_bytes()
    print(json.dumps({'archive':str(archive),'calls':len(rows),'valid':report['valid_calls'],'invalid':report['invalid_or_error_calls'],'files':len(files)}))
if __name__=='__main__':main()
