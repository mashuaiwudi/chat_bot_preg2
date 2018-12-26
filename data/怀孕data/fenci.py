#encoding=utf-8
import jieba
import jieba.posseg as pseg
import re
filename='fenci/tgt-val.txt'
fileneedCut='tgt-val.txt'
fn=open(fileneedCut,"r",encoding='utf-8')
f=open(filename,"w+", encoding='utf-8')
for line in fn.readlines():
    result = re.findall(r'.{1}', line)
    for i in range(len(result)-1):
    	f.write(result[i])
    	f.write(' ')
    f.write(result[-1])
    f.write('\n')







    #words=pseg.cut(line)
    #for w in words:
    #    print >>f,str(w)
f.close()
fn.close()