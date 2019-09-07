#!/usr/bin/env python3

import sys

gene_list=[]

for line in open(sys.argv[1]):
    fields=line.rstrip("\n").split()
    if fields[0]=="3R" and fields[2]=="gene" and "protein_coding" in line:
        count=8
        for i in fields[8:]:
            count+=1
            if i == "gene_name":
                name=fields[count]
                break
        gene_list.append((fields[3], fields[4],name))
gene_list.sort()
#print(gene_list)

#Binary search
#Note that the gtf file is already sorted

lo = 0
hi = len(gene_list)-1
mid = 0
number_iterations = 0
mutation = 21378950



while (lo < hi):
  mid = int((hi + lo) / 2)
  number_iterations = number_iterations +1
  if ( mutation < int(gene_list[mid][1])):
      hi = mid
  elif (mutation > int(gene_list[mid][1])):
      lo = mid +1
  else:
      break
      
print(gene_list[lo],number_iterations)

quit()
if (abs(gene_list[lo][2] - mutation)) > (abs(gene_list[hi][1]-mutation)):
    mid = hi
    print(abs(gene_list[hi][1]-mutation))
if (abs(gene_list[lo][2] - mutation)) < (abs(gene_list[hi][1]-mutation)):
    mid = lo
    print (abs(gene_list[lo][2] - mutation))

print(gene_list[mid])
print (number_iterations)

  # else:
      # break
       #print(gene_list[0])
       

 
       
       
       