#!/usr/bin/env python3

"""Usage: ./01-scatter.py <ctab>

Plot FPKM
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

fpkms=[]

for i, line in enumerate(open(sys.argv[1])):
    if i==0:
        continue
    fields=line.rstrip("\n").split("\t")
    if float(fields[11])>0:
        fpkms.append(float(fields[11]))

print(len(fpkms))
my_data=np.log2(fpkms)

mu=float(sys.argv[2]) #6
sigma=float(sys.argv[3]) #3
a=float(sys.argv[4]) #3

x=np.linspace(-15, 15, 100)
y=stats.skewnorm.pdf(x, a, mu, sigma)
#print(y)
#print(type(y))

fig,ax=plt.subplots()       #fig is the entire image -  ax is the pannel  (so like how many paneles que indican x e y)

ax.hist(my_data, bins=100, density=True, label="frequency SRR072893")
ax.plot(x,y, label="skeynorm pdf")
ax.legend()
plt.xlabel("log2 FPKM ")
plt.ylabel("frequency")
plt.title("FPKM vs frequency in SRR072893")
plt.text(-15,0.15,"mu=%0.1f  sigma=%0.1f    a=%0.1f" %(mu,sigma,a))
fig.savefig("fpkms.png")
plt.close(fig)

#mu= average
#sigma=standard deviation
