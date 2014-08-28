#!/usr/bin/python

#GVCF TO TILEDB INPUT CSV CONVERTER
#Caveats: 
#	1)Assumes gVCF has blank ID, Qual, Filter fields 
#	2)Assumes <5000 lines of comments 
#	3)Throws out comments 
#	4)Converts chromosome postion to genome-wide globabl position 
#	5)Throws out refseq (will need to get from separate fasta)
#Will Add:
#	1)try, finally block
#	2)with block
#	3)print errors and usage instructions on cmdline
#	4)verify there are no memory issues: csv reader opens line by line?
#	5)separate program - local position to global position converter utility

#---------------------------------------------------------------------------------------------------


from itertools import repeat
import sys
import csv
import gzip
import os

#open input (on cmdline) listfile, read into list
ZippedvcfListSource = open(sys.argv[1])#("fakezippedclusterlist.txt")
ZippedvcfList = ZippedvcfListSource.readlines()
ZippedvcfListSource.close

#generate list of unzipped targets and unzip VCFs into those targets
UnzippedvcfList = []
for ZippedItem in ZippedvcfList
	UnzippedTarget, ZipExtension = os.path.splitext(ZippedItem)
	UnzippedvcfList.append(UnzippedTarget)

	Input = gzip.open(ZippedItem,'r')
	Output = open(UnzippedTarget,'w+')
	Output.write(Input.read())
	Input.close()
	Output.close()

#read in TSV(gVCF) data and write to CSV(TileDB Input)
for UnzippedItem in UnzippedvcfList
	with open(UnzippedItem) as tsvin, open("output.csv", "a") as csvout:
    	#open csv modules
    	tsvin = csv.reader(tsvin, delimiter='\t')
    	csvout = csv.writer(csvout)
    	#find first actual data line
    	NumberofTries = 0
    	for rowindex, rowcontent in enumerate(tsvin):
    		if not "#" in rowcontent[0]:
    			FirstDataLine = rowindex + 1
    			break
    		else: NumberofTries+=1
    		if NumberofTries >=5000:
    			print("ERROR: The parser thinks there are 5000 lines or more of comments. If this is the case increase NumberofTries in the source")
    			sys.exit()
    	#drop every line above first actual data line
    	for LineCounter in range(FirstDataLine):
    		next(tsvin, None)
    	#split row and store each attribute into variable
        for rowcontent in tsvin:
        	chromosome = rowcontent[0]
        	localposition = rowcontent[1]

        	count = int(row[4])
        	if count > 0:
            	csvout.writerows(repeat(row[2:4], count))