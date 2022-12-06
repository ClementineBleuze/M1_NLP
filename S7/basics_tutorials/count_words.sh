# !/bin/bash
sed 's/ /\n/g' $1 > words.txt
sort words.txt > sorted.txt
uniq -c sorted.txt | sort -n > counts.txt 
tail -n 30 counts.txt
