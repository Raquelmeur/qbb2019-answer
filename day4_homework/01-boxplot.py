#!/usr/bin/env python

"""
Usage 01-boxplot.py <gene_name> <FPKMs.csv>

Boxplot all transcripts for a given gene
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

gene_name=sys.argv[1]
fpkm_file=sys.argv[2]

df=pd.read_csv(fpkm_file, index_col="t_name")       #it is just open the fpkm_file and setting as the index_column THAT MEANS THAT THAT ARE SET AS ROW NAMES!!!!!!!!!!!!!!!! when we see the information on rows and columns we DO NOT COUNT THAT COLUMN
#print(df)

goi=df.loc[:,"gene_name"]==gene_name            #with Sxl we got 25 trues and 34000 falses
fpkms=df.drop(columns="gene_name")      # it is just dropping the column that is names gene_name
col_names=fpkms.columns

# col_female=[]
# col_male=[]
# for i in col_names:
#     if "female" in i:
#         col_female.append(i)
#     else:
#         col_male.append(i)
# print (col_female)
# print(col_male)

col_names2=[]
col_names3=[]
for i in col_names:
    if "female" in i:
        col_names2.append(True)
    else:
        col_names2.append(False)

for i in col_names2:
    if i==True:
        col_names3.append(False)
    else:
        col_names3.append(True)

#print(col_names3)

# print(col_names)
# print(col_names2)
# quit()
#you cano
#soi=df.goi["female",:]==female
#print(fpkms.loc[goi,:])
#print(fpkms.loc[:,"t_name"])
fig, (ax1,ax2)=plt.subplots(nrows=2)
fig.subplots_adjust(hspace=0.6)
fig.suptitle("Sxl Female Male")
ax1.boxplot(fpkms.loc[goi,col_names2].T)
ax2.boxplot(fpkms.loc[goi,col_names3].T)
ax1.set_xticklabels(["10", "11", "12", "13", "14A", "14B", "14C", "14D"])
ax2.set_xticklabels(["10", "11", "12", "13", "14A", "14B", "14C", "14D"])
ax1.set_title("female")
ax2.set_title("male")
ax1.set_ylabel("FPKMs")
ax1.set_xlabel("Stages of Development")
ax2.set_xlabel("Stages of Development")
ax2.set_ylabel("FPKMs")

      #T =That allows us to flip it and put the number of sample in the x axis, the x.boxplot(fpkms.loc[goi,:] part says that you are gonna plot just the rows that are TRUE


fig.savefig("boxplot.png")
plt.close(fig)


#
#
