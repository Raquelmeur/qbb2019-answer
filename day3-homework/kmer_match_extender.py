#!/usr/bin/env python3

#the target sequence we are using is the ensembl GTF file (so they are transcripts formed by the alignment)

from fasta import FASTAReader
import sys

target=FASTAReader(open(sys.argv[1]))
query=FASTAReader(open(sys.argv[2]))

k=int(sys.argv[3])
dic_target={}
target_name={}
target_sequence={}

for ident, sequence in target:
    sequence=sequence.upper()
    target_sequence[ident]=sequence     #dictionary with ident:complete sequence
    for i in range (0, len(sequence)-k+1):
        kmertarget=sequence[i:i+k]      #making the kmers
        if kmertarget not in dic_target:
            dic_target[kmertarget]=[(ident,i)]
        else:
            dic_target[kmertarget].append((ident,i))
            #print(dic_target)
    #print(target_sequence)
final_dic={}
for identifier, sequence1 in query:
    sequence1=sequence1.upper()
    for j in range(0,len(sequence1) -k +1):
        kmerquery=sequence1[j:j+k]      #kmerquery
        if kmerquery in dic_target:
            for ident, i in dic_target[kmerquery]:
                target_seq=target_sequence[ident]
                #print(target_seq)
                #print(type(target_seq))
                length_target_seq=len(target_seq)
                #print(length_target_seq)
                length_query_seq=len(sequence1)
                extend_right=True
                extended_kmer=kmerquery 
                total_kmer=[]
                #print(extended_kmer)
                while True:
                    if (i+k==length_target_seq) or(j+k==length_query_seq):
                        if ident in final_dic:
                            final_dic[ident].append(extended_kmer)
                        else:
                            final_dic[ident]=[extended_kmer]
                        break
                    if sequence1[j+k]==target_seq[i+k]:
                        extended_kmer+=sequence1[j+k]
                        j+=1
                        i+=1
                    else:
                        if ident in final_dic:
                            final_dic[ident].append(extended_kmer)
                        else:
                            final_dic[ident]=[extended_kmer]
                        break
                         #this is where i'll add to my dictionary the extention
#print(final_dic)
                    
                    # total_kmer.append(extended_kmer)
                    #
                    # print(total_kmer)
#                     quit()
# print(final_dic)
# quit()
list_final=[]
# list_values=final_dic.values()
for x in final_dic.values():
    for r in x:
        list_final.append(r)
#print(list_final)

#quit()
for sort in sorted(list_final, key=len, reverse=True):
    print (sort)
    







