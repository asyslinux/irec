#!/bin/bash

for FPN in `find $1/ -type f -not -wholename "$1/recup_dir.*/report.xml"`
do

DNM=`dirname "$FPN"`
EXT=`echo -n "$FPN" | awk '{gsub(/.*[/]|[.]{1}[^.]+$/, "", $0)} 1' | awk -F'[.]' '{print $NF}'`
FBS="$DNM/$EXT"

SUM=`md5sum -z "$FPN" | cut -d " " -f1 | head -c -1`

if [ "$FPN" = "$FBS" ]; then
FNM=`echo -n "$FPN" | rev | cut -d '/' -f1 | rev`
else
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
