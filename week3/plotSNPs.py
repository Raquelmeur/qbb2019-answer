#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt

data=open(sys.argv[1])
dp=[]
dp_values=[]
list_info=[]
dic={}
list_qual=[]
list_af=[]
ann_dic={}
for i,line in enumerate(data):
    if line.startswith("#"):
        continue
    fields=line.rstrip("\n").split()
    list_info.append(fields[7].split(";"))
    list_qual.append(int(float(fields[5])))
    r_info=fields[7]
    r_info_split=r_info.split(";")[3]
    list_af.append(r_info_split.split("=")[1])
    sumary_split=r_info.split(";")[41]
    sumary_value=sumary_split.split("=")[1]
    sumary_score=sumary_value.split("|")[1]
    if sumary_score in ann_dic:
        ann_dic[sumary_score]+=1
    else:
        ann_dic[sumary_score]=1

#print(list_af)
#print(sumary_score)
#print(list_info)
#print(list_qual)
#quit()
for i in list_info:
    for a in i:
        if "DP=" in a:
            dp.append(a.split("="))
#print(dp)

for b in dp:
    dp_values.append(b[1])


#print(dp_values)
#FIG1
# fig,ax=plt.subplots()
# ax.hist(dp_values,bins=100)
# fig.savefig("Figure1")
# plt.close(fig)

#FIG2
# fig,ax=plt.subplots()
# ax.hist(list_qual,bins=1000,range=[0,5000])
# fig.savefig("Figure2")
# plt.close(fig)

#FIG3
# fig,ax=plt.subplots()
# ax.hist(list_af,bins=100)
# fig.savefig("Figure3")
# plt.close(fig)

#FIG4
fig,ax=plt.subplots(4)
fig.subplots_adjust(hspace=1)
ax[0].hist(dp_values,bins=100)
ax[1].hist(list_qual,bins=1000,range=[0,5000])
ax[2].hist(list_af,bins=100)
plt.bar(range(len(ann_dic)), list(ann_dic.values()), align = 'center')
plt.xticks(range(len(ann_dic)), list(ann_dic.keys()),rotation="vertical",size=5)
ax[0].set_xlabel("Variants")
ax[0].set_ylabel("Read Depth")

ax[1].set_xlabel("Variants")
ax[1].set_ylabel("Quality")

ax[2].set_xlabel("Variants")
ax[2].set_ylabel("Frequency")

ax[3].set_xlabel("Variants")
ax[3].set_ylabel("Impact")

ax[0].set_title("Graph1-Read Depth Distribution")
ax[1].set_title("Graph2-Genotype Quality Distribution")
ax[2].set_title("Graph3-Allele Frequency spectrum")
ax[3].set_title("Graph4-Predicted effect")
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
ax.yaxis.set_major_locator(plt.MaxNLocator(8))
fig.savefig( "results.png" )
plt.close(fig)
plt.show()


