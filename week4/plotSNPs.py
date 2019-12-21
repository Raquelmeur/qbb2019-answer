#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt

#data=open(sys.argv[1])
databam=open(sys.argv[1])
dataplink=open(sys.argv[2])
alleleparse=[]
allelefrequence=[]
xaxis=[]
yaxis=[]
names=[]
index=[]
tuple_pca=[]
for i,line in enumerate(databam):
    if line.startswith("#"):
        continue
    fields1=line.rstrip("\n").split()
    if ',' not in fields1[7]:
        alleleparse.append(float(fields1[7].split("=")[1]))
    elif ',' in fields1[7]:
        something=fields1[7].split('=')[1]
        alleleparse.append(float(something.split(',')[0]))
    #allelefrequence.append(alleleparse[1])
#print(alleleparse)

for i,line in enumerate(dataplink):
    fields2=line.rstrip("\n").split()
    names.append(fields2[0])
    xaxis.append(float(fields2[2]))
    yaxis.append(float(fields2[3]))
    tuple_pca.append((fields2[0], float(fields2[2]),float(fields2[3])))
    
print(tuple_pca)
#quit()
#print(names)
fam_colors={}
for a in names:
    if a not in index:
        index.append(a)

colors = ['#800000', '#9A6324', '#e6194B', '#808000', '#ffe119', '#469990', '#000075', '#000000', '#f032e6', '#aaffc3', '#a9a9a9']
for i in range(len(index)):
   fam_colors[index[i]] = colors[i]
print(index)
#print(xaxis)

#quit()

#FIG1
fig,ax=plt.subplots()
ax.hist(alleleparse,bins=5000, color="red")
ax.set_xlabel("SNPs")
ax.set_ylabel("Allele Frequency")
ax.set_title("Allele Frequency across SNPs")
fig.savefig("Allele Frequency across SNPs")
plt.close(fig)

fig,ax=plt.subplots()
for point in tuple_pca:
    ax.scatter(point[1],point[2],color=fam_colors[point[0]],s=3)
ax.set_xlabel("First component")
ax.set_ylabel("Second component")
ax.set_title("Genetic variant")
plt.tight_layout()
fig.savefig("PCA")
plt.close(fig)
