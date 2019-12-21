#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA       #TO IMPORT PCA

df=pd.read_csv(sys.argv[1],index_col="t_name")
df=df.drop(columns="gene_name")
col_names=df.columns.values.tolist()
#print(df.shape)
n,p=df.shape    #to store the shape of my dataframe

fit=PCA().fit_transform(df.T)     #T= we need to transpose our dateframe otherwise it will cluster our genes
print(fit[:,0])     #allows us to see the first principal component, to see the second one we just replace the 0 with a 1

quit()
sexes=[]
stages=[]
for name in col_names:
    sex,stage=name.split("_")
    if sex=="female":
        sexes.append("red")
    else:
        sexes.append("blue")
                #WHEN WE DO THAT WE SEE THAT THERE IS NO CLEAR CORRELATION BASED ON SEX
    if "10"in stage:
        stages.append("lightsalmon")
    elif "11" in stage:
        stages.append("tomato")
    elif "12" in stage:
        stages.append("r")
    elif "13" in stage:
        stages.append("brown")
    elif "14" in stage:
        stages.append("black")

# # fig,ax=plt.subplots()
# # ax.bar(range(p),fit.explained_variance_ratio_)
# # #print(fit.explained_variance_ratio_)
# # fig.savefig("scree.png")
# # plt.close(fig)
# # #We see that the first principal component is the one that explaines better our data
fig,ax=plt.subplots()
ax.scatter(fit[:,0],fit[:,1],c=stages)
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
fig.savefig("pca.png")
plt.close()