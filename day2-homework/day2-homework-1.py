#!/usr/bin/env python3

import sys
#id_fly_list=[]
#ac_list=[]

for i, line in enumerate(sys.stdin):
    if "DROME" not in line:
        continue
    if "FBgn" not in line:
        continue
    columns=line.rstrip("\n").split()
    id_fly=columns[-1]
    ac=columns[-2]
    print(id_fly, ac)
    
    
    
    #id_fly_list.append(id_fly)
    #ac_list.append(ac)

    