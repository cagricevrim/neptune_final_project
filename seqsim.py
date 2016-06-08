#! /usr/bin/env python

import random

def BarGen (N):
	Bases = list ( 'ATGC' )
	Barcode = [ random.choice ( Bases ) for i in range (N) ]
	Barcode = ''.join ( Barcode )
	return Barcode

#The flow so far is generating a random barcode of 12bp lenght.
#Now it is required to generate 100 of them and make a list with these 100 unique barcodes.

def BarList(N, M):
	Barcodes = []
	for i in range (N):
		Barcodes.append ( BarGen (M) )
	print (Barcodes)
	return BarList

#Now we have a list of 100 barcodes.
#Next aim to write a function that would generate mRNA reads with random lenghts

def mRNAGen (N):
	Bases = list ( 'ATGC' )
	mRNA = [ random.choice (Bases) for i in range (N) ]
	mRNA = ''.join (mRNA)
	return mRNA

def mRNAlist (N, M):
	mRNAs = []
	for i in range (N):
		mRNAs.append (mRNAGen (M))
	print (mRNAs)
	return mRNAs

#Now I have a library of 100000 random mRNA sequences each is 1000bp long.
#Next step is to select each one of these mRNA sequences and add a barcode at the beginning of it.

BarList(100,12)
mRNAlist (100,5)