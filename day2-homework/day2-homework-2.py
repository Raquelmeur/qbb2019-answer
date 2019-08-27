#!/usr/bin/env python3

import sys
#id_fly_list=[]
#ac_list=[]

#mapping_file=../day2-homework/Question1-output #day2-homework-1
#c_tab=~/qbb2019-answer/ #893



dic_c_tab={}

for line in open(sys.argv[1]):
    fields=line.rstrip("\n").split("\t")
    dic_c_tab[fields[0]]=fields[1]
# print (dic_c_tab)

for nlines in open(sys.argv[2]):
    list2=nlines.rstrip("\n").split("\t")
    fbgn = list2[8]
    if list2[8] in dic_c_tab:
        print(dic_c_tab[fbgn],nlines.rstrip())
    else:
        if "star"==sys.argv[3]:
            print("*", nlines.rstrip())
        else:
            pass




        #count+=1
        #total+=fpkm


