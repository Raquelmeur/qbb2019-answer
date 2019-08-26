#!/usr/bin/env python3

import sys

f=open(sys.argv[1])

count=0
for i in f:
    fields=i.split("\t")
    if "NM:i:0" in fields:
        count+=1
print(count)
    