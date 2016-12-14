import subprocess
import os
import csv as csv

import odf.opendocument
from odf.table import Table, TableRow, TableCell, TableColumn
from odf.text import P

"""
fileName = '.\example_terminology.txt'
lines = open(fileName, 'r').readlines()
if fileName.endswith('.txt'):
    print("Is text file")
print(lines[0])

idx = lines[0].find("\t")
nativeString = lines[0][0:idx]
targetString = lines[0][idx:].lstrip()
for idx in range(len(lines)):
    print(lines[idx])

"""
# register dialect to comply with converted .cvs file

# read the file

with open('Terminologie.csv', newline='' ) as csvfile:

    data = csv.reader(csvfile, delimiter=',')
    rowSize = 0
    colSize = 0
    rows = []
    for row in data:
        rows.append(row)
        colSize = len(row)
        rowSize = rowSize+1
    rows = rows[1:]
    print(rows)
