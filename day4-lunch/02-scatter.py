#!/usr/bin/env python3

"""Usage: ./00-scatter.py <ctab>

Compare num_exons vs length
"""

import sys
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

fpkms1={}
fpkms2={}
data=(open(sys.argv[1]))
data2=(open(sys.argv[2]))
both_data=[]

name1=sys.argv[1].split(os.sep)[-2]
ctab1=pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")
name2=sys.argv[2].split(os.sep)[-2]     #extracts the name in the column to name it (so -2 is SRR072893)
ctab2=pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")


fpkm={name1:ctab1.loc[:, "FPKM"],
      name2:ctab2.loc[:,"FPKM"]}
#print(fpkm)
df=pd.DataFrame(fpkm)

#print(df)

g_ctab1 = df.loc[:,"SRR072893"]
g_ctab2 = df.loc[:,"SRR072894"]
#print(g_ctab1)
#print(g_ctab2)
x = np.log2(g_ctab1 +1)
y = np.log2(g_ctab2 +1)
#


#
fig, ax = plt.subplots()
ax.scatter(x=x, y=y, s=5, alpha=0.2)


plt.title("SRR072893 vs SRR072894")
coeff= np.polyfit(x, y, 1)      #1 is to make it linear
xl= np.linspace(0, 10, 10)
yl= coeff[0]*xl + coeff[1]
ax.plot(xl,yl, color="red",label="fit curve") 
ax.legend()
plt.xlabel("g_ctab1 SRR072893 FPKM")
plt.ylabel("g_ctab2 SRR072894 FPKM")
fig.savefig("SRR072893 vs SRR072894")
plt.close(fig)

print(coeff)
print(type(coeff))




