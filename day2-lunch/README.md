#Question 1-
a)
head -n 40000 ~/data/rawdata/SRR072893.fastq > SRR072893.10k.fastq
wc -l SRR072893.10k.fastq

b)
fastqc SRR072893.10k.fastq
open SRR072893.10k_fastqc.html

c)
hisat2-build -p 4 ~/data/genomes/BDGP6.fa BDGP6
hisat2 -p 4 -x BDGP6 -U SRR072893.10k.fastq -S SRR072893.10k.sam

d)
samtools sort SRR072893.10k.sam -@ 4 > SRR072893.10k.bam
samtools index SRR072893.10k.bam

e)
stringtie SRR072893.10k.bam -G ~/qbb2019-answer/genomes/BDGP6.Ensembl.81.gtf -o SRR072893.10k.gtf -p -4 -B -e

done

#Question3-
(you first sort the gtf file and feed it to the cut function, where you just set it to read the first column with the chromosomes names, then using uniq -c you count the unique alignments in their clusters and therefore get the counts on each chromosome)

/Users/cmdb/qbb2019-answer/day2-lunch $ sort SRR072893.10k.gtf | cut -f 1 | uniq -c > question3_lunch
