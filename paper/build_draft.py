"""Build the complete manuscript from manuscript_source.md and verified audit tables."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'analysis/results.json').read_text())
SUMMARY={(r['model'],r['condition']):r for r in DATA['summary']}
MODELS=['llama3','hex1','sarvam']
REFS={
 'injecagent':('Zhan et al. (2024). InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents. Findings of ACL, 10471-10506.','https://aclanthology.org/2024.findings-acl.624/'),
 'prior':('Shetty et al. (2026). Cross Lingual Transfer in Tulu Legal Comprehension: Script-Dependent Improvement and RAG-Induced Knowledge Conflict. ORACLE, 107-133.','https://aclanthology.org/2026.oracle-main.8/'),
 'selbst':('Selbst et al. (2019). Fairness and Abstraction in Sociotechnical Systems. FAT*, 59-68.','https://doi.org/10.1145/3287560.3287598'),
 'joshi':('Joshi et al. (2020). The State and Fate of Linguistic Diversity and Inclusion in the NLP World. ACL, 6282-6293.','https://aclanthology.org/2020.acl-main.560/'),
 'bender':('Bender and Friedman (2018). Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science. TACL 6, 587-604.','https://aclanthology.org/Q18-1041/'),
 'bird':('Bird (2020). Decolonising Speech and Language Technology. COLING, 3504-3519.','https://aclanthology.org/2020.coling-main.313/'),
 'magesh':('Magesh et al. (2024). Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools. arXiv:2405.20362.','https://arxiv.org/abs/2405.20362'),
 'list':('Stanford Legal Design Lab. Legal Issues Taxonomy (LIST). Accessed October 27, 2026.','https://betterinternet.law.stanford.edu/about-the-project/taxonomy-nsmiv2/')}
def esc(text):
    text=re.sub(r'[\\&%$#_{}~^]',lambda m:{'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}[m[0]],text)
    return re.sub(r'\[([a-z]+)\]',lambda m:r'\cite{'+m[1]+'}' if m[1] in REFS else m[0],text)
def make_table(caption,headers,rows,widths=None,label=''):
    md='| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'
    md+='\n'.join('| '+' | '.join(map(str,row))+' |' for row in rows)
    spec=''.join('p{'+str(w)+r'\linewidth}' for w in widths) if widths else 'l'+'r'*(len(headers)-1)
    tex='\\begin{table}[htbp]\n\\caption{'+esc(caption)+'}\n'
    if label:tex+='\\label{'+label+'}\n'
    tex+='\\centering\n\\begin{tabular}{@{}'+spec+'@{}}\n\\toprule\n'
    tex+=' & '.join(esc(x) for x in headers)+r' \\'+'\n\\midrule\n'
    tex+='\n'.join(' & '.join(esc(str(x)) for x in row)+r' \\' for row in rows)
    tex+='\n\\bottomrule\n\\end{tabular}\n\\end{table}\n'
    return '**'+caption+'**\n\n'+md,tex
TABLES={}
TABLES['TABLE_FRAMEWORK']=make_table('Evaluation layers and the evidence needed to assess them.',
 ['Layer','Audit question','Evidence in this paper'],[
 ['Category reproduction','Does the output match the designated primary label?','Completed on archived predictions; labels not independently validated.'],
 ['Complaint fidelity','Are assertions about this complaint supported by the account?','Operational definition and prospective annotation; no expert-labeled fidelity results.'],
 ['Referral validity','Is the next step appropriate for a specified service?','Institutional validation proposed; no observed referral outcomes.']],
 [.18,.32,.40],'tab:framework')
TABLES['TABLE_CONDITIONS']=make_table('Conditions used in the selected paired comparisons.',
 ['Code','Query representation','Priming','Retrieval'],[
 ['G / H','Romanized / Kannada-script Tulu','None','No'],
 ['M_sparse / E_sparse','Romanized / Kannada-script Tulu','Sparse','No'],
 ['M_full / E_full','Romanized / Kannada-script Tulu','Full','No'],
 ['F','Kannada-script Tulu','None','Yes'],
 ['D_sparse / D_full','Kannada-script Tulu','Sparse / full','Yes'],
 ['A','English gloss','None','Yes']], [.24,.34,.15,.11],'tab:conditions')
cols=['H','G','E_sparse','E_full','F','D_sparse','D_full']
TABLES['TABLE_ACCURACY']=make_table('Correct primary labels out of 60 scenarios; all invalid outputs count as errors.',
 ['Model','H','G','E sparse','E full','F','D sparse','D full'],
 [[m]+[f"{SUMMARY[m,c]['correct']}/60" for c in cols] for m in MODELS],label='tab:accuracy')
retrieval=[next(r for r in DATA['comparisons'] if r['model']==m and r['contrast']=='retrieval_full') for m in MODELS]
TABLES['TABLE_REVERSALS']=make_table('Full-priming Kannada-script retrieval contrasts. Reversals become incorrect; recoveries become correct.',
 ['Model','Reversals','Recoveries','Label changes','Delta pp','Holm p'],
 [[r['model'],r['b_only_correct'],r['a_only_correct'],r['label_flips'],f"{r['delta_pp']:+.1f}",f"{r['p_holm']:.5f}"] for r in retrieval], label='tab:reversals')
allpairs=[]
for m in MODELS:
 for r in DATA['comparisons']:
  if r['model']!=m:continue
  allpairs.append([m,r['a']+' vs '+r['b'],r['a_only_correct'],r['b_only_correct'],r['label_flips'],f"{r['delta_pp']:+.1f}",f"{r['p_exact']:.6f}",f"{r['p_holm']:.6f}"])
TABLES['TABLE_ALL_PAIRS']=make_table('All 18 selected paired comparisons. Positive differences favor condition A, the first condition in the pair.',
 ['Model','A vs B','A only','B only','Changes','Delta pp','Exact p','Holm p'],allpairs,
 [.08,.27,.06,.06,.07,.07,.10,.10],'tab:all-pairs')
def main():
    source=(ROOT/'paper/manuscript_source.md').read_text();blocks=re.split(r'\n\s*\n',source.strip())
    title=blocks[0].removeprefix('# ')
    notice='Working manuscript. Existing model results are reused from the published ORACLE 2026 pilot. The proposed direct complaint-fidelity study is not yet executed; publication eligibility is unresolved for any future distinct submission.'
    md=source
    for key,(mt,_) in TABLES.items():md=md.replace('['+key+']',mt)
    md=md.replace('[BIBLIOGRAPHY]','\n\n'.join(f'[{k}] {t} [Source]({u})' for k,(t,u) in REFS.items()))
    md=md.replace('# '+title,'# '+title+'\n\n**'+notice+'**',1)
    (ROOT/'paper/manuscript.md').write_text(md.rstrip()+'\n')
    abstract=blocks[2];assert blocks[1]=='## Abstract'
    tex=r'''\documentclass[manuscript,screen,review,anonymous]{acmart}
\usepackage{booktabs}
\setcopyright{none}
\settopmatter{printacmref=false}
\renewcommand\footnotetextcopyrightpermission[1]{}
\acmConference[ACM FAccT 2027]{ACM Conference on Fairness, Accountability, and Transparency}{June 21--24, 2027}{}
\title{'''+esc(title)+r'''}
\begin{document}
\begin{abstract}
'''+esc(abstract)+r'''
\end{abstract}
\ccsdesc[500]{Computing methodologies~Natural language processing}
\ccsdesc[300]{Social and professional topics~Computing / technology policy}
\keywords{complaint fidelity, language equity, legal intake, Tulu, retrieval-augmented generation, sociotechnical evaluation}
\maketitle
\begin{quote}\small '''+esc(notice)+r'''\end{quote}
'''
    appendix_started=False
    for block in blocks[3:]:
        if block.startswith('## '):
            heading=block[3:]
            if heading=='Ethical considerations and adverse impacts':tex+='\n\\clearpage\n'
            if heading in {'Ethical considerations and adverse impacts','Generative AI usage statement'}:tex+='\n\\section*{'+esc(heading)+'}\n'
            elif heading=='References':tex+='\n\\clearpage\n'
            elif heading.startswith('Appendix:'):
                tex+='\n\\clearpage\n'
                if not appendix_started:
                    tex+='\\appendix\n';appendix_started=True
                tex+='\\section{'+esc(heading.removeprefix('Appendix: '))+'}\n'
            else:tex+='\n\\section{'+esc(heading)+'}\n'
        elif block.startswith('### '):tex+='\n\\subsection{'+esc(block[4:])+'}\n'
        elif block=='[BIBLIOGRAPHY]':tex+='\\bibliographystyle{ACM-Reference-Format}\n\\bibliography{references}\n'
        elif block.startswith('[TABLE_'):tex+=TABLES[block[1:-1]][1]
        else:tex+='\n'+esc(block)+'\n'
    tex+='\n\\end{document}\n'
    assert not re.search(r'\[(?:TABLE_|BIBLIOGRAPHY)',tex)
    (ROOT/'paper/main.tex').write_text(tex)
    (ROOT/'docs/pilot_abstract_NOT_FOR_SUBMISSION.txt').write_text('WORKING ABSTRACT - DISTINCT STUDY INCOMPLETE\n\n'+title+'\n\n'+abstract+'\n')
    print('Built manuscript.md and main.tex;',len(re.findall(r'\b\w+\b',source)), 'source words;',len(re.findall(r'^## ',source,re.M)),'top-level sections.')
if __name__=='__main__':main()
