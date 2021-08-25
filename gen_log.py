#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#   create Gorilla

import os
import csv
import pandas as pd
import random
from itertools import groupby


#
##   enter the lines you are interested in from the csv pool (usage_data.csv)
#

fisrtRow = 5834
SecondRow = 8763

#
##  -------------------------------------------------------------------------
#

path = 'usage_data.csv'
def getDate():

    dirtPool = []

    print(f"Get current date from '{path}'")
    print()

    dateRows = pd.read_csv(path,\
    dtype=str,\
    skiprows=fisrtRow,\
    nrows=SecondRow,\
    usecols=[0],\
    delimiter=',')  # get date from csv 1 collumnt
    dirtPool = dateRows.values.tolist() # push to list
    # print(dateRows) # if you need to watch this trash - uncomment
    date = []
    for row in dirtPool:
        for rows in row:
            x = rows[:-5]
            date.append(x)
    date1 = [line.rstrip() for line in date]

    woduplicates = [el for el, _ in groupby(date)]

    datepool = [el for el, _ in groupby(woduplicates)] # append to list, delete space and duplicate date

    del datepool[1]
    del datepool[-1] # delete trash 0_o
    currentNumMonth = "{0}".format(len(datepool))
    floatNumMonth = int(currentNumMonth) - 1 # count rows in list for while
    # print(datepool)

    return datepool,floatNumMonth

