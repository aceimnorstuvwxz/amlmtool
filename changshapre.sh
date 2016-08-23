#xmlypre folder Char outfolder

xnt=0
mkdir $3
for p in $1/*.mp3; do

mv "$p" "$3/$2$xnt.wav"
xnt=$[ xnt + 1 ]

done
