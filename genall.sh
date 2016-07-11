cnt=0
cat "dir-0.txt" | while read line
do 
    echo $line
    echo $cnt
    cnt=$[cnt + 1]
    ./changeshacut.py "$line" "/Volumes/Seagate Backup Plus Drive 1/changshacuto"

done
