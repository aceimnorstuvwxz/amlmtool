mkdir $2
for p in $1/*.wav; do

./xcut_pure.py "$p" $2

done
