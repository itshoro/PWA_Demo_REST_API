#!/bin/bash
FILES=(imgs/*)
count=0
len=${#FILES[@]}
for ((i=0; i<$len; i++));
do

filename=`basename ${FILES[i]} .jpg`
data="data:image/jpeg;base64,$(base64 ${FILES[i]} -w 0)"

curl -X PUT -H "Content-Type: application/json; charset=utf-8" -d @- 127.0.0.1:5000/api/$i --trace-ascii trace.out << EOT
{
"name": "$filename",
"data": "$data"
}
EOT

done
