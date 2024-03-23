#!/bin/bash

for FPN in `find $1/ -type f -not -wholename $1/recup_dir.*/report.xml`
do

EXT=`echo -n "$FPN" | awk -F'[.]' '{print $NF}'`

if [ "$FPN" = "$EXT" ]; then
FNM=`echo -n "$FPN" | rev | cut -d '/' -f1 | rev`
else
SUM=`md5sum -z "$FPN" | cut -d " " -f1 | head -c -1`
FNM=`echo -n "$SUM.$EXT"`
fi

FL=${SUM:0:2}
SL=${SUM:3:5}

mkdir -p "$2/$FL/$SL"
mv "$FPN" "$2/$FL/$SL/$FNM"

done

if [ ! -z "$1" ]; then
rm -rf $1/recup_dir.*
fi

#END
