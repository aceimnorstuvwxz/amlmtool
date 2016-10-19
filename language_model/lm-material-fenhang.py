#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
2,把句号逗号分割符号，如果前置长度超过第一大小后，把符号位置开新行。适应正常的说话停顿。
天苍苍，野茫茫，风吹草低见牛羊。
>>>
天 苍苍 野 茫 茫 风 吹 草 低 见 牛 羊 （不是很好）
>>>
天 苍苍 野 茫 茫 
风 吹 草 低 见 牛 羊

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

FENHANG_THRESHOLD = 7
def fenhang(l):
    #print l
    remain = l
    ret = []
    l = l + ' '
    start = 0
    now = 0
    isin = False
    cnt = 0
    while now < len(l):
        if l[now] == ' ' and isin == True and cnt >= FENHANG_THRESHOLD:
            ret.append(l[start:now] + '\n')
            isin = False
            cnt = 0
        elif l[now] != ' ' and isin == False:
            isin = True
            start = now
        
        cnt = cnt + 1
        now = now + 1
    # print ret
    return ret




#音素
dict = {}


def load_lexicon_dict():
	with open('lexicon.txt', 'r') as fp:
		cc = fp.readlines()
		cc = [c.decode('utf-8') for c in cc]
		for c in cc :
			k = c.find(' ')
			k, v= c[0:k], c[k+1:-1] #-1去掉换行
			dict[k] = v
        
def runfenhang(fin, fout):
    with open(fin, 'r') as f_in:
        cc = f_in.readlines()
        num = len(cc)
        ret = []
        cnt = 0
        for c in cc:
            uc = c.decode('utf-8')
            uc = replace_number(uc)
            uc = replace_fuhao(uc)
            ucs = fenhang(uc)
            for euc in ucs:
                c = euc.encode('utf-8')
                ret.append(c)
            cnt = cnt + 1
            print "", cnt, "/", num
            

        with open(fout, 'w') as f_out:
            f_out.writelines(ret)

if __name__ == "__main__":
        
    load_lexicon_dict()

    usage = 'lm-material-fenghang.py input-material out-material THRESH_HOLD\n'
    if len(sys.argv) != 4:
        print(usage)
        exit()
        
    global FENHANG_THRESHOLD
    FENHANG_THRESHOLD = int(sys.argv[3])
    runfenhang(sys.argv[1], sys.argv[2])
    print "whole=", cnt_whole,  "split=", cnt_split, "split miss=", cnt_miss

    

