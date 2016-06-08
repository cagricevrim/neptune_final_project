#! /usr/bin/env python

import random

N = 12

Bases = list('ATGC')
Barcode = [ random.choice(Bases) for i in range(N) ]
Barcode = ''.join(Barcode)
print (Barcode)