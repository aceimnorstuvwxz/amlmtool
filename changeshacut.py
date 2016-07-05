#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
(C) 2016 unicall
changsha-raw-audio 处理脚本
chenbingfeng



USAGE 
changeshacut   input-wav-name.wav  output-folder

有效的片段会被命名为input-wav-name-0.wav  -1.wav -2.wav，并存储在output-folder之下。



1，小于20秒的，踢除掉。
2，从9秒开始，去掉末尾的1秒。
3，超过0.5秒的低能量段表示断点。
4，断点之间的作为话语段，去掉首末两个段。
5，超过3秒的作为有效段落。



可能出现的问题：
由于不同录音批次的音频音量范围不同，如果不进行归一化，同时在silence-split时使用固定的magic-number，会导致不能适应音量及噪声。
解决办法：归一化

'''


import sys
from pydub import AudioSegment
from pydub.silence import split_on_silence


LENGTH_MIN = 20.0
CUT_START = 9000
CUT_TAIL = 1000
EFFECT_MIN = 3000


def changeshacut(wavfn, outfd):
    cnt = 0
    sound = AudioSegment.from_wav(wavfn)
    print len(sound)
    length =  len(sound)/1000.0 #length in second
    print "length=",length
    if length < LENGTH_MIN:
        print "too short, drop"
        return
    
    sound = sound[CUT_START:-CUT_TAIL]
    print len(sound)


    chunks = split_on_silence(sound, min_silence_len=300, silence_thresh=-33)#silence time:700ms and silence_dBFS<-70dBFS

    print "chunks num =", len(chunks)
    if len(chunks) <= 2:
        print "no un-head-tail chunk, drop"
        return
    
    chunks = chunks[1:-1]

    for ck in chunks:
        if len(ck) < EFFECT_MIN:
            print "too short chunk"
        else:
            nfn = outfd +"/" + (wavfn.split('/')[-1][:-4]) + ('-%d.wav'%cnt)
            cnt = cnt + 1
            nck = ck.set_frame_rate(16000)
            nck.export(nfn, format="wav")
            print "effect chunk name= %s length= %d" % (nfn, len(ck))


if __name__ == "__main__":
    
    usage = 'USAGE  changeshacut.py input-wav-name.wav output-folder'
    if len(sys.argv) != 3:
        print usage
        exit()

    changeshacut(sys.argv[1], sys.argv[2])