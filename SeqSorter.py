#! /usr/bin/env python

X = raw_input ( 'Name of the file ')
f = open ( X, 'r' )
file = open ( 'SortedSeq.txt', 'w' )

lines = f.readlines ()
Y = sorted ( lines )
for item in Y:
	file.write ( item )

f.close()
file.close()

print ( 'The Sequences are sorted and saved in SortedSeq.txt in your directory')