#! /usr/bin/env python
import random


def seqsim (A, B, D, C):
	file = open ( 'SeqSimulation.txt', 'w' )
	Bases = list ( 'ATGC' )
	Barcodes = []
	DropSeq = []

	for i in range (A):
		Barcode = [ random.choice ( Bases ) for i in range (B) ]
		Barcode = ''.join ( Barcode )
		Barcodes.append ( Barcode )

	for i in range (D):
		mRNA = [ random.choice (Bases) for i in range (C) ]
		mRNA = ''.join (mRNA)
		Read = ( random.choice(Barcodes) + mRNA + '\n')
		file.write ( Read )

	file.close()

B = int(raw_input ('Barcode size '))
A = int(raw_input ('Number of barcodes '))
C = int(raw_input ('Lenght of mRNA '))
D = int(raw_input ('Number of mRNAs reads '))

seqsim (A, B, D, C)

print ('Simulations are saved in SeqSimulation.txt in your directory')

H = raw_input ( 'Would you like the sequences to be sorted according to barcodes Y/N ? ' )

def seqsorter ( X ):
	f = open ( X, 'r' )
	file = open ( 'SortedSeq.txt', 'w' )

	lines = f.readlines ()
	Y = sorted ( lines )
	for item in Y:
		file.write ( item )

	f.close()
	file.close()

	print ( 'The Sequences are sorted and saved in SortedSeq.txt in your directory')

if H == ( 'Y' ):
	seqsorter ( 'SeqSimulation.txt')