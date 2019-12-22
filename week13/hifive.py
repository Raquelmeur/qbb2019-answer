#!/usr/bin/env python3

import sys
import numpy

enh_act=open(sys.argv[1])
rna=open(sys.argv[2])
enh={}
rnadic={}

for i, line in enumerate(enh_act):
    if i ==0:
        continue
    position=line.rstrip("/n").split()
    #print(position)
#quit()
    if int(position[1])>=5000000 and int(position[2])<=40000000:
        pos=(int(position[1])-5000000)/5000
        print(pos)
        enh[pos]=float(position[4])
#print (enh)


for a, lines in enumerate(rna):
    if a==0:
        continue
    positionRNA=lines.rstrip("/n").split()
    if int(positionRNA[1])>=5000000 and int(positionRNA[2])<=40000000:
        posRNA=(int(positionRNA[1])-5000000)/5000
        rnadic[posRNA]=float(positionRNA[4])
#print(rnadic)

enharray=numpy.array(enh)
rnarray=numpy.array(rnadic)

#quit()
import hifive

hic = hifive.HiC('PROJECT_FNAME', 'r')
data = hic.cis_heatmap(chrom='chr10', start=5000000, stop=40000000, binsize=5000, datatype='fend', arraytype='full')
where = numpy.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = numpy.log(data[:, :, 0] + 0.1)
data -= numpy.amin(data)
data_subset=data[numpy.where(rnaa > 0), :]
sum_data_subset= numpy.sum(data_subset, axis=1)
R= numpy.corrcoef(sum_data_subset, rnaa)[0, 1]
print(R)

