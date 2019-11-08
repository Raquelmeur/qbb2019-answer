#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
import numpy as np
import seaborn as sns
import scipy.cluster.hierarchy as hac

df=pd.read_csv(sys.argv[1], sep="\t", header=0, index_col=0)
#print(df)
array=np.array(df)
#print(array)
dt=hac.linkage(df,'average')
#print(dt)
sortedarray=hac.leaves_list(dt)
#print(sortedarray)
new_list=[]
for i in sortedarray:
    new_list.append(array[i])
newarray=np.asarray(new_list)
#print(newarray)

# sns.heatmap(newarray)
# plt.show()

cell_type=np.transpose(newarray)
dcell=hac.linkage(cell_type,'average')
sortedarraycell=hac.leaves_list(dcell)
new_list_cell=[]
for a in sortedarraycell:
    new_list_cell.append(cell_type[a])
newarray_cell_type=np.asarray(new_list_cell)
cell_type_transposeback=np.transpose(newarray_cell_type)


names=["CFU","poly","unk","int","mys","mid"]
columns=df.columns
celltypecolumn=[]
# for m in sortedarray:
#     genescolumn.append(columns[m])
for n in sortedarraycell:
    celltypecolumn.append(columns[n])


# fig,ax=plt.subplots(sharey=True)
# hac.dendrogram(dcell,ax=ax)
# plt.xlabel("Cell type")
# plt.ylabel("Differentiation")
# ax.set_xticklabels([names[1],names[2],names[0],names[4],names[3],names[5]])
# plt.tight_layout()
# fig.savefig("dendrogram")
#
# plt.show()
# quit()
#print(sortedarray)
fig,(ax1,ax2,ax3)=plt.subplots(ncols=3)
sns.heatmap(array, ax=ax1)
sns.heatmap(newarray, ax=ax2)
sns.heatmap(cell_type_transposeback,ax=ax3)

ax1.set_xlabel("cell type")
ax2.set_xlabel("cell type")
ax3.set_xlabel("cell type")
ax1.set_xticklabels(columns)
ax1.set_ylabel("Genes")
ax2.set_ylabel("Genes")
ax3.set_ylabel("Genes")
ax2.set_xticklabels(columns)
ax1.set_title("Nonsorted")
ax2.set_title("Genes sorted")
ax3.set_title("Genes & Cell type sorted")
ax3.set_xticklabels(celltypecolumn)

plt.tight_layout()

fig.savefig("heatplots")
plt.show()

# quit()
# plt.pcolor(df)
# plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
# plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
# plt.show()