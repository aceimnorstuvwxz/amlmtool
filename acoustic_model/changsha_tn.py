#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

在识别出了文字之后，给每句话注音，具体过程与tts_corpus_gen中的tn.py类似
紧接着 tr.py。
tn.py 负责对 句子 
1，分词
2，标记拼音（假）
3，标记音素

会自动将xxx.trn 改成xxx.wav.trn


'''

import sys,re
import jieba

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
        nl = ' '.join(ww)
        
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


def gen(fn, foo):
    with open(fn, 'r') as fp:
        cc = fp.readlines()
        if len(cc) <= 0:
            report_null(fn)
            return
        
        c = cc[0]
        if len(c) <= 0:
            report_null(fn)
            return

        uc = c.decode('utf-8')
        
        #unicode start
        
        uc = remove_unkonwn(uc)
        uc = fenci(uc)
        fuc = mark_phoneme(uc)
        

        #unicode end
        c = uc.encode("utf-8")
        fc = fuc.encode("utf-8") 
        
        with open(foo, 'w') as fo:
            fo.write(c+'\n')
            fo.write(fc+'\n')
            fo.write(fc+'\n')
        

if __name__ == "__main__":
        
    load_lexicon_dict()

    with open('pp.txt','r') as pp:
        files = pp.readlines()
        for ffn in files:
            if len(ffn) > 3:
                print(ffn[:-1])
                gen("/Users/chenbingfeng/tmpp/t-r-n/"+ffn[:-1], "/Users/chenbingfeng/tmpp/n-t-r-n/"+ffn[:-4]+"wav.trn")

    

