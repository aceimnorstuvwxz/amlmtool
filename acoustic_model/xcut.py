#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
(C) 2016 unicall
有声音频切分脚本

USAGE 
xcut   input-wav-name.wav  output-folder

有效的片段会被命名为input-wav-name-0.wav  -1.wav -2.wav，并存储在output-folder之下。


可以啊，比changsha清晰多了，而且普通话多的标准，缺点是每个节目的speaker都是同一个，
因而需要多下载不同的节目，获得更多的speaker，同时注意，节目最好无BGM，同时speaker的情感音调变化不夸张的。
这样产生的corpus，其质量将非常好。
音频长度尽量较短，咬字要清晰，语速较慢。

1，单片超过2秒，少于5.6秒。
2，前后加入silence部分。
3，超过x秒的silence表示断点。
4，去掉开头20秒，去掉结尾20秒。
5，去掉首位单片。

wav文件的采样率、声道数量都可能不同。
8000,16000,24000
1/2

'''


import sys
from pydub import AudioSegment
from pydub.silence import split_on_silence


LENGTH_MIN = 20.0
CUT_START = 60000
CUT_TAIL = 20000
EFFECT_MIN = 2500
EFFECT_MAX = 5600


def xcut(wavfn, outfd):
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


    chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=-36, keep_silence=400)#silence time:700ms and silence_dBFS<-70dBFS

    print "chunks num =", len(chunks)
    if len(chunks) <= 2:
        print "no un-head-tail chunk, drop"
        return
    
    chunks = chunks[1:-1]

    for ck in chunks:
            nfn = outfd + "/" + (wavfn.split('/')[-1][:-4]) + ('_%d.wav'%cnt)
            nck = ck.set_frame_rate(16000)
            nck = nck.set_channels(1)
            if len(nck) < EFFECT_MIN:
                pass
            elif len(nck) > EFFECT_MAX:
                pass
            else:
                nck.export(nfn, format="wav")
                cnt = cnt + 1
                print "chunk name= %s length= %d" % (nfn, len(nck))


if __name__ == "__main__":
    
    usage = 'USAGE  xcut.py input-wav-name.wav output-folder'
    if len(sys.argv) != 3:
        print usage
        exit()

    xcut(sys.argv[1], sys.argv[2])