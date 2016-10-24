#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
从12306密码.txt里面抽取姓名
'''


import sys
import logging
import random



if __name__ == "__main__":
    ret = []
    with open('12306密码.txt', 'r') as f:
        lines = f.readlines()
        for l in lines:
            ww = l.split('----')
            if len(ww) > 2:
                ret.append(ww[2])
                print ww[2]
    
    with open('12306names.txt', 'w') as f:
        f.write(' '.join(ret))
