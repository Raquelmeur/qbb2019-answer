#!/usr/bin/env python3

import sys

f=open(sys.argv[1])

num=0
count=0
for i in f:
    fields=i.split("\t")
    count+=1
    num+=int(fields[4])
ave=num/count
        
print (ave)