#! /usr/bin/env python
import random


def seqsim (X, Y, Z, T):
	file = open ( 'SeqSimulation.txt', 'w' )
	Bases = list ( 'ATGC' )
	Barcodes = []
	DropSeq = []

	for i in range (X):
		Barcode = [ random.choice ( Bases ) for i in range (Y) ]
		Barcode = ''.join ( Barcode )
		Barcodes.append ( Barcode )

	for i in range (Z):
		mRNA = [ random.choice (Bases) for i in range (T) ]
		mRNA = ''.join (mRNA)
		Read = ( random.choice(Barcodes) + mRNA + '\n')
		file.write ( Read )

	file.close()

Y = int(raw_input ('Barcode size '))
X = int(raw_input ('Number of barcodes '))
T = int(raw_input ('Lenght of mRNA '))
Z = int(raw_input ('Number of mRNAs reads '))

seqsim (X, Y, Z, T)

print ('Simulations are saved in SeqSimulation.txt in your directory')