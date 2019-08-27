#!/usr/bin/env python3

import sys

f=open(sys.argv[1])
count=0
for i in f:
    fields=i.split("\t")
    if fields[2]=="2L":
        read=int(fields[3])
        if read>10000 and read<20000:
            count+=1
print(count)