#! /usr/bin/env python
import re

f = open ('seqs.txt', 'r')

lines = f.readlines()
print(sorted(lines))
f.close()

