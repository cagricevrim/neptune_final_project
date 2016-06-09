#! /usr/bin/env python
import random

Bases = list ( 'ATGC' )
Barcodes = []
DropSeq = []

for i in range (100):
	Barcode = [ random.choice ( Bases ) for i in range (12) ]
	Barcode = ''.join ( Barcode )
	Barcodes.append ( Barcode )

for i in range (5):
	mRNA = [ random.choice (Bases) for i in range (1000) ]
	mRNA = ''.join (mRNA)
	Read = ( random.choice(Barcodes) + mRNA)
	DropSeq.append (Read)

print(DropSeq)