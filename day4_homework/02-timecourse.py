#!/usr/bin/env python

"""
/Users/cmdb/qbb2019-answer/day4_homework $ ./02-timecourse.py FBtr0331261 ~/qbb2019/data/samples.csv ~/qbb2019/data/replicates.csv ~/qbb2019-answer/results/stringtie/

Usage: 02-timecourse.py <ty_name> <samples.csv> <FPKMs>

Create a timecourse of a given transcript for females
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import os

#Specify transcript of interest
t_name=sys.argv[1]

#Load metadata
samples=pd.read_csv(sys.argv[2])
repet=pd.read_csv(sys.argv[3])
ctab_dir=sys.argv[4]
print(type(samples))

def sex(finder,rep):
    soi=rep.loc[:,"sex"]==finder
    srr_ids=rep.loc[soi,"sample"]
    my_data=[]
    
          #return #you return them to actually have those variables
    for srr_id in srr_ids:
        ctab_path = os.path.join (ctab_dir, srr_id, "t_data.ctab") # Find path to ctab file
        df = pd.read_csv (ctab_path, sep="\t",index_col="t_name") # Load ctab file
        #fpkms=pd.read_csv(sys.argv[3], index_col="t_name")
        my_data.append(df.loc[t_name,"FPKM"]) # Grab the FPKM value for our transcript, and append to my_data
        #print(srr_id)
        #my_data.append(fpkms.loc[t_name,srr_id])
    return my_data
#soi, srr_ids = sex("female")=female        #that is how you call them to exist
male_vals=sex("male",repet)
male_vals2=sex("male",samples)
fem_vals=sex("female",repet)
fem_vals2=sex("female",samples)

#quit()
#load FPKMs

# #Extract data
# my_data=[]
# for srr_id in srr_ids:
#     #print(srr_id)
#     my_data.append(fpkms.loc[t_name,srr_id])
    
#print(my_data)

fig, ax =plt.subplots()
ax.plot(range(4,8),fem_vals,"x", color="red", label='female')
ax.plot(fem_vals2, color="red", label='male')
ax.plot(range(4,8),male_vals, "x",color="blue", label='male')
ax.plot(male_vals2, color="blue", label='male')
ax.legend(loc='lower right', bbox_to_anchor=(1.3, .5))
ax.set_xticklabels(["0", "10", "11", "12", "13", "14A", "14B", "14C", "14D"])
ax.set_ylabel("mRNA abundance(RPKM)")
ax.set_xlabel("development stage")
fig.suptitle("Sxl", style="italic")

plt.tight_layout()
plt.subplots_adjust(top=0.9)
fig.savefig("timecourse.png")
plt.close(fig)
