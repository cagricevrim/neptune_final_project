#! /usr/bin/env python

import random

#N = 12

def BarGen (N):
	Bases = list ( 'ATGC' )
	Barcode = [ random.choice ( Bases ) for i in range (N) ]
	Barcode = ''.join ( Barcode )
	return Barcode

#The flow so far is generating a random barcode of 12bp lenght.
#Now it is required to generate 100 of them and make a list with these 100 unique barcodes.

Barcodes = [ ]

for i in range (100):
	Barcodes.append ( BarGen (12) )
	
print (Barcodes)

#Now we have a list of 100 barcodes.