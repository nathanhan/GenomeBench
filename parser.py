#!/usr/bin/python
from itertools import repeat
import sys
import csv

#eventually will need to support command line args to input list/print usage notes
#TEMPORARU HARD CODE SOLUTION: set target VCF list here
vcflist = open("/home/nathanhan/cmdfiles/clusterlist.txt")


target = vcflist.readline()
with open('sample.txt','rb') as tsvin, open('new.csv', 'wb') as csvout:
    tsvin = csv.reader(tsvin, delimiter='\t')
    csvout = csv.writer(csvout)

    for row in tsvin:
        count = int(row[4])
        if count > 0:
            csvout.writerows(repeat(row[2:4], count))