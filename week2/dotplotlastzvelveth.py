#!/usr/bin/env python3

"""
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

lastz=open(sys.argv[1])
list_start_target=[]
list_end_target=[]
list_count_query=[]
list_end_query=[]
dic={}
for i,line in enumerate(lastz):
    if i==0:
        continue
    fields=line.rstrip("n").split()
    if fields[0]==str(0):
        if fields[6]=="+":
            dic[int(fields[3])]=[fields[3],fields[4],int(fields[4])-int(fields[3])]
            
#print(dic)
#quit()
for key in sorted(dic):
    #print(dic[key])
    list_start_target.append(dic[key][0])
    list_end_target.append(dic[key][1])
    list_count_query.append(dic[key][2])
# print(list_start_target)
# print(list_end_target)
# print(list_count_query)
# list_start_target.sort()
count=0
fig,ax=plt.subplots()
for i in range(len(list_start_target)):
    plt.plot([count,count+list_count_query[i]],[list_start_target[i],list_end_target[i]],'r-')
    count+=int(list_count_query[i])
ax.set_title("Genome Assembly")
plt.xlabel('Assembled Contigs')
plt.ylabel('Reference Genome')
ax.yaxis.set_major_locator(plt.MaxNLocator(8))  #Separate y axis in 8 values
plt.tight_layout()
fig.savefig("velvethplot.png")
plt.close(fig)

plt.plot()


