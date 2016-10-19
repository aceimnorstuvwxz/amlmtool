#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

在识别出了文字之后，给每句话注音，具体过程与tts_corpus_gen中的tn.py类似
紧接着 tr.py。
tn.py 负责对 句子 
0，数字替换  32 -> 三十二
1，分词
2，标记拼音（假）
3，标记音素

会自动将xxx.trn 改成xxx.wav.trn


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


def fenci(l):
        t = replace_fuhao(l)
        ww = jieba.cut(t, cut_all=False)
        ww = [w.strip() for w in ww]
        nww = []
        for w in ww:
            if dict.has_key(w):
                nww.append(w)
            else:
                for iw in w:
                    nww.append(iw)
        nl = ' '.join(nww)
        
        return nl


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
	
def phoneme(w):
	'''给一个词寻找 phoneme'''
	if dict.has_key(w):
		return dict[w].strip()
	r = u''
	for c in w:
		r = r + dict[c] + ' '
	
	return r.strip()

def mark_phoneme(l):
    r = u''
    ww = l.split(u' ')
    for w in ww:
        r = r + phoneme(w) + u' '
    return r.strip()


def report_null(fn):
    print("dead "+fn +"<<>>")
    with open("report.txt", "a") as fr:
        fr.write(fn + "\n")

def remove_unkonwn(l):
    r = u''
    for w in l:
        if dict.has_key(w):
            r = r + w
    return r


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


    # pat_search = SEARCH_PAT.search(l)
    # if pat_search != None:
        # print pat_search.groups()
    print(ret)
    return ret

        

if __name__ == "__main__":
    replace_number(u"我有10块钱，你怎么能够放弃这190万的奖金呢，电话是9934343223，给我200万")

        