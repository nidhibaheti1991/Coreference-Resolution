import glob
import re

count_w=0

path1 = 'annotated-corpus'
path2 = 'stories'
output=open('output.txt','w')
for index,name in enumerate(glob.glob(path1+'/*.txt')):
    # print index+1,'\t', name
    output.write('\n'+str(index+1)+'.\t'+ name+'\n')
    file = open(name, 'r')
    words = file.read().replace('\n', ' ').replace('|', ' ').strip()
    file.close()
    mentions=re.findall("<[0-9]{1,3}\,[PC][NR]{1,2}>",words)
    pn_count=0
    prn_count=0
    cn_count=0
    max=0
    for mention in mentions:
        num= re.findall(r'\d+', mention)
        if num>max:
            max=num
        if 'PN' in mention:
            pn_count+=1
        elif'PRN' in mention:
            prn_count+=1
        else:
            cn_count+=1
    num_entities = max
    count_f=len(words.split(' '))
    count_w += count_f
    output.write('file_word_count: '+ str(count_f)+'\n'+'mention_count: '+str(len(mentions))+'\n')
    output.write('PN: '+str(pn_count)+' PRN: '+str(prn_count)+' CN: '+str(cn_count)+'\n')

output.write('\n\nTotal no of articles: '+str(index+1)+'\navg doc length: '+str(count_w/index+1)+' words/doc\ntotal word count: '+str(count_w)+' words')
