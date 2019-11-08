#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


df=pd.read_csv(sys.argv[1], sep="\t", header=0, index_col=0)
array=np.array(df)
#print(array)
array2=np.delete(array,[2,3,4,5],1)
#print(array2)

Kmean=KMeans(n_clusters=5)

Kmean.fit(array2)
Kmean.cluster_centers_
Kmean.labels_
fig,ax=plt.subplots(sharey=True)
plt.xlabel("CFU")
plt.ylabel("poly")
ax.set_title("Kmean")
plt.scatter(array2[:,0], array2[:,1], alpha=0.5,c=Kmean.labels_.astype(float))
fig.savefig("Kmeanscatter")

plt.show()