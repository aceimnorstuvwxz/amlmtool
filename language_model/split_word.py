#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
1,给lm的训练材料进行分词，并且去掉非lexicon内的词。

'''

import sys,re
import jieba
import num2chinese

reload(sys)
sys.setdefaultencoding("utf-8")


#分词
def replace_fuhao(l):
    '''只剩中文，留下空格'''
    a= re.findall(u"([\u4e00-\u9fff]+)", l)
    return " ".join(a)

cnt_eff = 0
cnt_miss = 0
cnt_split = 0
cnt_whole = 0


def number_to_zhcn(nb):
    if len(nb) >= 5:
        #may be tellphone 
        return num2chinese.num2cnphone(nb)
    else:
        return num2chinese.num2chinese(nb, big=False, simp=True, o=False, twoalt=True)



def replace_number(l):
    repat = re.compile(r'(\d+)')
    numbers = repat.findall(l)
    cnnumbs = [number_to_zhcn(nb) for nb in numbers]

    ret = l
    for nb,zh in zip(numbers, cnnumbs):
        ret = ret.replace(nb, zh, 1)

    return ret

def fenci(l):
        t = replace_fuhao(l)
        ww = jieba.cut(t, cut_all=False)
        ww = [w.strip() for w in ww]
        nww = []
        global cnt_eff, cnt_miss, cnt_split, cnt_whole
        for w in ww:
            if dict.has_key(w):
                nww.append(w)
                cnt_whole = cnt_whole + 1
            else:
                cnt_split = cnt_split + 1
                for iw in w:
                    if dict.has_key(iw):
                        nww.append(iw)
                        cnt_eff = cnt_eff + 1
                    else:
                        cnt_miss = cnt_miss + 1
        nl = ' '.join(nww)
        
        return nl + '\n'


#音素
dict = {}


def load_lexicon_dict():
	with open('../lexicon.txt', 'r') as fp:
		cc = fp.readlines()
		cc = [c.decode('utf-8') for c in cc]
		for c in cc :
			k = c.find(' ')
			k, v= c[0:k], c[k+1:-1] #-1去掉换行
			dict[k] = v
        
def runfenci(fin, fout):
  with open(fout, 'w') as f_out:
    with open(fin, 'r') as f_in:
        cc = f_in.readlines()
        num = len(cc)
        cnt = 0
        for c in cc:
            uc = c.decode('utf-8')
            uc = fenci(uc)
            uc = replace_number(uc)
            c = uc.encode('utf-8')
            f_out.writelines(c)
            cnt = cnt + 1
            if cnt % 10000 == 0:
                print "\r", cnt, "/", num, cnt*1.0/num
            


if __name__ == "__main__":
        
    load_lexicon_dict()

    usage = 'lm-material-fenci.py input-material out-material\n'
    if len(sys.argv) != 3:
        print(usage)
        exit()
    
    runfenci(sys.argv[1], sys.argv[2])
    print "whole=", cnt_whole,  "split=", cnt_split, "split miss=", cnt_miss

    

