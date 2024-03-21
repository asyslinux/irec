#!/bin/bash

for X in `ls -1 $1/`
do

SUM=`md5sum -z $1/$X | cut -d " " -f1 | head -c -1`
FNM=`echo -n $SUM | awk '{print $1".jpg"}'`

FL=${SUM:0:2}
SL=${SUM:3:5}

mkdir -p $2/$FL/$SL
mv $1/$X $2/$FL/$SL/$FNM

done

#END