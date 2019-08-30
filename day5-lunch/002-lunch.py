#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(sys.argv[1],
    sep="\t")

new_df=df.loc[:,["chr","start","end","t_name"]]

strand=df.loc[:,"strand"]=="+"
col_strand=strand.drop(columns="t_name")

new_new_df=new_df.join(col_strand)
#print(strand)
#print(col_strand)
#print(new_new_df)

quant=pd.DataFrame({"quant":[500]*34718})
#print(quant)

new_new_new_df=new_new_df.join(quant)
#print(new_new_new_df)




#print(new_new_new_df.loc[new_new_new_df["strand"] == True])     #it is saying the same as if

# new_new_new_df.loc[new_new_new_df["strand"] ==True]=new_new_new_df["start"]-new_new_new_df["quant"]     #it is saying the same as if
# new_new_new_df["start"]=(new_new_new_df["start"]-new_new_new_df["quant"]).apply()
data={}
for index,row in new_new_new_df.iterrows():
    #print(row["t_name"])
    if row.loc["strand"] == True:
        # print(row.loc["start"])
        row.loc["start"]=int(row.loc["start"])-int(row.loc["quant"])
        if row.loc["start"]<1:
            row.loc["start"]=1
        # print(row.loc["start"])
        end = int(row.loc["start"])+int(row.loc["quant"]*2)
        #print(row.loc["chr"],row.loc["start"], end, row.loc["t_name"],sep="\t")
        print(row.loc["chr"],row.loc["start"], end, row.loc["t_name"],sep="\t")
        
    else:
        row.loc["end"]=int(row.loc["end"])+int(row.loc["quant"])
        if row.loc["end"]<1:
            row.loc["end"]=1
        end=int(row.loc["end"])-(int(row.loc["quant"]*2))
        if end<1:
            end=1
        print(row.loc["chr"],row.loc["end"], end, row.loc["t_name"],sep="\t")
        


# print(new_new_new_df)




