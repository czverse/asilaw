import re,sys,os,statistics as st
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','chapters')
CAPS={'did_not_say':(r"did not say anything|nobody said anything|didn't say anything",1),
'long_time':(r'for a (very )?long time',1),'still':(r'very still|went still',1),
'the_way':(r'\bthe way (a|an|you|someone|people|the)\b',2),'notx':(r'(?m)^Not [^.\n]{1,50}\. Not ',1),
'very':(r'\bvery\b',6),'something':(r'\bsomething\b',6),'a_little':(r'\ba little\b',3),
'tell_first':(r'telling you first|told (him|her|them|you) first',1),'rule_obv':(r"that's the rule|that is the rule|\bobviously\b",1),
'capitals':(r'square black capitals',1),'banned':(r'almost smiled|face did (a|the) thing|face was doing',0),
'he_says_run':(None,3)}
for n in sys.argv[1:]:
    f=os.path.join(D,f'ch{int(n):02d}.md' if int(n)<100 else f'ch{n}.md')
    t=open(f).read()
    out=[]
    for k,(p,c) in CAPS.items():
        if p is None:
            runs=max([len(m) for m in re.findall(r'(?:> \*\*(?:He|She) says[^\n]*\n(?:>\n)?)+',t)] or [0])
            v=max([m.count('says') for m in re.findall(r'(?:> \*\*(?:He|She) says[^\n]*\n(?:>\n)?)+',t)] or [0])
        else: v=len(re.findall(p,t,re.I))
        if v>c: out.append(f'{k}={v}>{c}')
    body=re.sub(r'[>*#]','',t)
    S=[len(s.split()) for s in re.split(r'(?<=[.!?])\s+',body) if s.strip()]
    paras=[p for p in t.split('\n\n') if p.strip() and not p.startswith('##') and p.strip()!='---']
    sp=round(100*sum(len(p.split())<=6 for p in paras)/len(paras))
    sim=len(re.findall(r'\blike (a|an|the|someone)\b|\bas if\b',t))
    w=len(t.split())
    print(n,'words',w,'sent_mean',round(st.mean(S),1),'short%',sp,'similes/500w',round(sim*500/w,2),'OVER:',out or 'none')
