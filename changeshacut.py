#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
(C) 2016 unicall
changsha-raw-audio 处理脚本
chenbingfeng



USAGE 
changeshacut   input-wav-name.wav  output-folder

有效的片段会被命名为input-wav-name-0.wav  -1.wav -2.wav，并存储在output-folder之下。
'''


import sys



def changeshacut(wavfn, outfd):
    pass


if __name__ == "__main__":
    
    usage = 'USAGE  changeshacut.py input-wav-name.wav output-folder'
    if len(sys.argv) != 3:
        print usage
        exit()

    changeshacut(sys.argv[1], sys.argv[2])