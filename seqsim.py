#! /usr/bin/env python
import random

Bases = list ( 'ATGC' )
Barcodes = []
DropSeq = []

for i in range (100):
	Barcode = [ random.choice ( Bases ) for i in range (12) ]
	Barcode = ''.join ( Barcode )
	Barcodes.append ( Barcode )

for i in range (10000):
	mRNA = [ random.choice (Bases) for i in range (150) ]
	mRNA = ''.join (mRNA)
	Read = ( random.choice(Barcodes) + mRNA)
	print (Read)
#	DropSeq.append (Read)

#print(DropSeq)