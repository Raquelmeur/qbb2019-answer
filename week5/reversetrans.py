#!/usr/bin/env python3

import sys

from fasta import FASTAReader
import math
import matplotlib.pyplot as plt
import statistics as stats

reader = FASTAReader(open(sys.argv[1]))
reader2=FASTAReader(open(sys.argv[2]))

my_prot_sequence = [] #protein
for ident, sequence in reader:
   my_prot_sequence.append(sequence)
#print(my_sequence)
#quit()
my_sequence_nt=[] #nucleotide
for ident2,sequence2 in reader2:
    my_sequence_nt.append(sequence2)
#print(my_sequence_nt)
newlist=[]
#for m in my_sequence_nt:
    #dna = my_sequence_nt[m]#you only need to do it in the query sequence
#store by sequence identity in dictionary
# for i in range(len(my_prot_sequence)):
    #dna= str(dna)
for sequence, protein in zip(my_sequence_nt,my_prot_sequence):
    gap_dna = ""
    nucl_pos=0
    for num, a in enumerate(protein):
      # print(a)
      if a == "-":
          gap_dna = gap_dna + "---"
      else:
          gap_dna = gap_dna + sequence[nucl_pos:nucl_pos+3]
          nucl_pos+=3
    newlist.append(gap_dna)
#print(newlist)
#quit()
codons = {
     "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
     "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
     "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
     "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
     "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
     "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
     "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
     "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
     "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
     "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
     "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
     "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
     "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
     "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
     "TAC":"Y", "TAT":"Y", "TAA":"", "TAG":"",
     "TGC":"C", "TGT":"C", "TGA":"_", "TGG":"W"}
     
query = newlist[0]
rest_of_dna_seq=newlist[1:]

#print(rest_of_dna_seq)

dSyn_list=[]
dNon_list=[]

for i in range(0,(len(query)),3):
    dSyn=0
    dNon=0
    #print(query[1:i+3])
    if query[i:i+3]=="---":
        continue
    for sequence in rest_of_dna_seq:
        if sequence[i:i+3]=="---":
            continue
        if sequence[i:i+3] not in codons:
            continue
        if query[i:i+3]!=sequence[i:i+3] and codons[query[i:i+3]]==codons[sequence[i:i+3]]:
            dSyn+=1
        if query[i:i+3]!=sequence[i:i+3] and codons[query[i:i+3]]!=codons[sequence[i:i+3]]:
            dNon+=1
    dSyn_list.append(dSyn)
    dNon_list.append(dNon)
print(dSyn_list)
#quit()
ratioSN=[]
for i in range(len(dSyn_list)):
    ratio=(dSyn_list[i]+1)/(dNon_list[i]+1)
    log_ratio=math.log2(ratio)
    ratioSN.append(ratio)
print(ratioSN)

diffentSSN=[]
for i in range(len(dSyn_list)):
    differ = dSyn_list[i]-dNon_list[i]
    diffentSSN.append(differ)
stdev_differ=stats.stdev(diffentSSN)
print(stdev_differ)
z_score=[]
for i in diffentSSN:
    zscore=i/stdev_differ
    z_score.append(zscore)
print(z_score)

colors = ['red' if zscore > 1.645 or zscore<-1.645 else 'black'for zscore in z_score]
fig, ax = plt.subplots()
ax.scatter([x for x in range(len(z_score))], ratioSN, color=colors, s=2)
ax.set_xlabel('position')
ax.set_ylabel('log2(dN/dS)')
fig.savefig("plotZscore.png")
plt.close(fig)


