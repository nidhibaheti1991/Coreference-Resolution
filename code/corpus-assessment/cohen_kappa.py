import glob
import re

path2 = 'coh_kap_2'

for index,name in enumerate(glob.glob(path2+'/*.txt')):

    file_nidhi = open(name, 'r')
    words_nidhi = file_nidhi.read().replace('\n', ' ').replace('|', ' ').strip()
    file_nidhi.close()

    name_saba=name.replace('_ann',' copy').replace('coh_kap_2','coh_kap')
    file_saba=open(name_saba,'r')
    words_saba = file_saba.read().replace('\n', ' ').replace('|', ' ').strip()
    file_saba.close()
    myre = re.compile(ur'<[0-9]{1,3}\,[PC][NR]{1,2}>',
                      re.UNICODE)
    print  name
    mentions_n = myre.findall(words_nidhi)
    # raw_input()
    for mention in mentions_n:
        abc= unicode(mention,encoding='utf-8')

    mentions_s=myre.findall(words_saba)
    # for mention in mentions_n:

    pn_count = 0
    prn_count = 0
    cn_count = 0
    max = 0

    print 'n: ',mentions_n
    print 's: ',mentions_s


    # raw_input()
