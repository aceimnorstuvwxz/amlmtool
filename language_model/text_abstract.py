#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
能够从大的文本文件里面随机的抽出部分行显示出来，
让你能够看到里面大概都是些什么。
'''


import sys
import logging
import random


def abst(fn, pers):
    with open(fn, 'r') as f:
        while True:
            l = f.readline()
            if len(l) == 0:
                break
            if random.random() < pers:
                print l,  #防止2个\n


if __name__ == "__main__":
    USAGE = "text_abstract.py filename 0.001"
    if len(sys.argv) < 3:
        logging.error(USAGE)
    else:
        abst(sys.argv[1], float(sys.argv[2]))