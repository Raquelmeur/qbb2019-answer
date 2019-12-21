#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np



featER4=open(sys.argv[1])
featGIE=open(sys.argv[2])
diffER4=open(sys.argv[3])
diffGIE=open(sys.argv[4])

promoterER4=0
intronER4=0
exonER4=0
promoterGIE=0
intronGIE=0
exonGIE=0
listER4=[]
listGIE=[]
for i in featER4:
    if "promoter" in i:
        promoterER4+=1
    if "intron" in i:
        intronER4+=1
    if "exon" in i:
        exonER4+=1
listER4.append(promoterER4)
listER4.append(intronER4)
listER4.append(exonER4)
print(listER4)
for i in featGIE:
    if "promoter" in i:
        promoterGIE+=1
    if "intron" in i:
        intronGIE+=1
    if "exon" in i:
        exonGIE+=1
listGIE.append(promoterGIE)
listGIE.append(intronGIE)
listGIE.append(exonGIE)
print(listGIE)


count1ER4=0
for m in diffER4:
    count1ER4+=1
count2GIE=0
for n in diffGIE:
    count2GIE+=1
#print(count1,count2)


#quit()
x1=["loss","gain"]

fig,(ax1, ax2)=plt.subplots(ncols=2)
ax1.bar(x1[0],count1ER4)
ax1.bar(x1[1],count2GIE)
ax1.set_ylabel("number of sites")
ax1.set_title("CTCF binding after differentiation")

width=0.35
x2=["promoter","intron","exon"]
x=np.arange(len(x2))
ax2.bar(x-width/2,listER4,width, label="ER4")
ax2.bar(x+width/2,listGIE,width, label="GIE")
ax2.set_ylabel("number of sites")
ax2.set_xticks(x)
ax2.set_xticklabels(x2)
ax2.set_title("Region of CTCF binding")
ax2.legend()
fig.tight_layout()


 
fig.savefig("Plot.png")
plt.close(fig)
    
