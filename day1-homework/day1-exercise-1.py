#!/usr/bin/env python3

import sys

f=open(sys.argv[1])

count=0
for x in f.readlines():
    count+=1
print(count)

