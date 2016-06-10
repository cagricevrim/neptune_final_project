#! /usr/bin/env python
import random


def seqsim (A, B, D, C):
	file = open ( 'SeqSimulation.txt', 'w' ) 														#This is the file that outcomes will be written
	Bases = list ( 'ATGC' )
	Barcodes = []
	DropSeq = []

	for i in range (A):
		Barcode = [ random.choice ( Bases ) for i in range (B) ]									#random.choice makes a list of (B) items from the Bases list.
		Barcode = ''.join ( Barcode ) 																#Join takes the items of this list and generate a string via concatenating them
		Barcodes.append ( Barcode ) 																#Adding each barcode (string) to the list of Barcodes as an item.

	for i in range (D):
		mRNA = [ random.choice (Bases) for i in range (C) ]											#Choosing random bases and make a list
		mRNA = ''.join (mRNA)																		#Concatenating the bases and generating a sequence (string)
		Read = ( random.choice(Barcodes) + mRNA + '\n')												#choosing a random barcode and concatenating it with mRNA generated and puting a line ending 
		file.write ( Read )																			#then writing it in the file (SeqSimulation.txt)

	file.close()

B = int(raw_input ( 'Barcode size ' ))																#These a re the parameters asked to the user.
A = int(raw_input ( 'Number of barcodes ' ))
C = int(raw_input ( 'Length of mRNA ' ))
D = int(raw_input ( 'Number of mRNAs reads ' ))

seqsim (A, B, D, C)																					#After parameters are given, this runs the function with given parameters.

print ('Simulations are saved in SeqSimulation.txt in your directory')								#Notification for the user

H = raw_input ( 'Would you like the sequences to be sorted according to barcodes Y/N ? ' )			#Question to the user for continum.
H = H.upper ()																						#Capitalizing the answer letter

def seqsorter ( X ):																				#This is the function that sort sequences into alphabetical order.
	f = open ( X, 'r' )																				#Working on the file X
	file = open ( 'SortedSeq.txt', 'w' )															#And writing the outcome in the file SortedSeq.txt

	lines = f.readlines ()																			#reading the lines of the file X
	Y = sorted ( lines )																			#sorting the lines into alphabetical order
	for item in Y:																					#writing every row to the file (SortedSeq.txt)
		file.write ( item )

	f.close()								
	file.close()

	print ( 'The Sequences are sorted and saved in SortedSeq.txt in your directory' )				#Notification for the user

if H == ( 'Y' ):																					#If the answer for the question on line 33 is Y it executes the function on SeqSimulation.txt
	seqsorter ( 'SeqSimulation.txt' )