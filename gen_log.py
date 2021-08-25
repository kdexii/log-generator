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

def getIntensity():

    print(f"Get intensity")
    print()
    intenRows = pd.read_csv(path,\
    dtype=float,\
    skiprows=fisrtRow,\
    nrows=SecondRow,\
    usecols=[1,2,3,4,5,6,7,8],\
    delimiter=',')
    randomIntensity = intenRows.values.tolist()
    # print(randomIntensity)
    return randomIntensity

def getCase():
    print(f"Get all case from pool")
    print()
    with open('usage_data.csv', newline='') as f:
        reader = csv.reader(f)
        uc = next(reader) # get uc list from csv row 0
        del uc[0]
    # print(uc)
def getStatus():
    print(f"Get status code")
    print()
    liststatus = ['success',\
        'error',\
        'success',\
        'success',\
        'success',\
        'success']
    # print(liststatus) # i was too lazy to come up with something, so im did so =)
    return liststatus

def getTime():
    timelist = []
    counthour = -1
    countMin = -1
    while counthour <= 23:
        counthour = counthour + 1
        timelist.append(f'{counthour}:')
    print(timelist)
getDate()
getIntensity()
getCase()
getStatus()
getTime()