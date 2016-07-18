


for f in $1/*.mp3; do 


mpg321 -w   "$f.wav"   "$f"


done

