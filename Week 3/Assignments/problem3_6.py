# -problem3_6.py *- coding: utf-8 -*-

import sys

infile = sys.argv[1]
outfile = sys.argv[2]
inf = open(infile)
outf = open(outfile, 'w')
count = []
for line in inf:
    line = line.strip('\n')
    outf.write(str(len(line) - 1) + '\n')
inf.close()
outf.close()
