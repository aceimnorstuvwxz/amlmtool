#xmlypre folder Char outfolder
for p in $1/*.mp3; do

nn=$(uuidgen)

mv "$p" "$1/$nn.m4a"

done

xnt=0
mkdir $3
for p in $1/*.m4a; do

avconv -i "$p" "$3/$2$xnt.wav"
xnt=$[ xnt + 1 ]

done
