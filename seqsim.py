#! /usr/bin/env python
import random

Bases = list ( 'ATGC' )
Barcode = [ random.choice ( Bases ) for i in range (12) ]
Barcode = ''.join ( Barcode )

#The flow so far is generating a random barcode of 12bp lenght.
#Now it is required to generate 100 of them and make a list with these 100 unique barcodes.

Barcodes = []
for i in range (100):
	Barcodes.append ( Barcode )

#Now we have a list of 100 barcodes.
#Next aim to write a function that would generate mRNA reads with random lenghts

mRNA = [ random.choice (Bases) for i in range (1000) ]
mRNA = ''.join (mRNA)

#This generates a random mRNA lenght of 1000bp
#now I have to generate 10000 mRNA reads and each of them should have one of the barcodes that was generated.

Read = [ random.choice(Barcodes) + mRNA]

#This picks a barcode from the list and concatenates it with a random 1000bp sequence.

DropSeq = []
for i in range (10000):
	DropSeq.append (Read)

#This makes a list of 10000 reads which has a barcode and a mRNA.

print(DropSeq)