#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy


df=pd.read_csv(sys.argv[1], index_col="t_name",sep="\t") 
fpkm=pd.DataFrame(df["FPKM"])
#print(fpkm)
#quit()
#goi=pd.DataFrame(df.loc[sys.argv[2]].iloc[1:])      #you get a dataframe of the values just for your gene of interest   iloc is subsetting by possition, so removing the first columns that is just gene_name

H3K4me1=pd.read_csv(sys.argv[2], sep="\t",header=None,index_col=0)
H3K4me1_mean=pd.DataFrame(H3K4me1.iloc[:,4])
#print(H3K4me1)
# quit()
H3K4me3=pd.read_csv(sys.argv[3],sep="\t",index_col=0,header=None)
H3K4me3_mean=pd.DataFrame(H3K4me3.iloc[:,4])
H3K9me3=pd.read_csv(sys.argv[4],sep="\t",index_col=0,header=None)
H3K9me3_mean=pd.DataFrame(H3K9me3.iloc[:,4])

#print(goi.columns)
#goi["FPKM"]=pd.to_numeric(goi["FPKM"])      #transform the values of FPKM to numeric
final_data=pd.concat([fpkm,H3K4me1_mean,H3K4me3_mean,H3K9me3_mean],axis=1,sort=False)
final_data.set_axis(["FPKM","H3K4me1","H3K4me3","H3K9me3"],axis=1,inplace=True)

#print(final_data)

#quit()

model=sm.formula.ols(formula="FPKM ~ H3K4me1+H3K4me3+H3K9me3",data=final_data) #"~" means depends on
#you wanna se whether FPKM depends on sex
ols_result=model.fit()
#print(ols_result.summary())

print(ols_result.resid)

fig,ax=plt.subplots()
ax.hist(ols_result.resid,bins=1000,range=(-100,100))
ax.set_xlim((-100,100))
plt.xlabel("Residual values")
plt.ylabel("Frequency")

fig.savefig("residuals.png")
plt.close(fig)



