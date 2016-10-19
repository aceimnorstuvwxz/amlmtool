#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
把多个成品语料按权重聚合在一起
lm-material-combine.py  outputfile.txt file1.txt 权重1 fine2.txt 权重2  ...... 
权重是整数

'''

import sys,re
import jieba
import num2chinese

reload(sys)
sys.setdefaultencoding("utf-8")
            
def runcombine(outfn, couples):
    with open(outfn, 'w') as f_out:
        for cp in couples:
            with open(cp[0], 'r') as f_in:
                lines = f_in.readlines()
                for i in range(cp[1]):
                    f_out.writelines(lines)
    

if __name__ == "__main__":

    usage = ''' lm-material-combine.py  outputfile.txt file1.txt 权重1 fine2.txt 权重2  ......\n''' 

    if len(sys.argv) % 2 != 0:
        print(usage)
        exit()
        
    outfn = sys.argv[1]
    couples = []
    for i in range(1, len(sys.argv)/2):
        tp = (sys.argv[i*2], int(sys.argv[i*2 + 1]))
        couples.append(tp)

    print outfn, couples
    runcombine(outfn, couples)
    print 'done' 

    

