__author__ = 'seandolinar'


import csv
import io
import json
import os

listOut = []
with io.open('data_arb2016.json', 'w') as jsonOut:
    with io.open('data_arb2016.csv') as f:

        dictArb = csv.DictReader(f, ['Name','TeamName','Service Time','Player','Team','Mid','Final'])
        print dictArb

        jsonOut.write(u'[')
        i = 0
        for line in dictArb:
            if i > 0:
                jsonOut.write(unicode(json.dumps(line, ensure_ascii=False).encode('utf8')))
                jsonOut.write(u',')
            i += 1

        jsonOut.write(u']')


    #
    #     dictOut = {}
    #
    #     for line in file.read().split('\n'):
    #
    #         for element in line.split(','):
    #
    #             dictOut[]

