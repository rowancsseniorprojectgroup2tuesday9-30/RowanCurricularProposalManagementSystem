#!/bin/bash
# The mighty archiver

TIMESTAMP=$(date +%Y%m%d%H%M%S)
EMPLOYEE=""

# Specify document type
# -s : cover [s]heet
# -l : [l]ibrary form
# -t : [t]emplate
# -p : [p]rogram guide
# -c : [c]onsult letter
# -n : uploader last [n]ame

while getopts ":n:f:sltpc" opt
do
    case "${opt}" in
        n) EMPLOYEE=${OPTARG};;
        f) FILE=${OPTARG};;
        s) DOCTYPE="Cover_Sheet";;
        l) DOCTYPE="Lib_Form";;
        t) DOCTYPE="Template";;
        p) DOCTYPE="Pgrm_Guide";;
        c) DOCTYPE="Consult_Letter";;
    esac
done
shift $((OPTIND -1))

NEWFILE=$EMPLOYEE\_$DOCTYPE\_$TIMESTAMP.pdf

mv $FILE $NEWFILE
echo $NEWFILE

exit 0
