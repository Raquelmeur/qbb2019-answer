#!/usr/bin/env python3

"""
Usage: ./00-scatter.py <ctab>
compare num exon vs length
"""
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#file /Users/cmdb/qbb2019-answers/results/results/stringtie/SRR072893/t_data.ctab

sample=sys.argv[1]
#
df=pd.read_csv(sample)

r=df.loc[:,"SRR072893"]
g=df.loc[:,"SRR072894"]

r+=1
g+=1
m=np.log2(r/g)
a=np.log2(r*g)*(0.5)

print(m)
print(a)
#

print(r)
print(g)
fig, ax = plt.subplots()
ax.scatter(x=a, y=m, alpha=0.2)
ax.plot(color="red") #we are passing a list of x coordinates and y coordinates
fig.suptitle("m and n")
ax.set_xlabel("a")
ax.set_ylabel("y")
fig.savefig("scatter plot")
plt.close(fig)
#
# gene_1=[]
# gene_2=[]
# m= [] #log ratio of the FPKMs
# a= [] # average of the FPKMs
# for i, line in enumerate(pd.read_cvs(sys.argv[1])):
#    if i == 0:
#        continue
#    fields= line.rstrip("\n").split()
#    gene_1.append(int(fields[3]))
#    gene_2.append(int(fields[3]))
#
# print(gene_1)
# print(gene_2)
# quit()
# fig, ax= plt.subplots()
# ax.scatter(x=m, y=a)
# fig.savefig("MA_plot.png")
# plt.close(fig)
#
#
# #!/usr/bin/env python3
#
# """Usage: ./00-scatter.py <ctab>
#
# Compare num_exons vs length
# """
#
# import sys
# import matplotlib.pyplot as plt
# import os
# import pandas as pd
# import numpy as np
#
# fpkms1={}
# fpkms2={}
# data=(open(sys.argv[1]))
# data2=(open(sys.argv[2]))
# both_data=[]
#
# name1=sys.argv[1].split(os.sep)[-2]
# ctab1=pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")
# name2=sys.argv[2].split(os.sep)[-2]     #extracts the name in the column to name it (so -2 is SRR072893)
# ctab2=pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")
#
#
# fpkm={name1:ctab1.loc[:, "FPKM"],
#       name2:ctab2.loc[:,"FPKM"]}
#
#
# print(fpkm)
# quit()
# df=pd.DataFrame(fpkm)
#
# #print(df)
#
# g_ctab1 = df.loc[:,"SRR072893"]
# g_ctab2 = df.loc[:,"SRR072894"]
# #print(g_ctab1)
# #print(g_ctab2)
# x = np.log2(g_ctab1 +1)
# y = np.log2(g_ctab2 +1)
# #
