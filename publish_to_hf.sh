#!/bin/bash
# git clone https://huggingface.co/spaces/Guillaume63/rbc rbc_huggingface
NOW=`date '+%F_%H:%M'`;
cp *.py ../rbc_huggingface
cp requirements.txt ../rbc_huggingface
cd ../rbc_huggingface
git add .
git commit -am"$NOW"
git push
cd ../rbc