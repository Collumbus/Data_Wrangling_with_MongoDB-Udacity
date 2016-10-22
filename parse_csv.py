import os
import pprint
import csv
DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    n = 0
    with open(datafile,'rb') as sd:
        r = csv.DictReader(sd)
        for line in r:
            data.append(line)
    return data

data = parse_file(DATAFILE)

print data
