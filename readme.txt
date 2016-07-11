

+++++++++++Q++++++++++
代号：Q
来自长沙的对话数据，需要从中提取ASR的corpus。
changsha-asr-raw 27W+对话  


1，小于20秒的，踢除掉。
2，从9秒开始，去掉末尾的1秒。
3，超过0.5秒的低能量段表示断点。
4，断点之间的作为话语段，去掉首末两个段。
5，超过3秒的作为有效段落。

changsha_q

+++++++++++X+++++++++++
代号：X
各种有声圣经：
http://www.jdtjy.org/html/shengjingyuandi/jingshuxiazai/zwyssj(MP3).rar
ftp://ftp.fhl.net/pub/FHL/audio

有声小说（踢出带背景音的）
http://www.tingchina.com/yousheng/25560/play_25560_34.htm
http://www.ximalaya.com/36095869/album/3144025

可以啊，比changsha清晰多了，而且普通话多的标准，缺点是每个节目的speaker都是同一个，
因而需要多下载不同的节目，获得更多的speaker，同时注意，节目最好无BGM，同时speaker的情感音调变化不夸张的。
这样产生的corpus，其质量将非常好。
音频长度尽量较短，咬字要清晰，语速较慢。

1，单片超过2秒，少于5.6秒。
2，前后加入silence部分。
3，超过x秒的silence表示断点。
4，去掉开头20秒，去掉结尾20秒。
5，去掉首位单片。


dgkae.cbf#gmail.com
