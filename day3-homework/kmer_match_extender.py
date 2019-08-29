#!/usr/bin/env python3


from fasta import FASTAReader
import sys

target=FASTAReader(open(sys.argv[1]))
query=FASTAReader(open(sys.argv[2]))

k=int(sys.argv[3])
dic_target={}
target_name={}

for ident, sequence in target:
    sequence=sequence.upper()
    target_sequence[ident]=sequence
    for i in range (0, len(sequence)-k+1):
        kmertarget=sequence[i:i+k]
        if kmertarget not in dic_target:
            dic_target[kmertarget]=[(ident,i)]
        else:
            dic_target[kmertarget].append((ident,i))
            #print(dic_target)
    #print(target_sequence)

for identifier, sequence1 in query:
    sequence1=sequence1.upper()
    for j in range(0,len(sequence1) -k +1):
        kmerquery=sequence1[j:j+k]
        if kmerquery in dic_target:
            for ident, i in dic_target[kmerquery]:
                target_seq=target_sequence[ident]
                length_target_seq=len(target_seq)
                length_query_seq=len(sequence1)
                extend_right=True
                extended_kmer=kmerquery
                while True:
                    if extend_right:
                        if sequence1[j+k+1]==target_seq[i+k+1]:
                            j+=1
                            i+=1
                            extended_kmer+=sequence1[j+k+1]
                        else:
                            extend_right=False
                    else:
                        #this is where i'll add to my dictionary the extention
                        break
                        
                    if (j+k==length_target_seq) or (j+k==length_query_seq):
                        extend_right=False
                        
                #helps us get individual tuples for each target
                #print(j, ident, a, kmerquery)
                
#Target start = i
#Query start =. j





