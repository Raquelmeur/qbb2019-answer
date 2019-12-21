#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np

tuple_pvalue=[]
chr_list=[]
chromosomes={}
position=[]
names=[]
index=[]
archive=""
fam_colors={}

for i in sys.argv[1:]:
    archive=str(i)
    for i,lines in enumerate(open(i)):
        if i==0:
            continue
        if "NA" in lines:
            continue
        fields=lines.rstrip("\n").split()
        if fields[0] not in index:
            index.append(fields[0])
        tuple_pvalue.append((fields[0],-np.log10(float(fields[-1]))))
        #chromosomes[fields[0]]=int(fields[2])
#print(chromosomes)

    # for a in names:
#         if a not in index:
#             index.append(a)
#     print(index)

    colors = ['#42d4f4', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']
    for i in range(len(index)):
       fam_colors[index[i]] = colors[i]

    start_point = 1
       #offset = 0
    fig, ax = plt.subplots()
    for chr in index:
        for point in tuple_pvalue:
            if point[0] == chr:
                ax.scatter(start_point, point[1], color = fam_colors[point[0]], s=2)
                if point [1]>5:
                    ax.scatter(start_point,point[1], color='red',s=2)
                start_point += 1

   # plt.tight_layout()
    ax.set_title("Manhatanplot %s" % archive)
    ax.set_xlabel("Base position")
    ax.set_ylabel('-log10(P-value)')
    plt.tight_layout()
    fig.savefig("MAplot%s.png" %archive)
    plt.close(fig)
    print("SNPs with P-values less than 10^-5 are highlighted in red")
    break

#print(fields)
#print(tuple_pvalue)
    
    