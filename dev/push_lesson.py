# Gebruik: python3 push_lesson.py a1-u4-l1 [meer ids]  -> print SQL om die lessen (zoals nu in spaans-leren.html) in D1 te zetten
import sys,json,re
c=open('/home/claude/spaans-leren.html',encoding='utf-8').read(); dec=json.JSONDecoder()
out=[]
for lid in sys.argv[1:]:
    m=re.search(r"\{ id:[\"']"+re.escape(lid)+r"[\"'],", c); s=m.start()
    w,we=dec.raw_decode(c,c.index('[',c.index('words:',s))); se,_=dec.raw_decode(c,c.index('[',c.index('sentences:',we)))
    uid=lid.rsplit('-',1)[0]; lvl=uid.split('-')[0].upper(); idx=int(re.search(r'-l(\d+)$',lid).group(1))-1
    q=lambda x:"'"+x.replace("'","''")+"'"
    out.append(f"INSERT OR IGNORE INTO units (id,level,idx,is_ai) VALUES ({q(uid)},{q(lvl)},0,0);")
    out.append(f"INSERT OR REPLACE INTO lessons (id,unit_id,idx,words_json,sentence_json) VALUES ({q(lid)},{q(uid)},{idx},{q(json.dumps(w,ensure_ascii=False))},{q(json.dumps(se,ensure_ascii=False))});")
print('\n'.join(out))
