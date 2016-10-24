#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
姓 称谓 组合

张总
张科长
张医生
陈经理
...
'''


import sys
import logging
import random

def load_firstnames():
    ret = []
    with open('中文姓氏排名.txt', 'r') as f:
        ll = f.readlines()
        for l in ll:
            l = l.decode('utf-8')
            l = l[:-1] #去掉换行
            ww = l.split('\t')
            for w in ww:
                ret.append(w)
                print w.encode('utf-8')

    return ret

def load_titles():
    ret = []
    with open('中文称呼大全.txt', 'r') as f:
        ll = f.readlines()
        for l in ll:
            l = l.decode('utf-8')
            l = l[:-1]
            l = l.strip()
            if len(l) > 0:
                ret.append(l)
                print l.encode("utf-8")
    return ret



if __name__ == "__main__":
    firstnames = load_firstnames()
    titles = load_titles()
    ret = []
    for fn in firstnames:
        for ti in titles:
            seg = fn + ti
            ret.append(seg)
            print seg.encode("utf-8")
    
    with open('firstname_title_combined.txt', 'w') as f:
        f.write(('\n'.join(ret)).encode('utf-8'))

