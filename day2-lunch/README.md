Question 1-
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
