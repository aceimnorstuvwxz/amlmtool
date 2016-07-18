
# clear-report.sh wav-folder

for p in $1/*.wav; do

if [ ! -f "$p.trn" ]; then 
    echo "$p"
    rm "$p"
fi 

done