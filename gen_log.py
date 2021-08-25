#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#   create Gorilla

import csv
import pandas as pd
import random
from itertools import groupby, repeat
import time


#
##   enter the lines you are interested in from the csv pool (usage_data.csv) and change path to file)
#

fisrtRow = 5834 # first date month (example: 01.09.2019)

SecondRow = 8763 # end date month (example: 31.12.2019)

path = 'usage_data.csv' # full path to file or or upload to the script folder

pathToTime = 'time' # full path to file or or upload to the script folder

#
##  -------------------------------------------------------------------------
#

def getDate():

    dirtPool = []
    print()
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
    # print(datepool)
    time.sleep(5)
    return datepool

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
    time.sleep(5)
    return uc

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
    time.sleep(5)
    return liststatus

def getTime():

    print(f"Get range /hour:min:sec/ from '{pathToTime}'")
    print()

    timelist = []
    with open(pathToTime) as timeFile:
        for lineTime in timeFile:
            timelist.append(lineTime)
    timeRange = [line.rstrip() for line in timelist]
    # print(timeRange) # get a
    time.sleep(5)

    return timeRange


def pushAnotherListToList(randomIntensity,timeRange,uc,datepool,liststatus):

    print("Push list to another list")
    print()

    # all massive
    #------------------------
    datelist = []

    timelist = []

    listuc = []

    status = []
    #------------------------

    count = 0
    listSumNum = 0

    currentNumMonth = "{0}".format(len(datepool))
    floatNumMonth = int(currentNumMonth) - 1

    while count <= floatNumMonth:
        
        #----------------

        index = -1

        sumNum = 0

        #----------------
        
        randFromMassive = random.choice(randomIntensity)
        randFromList = random.choice(randFromMassive) / 100 # get random intens. from csv pool and divide at 100
        num = int(randFromList) # convert to integer

        while index <= 1438:
            
            index = index + 1
            timelist.extend(repeat(timeRange[index], num)) # repeat time x count

            sumNum = sumNum + num # summ count number for status code

            randUC = random.choice(uc) * 1
            listuc.extend(repeat(randUC, num)) # get rand uc from list and repeat x count

        datelist.extend(repeat(datepool[count], sumNum)) # repeat date x count =)

        count = count + 1
        listSumNum = sumNum + listSumNum # summ count number intens for status code
        # print('sum in while',listSumNum)

    for code in range(listSumNum):
        randStatusCode = random.choice(liststatus) * 1
        status.append(randStatusCode) # write status code in log

    print(f"These values must be the same: \n\nlength list date{len(datelist)}\nlength list time{len(timelist)}\nlength list uc{len(listuc)}\nlength list status{len(status)}")

    print(f"\nFinally! Generate log file..")
    print()
    
    DataFrameList = pd.DataFrame({\
    'date':datelist,\
    '\ttime':timelist,\
    'case':listuc,\
    'status': status\
    })
    DataFrameList.to_csv('logs.txt', index=False) # ez, all massive to log file with format .txt


    print(f"Formatting file..")
    fileForFormat = "logs.txt"

    formatFile = open(fileForFormat, "r")
    x = formatFile.read()

    finalLog = x.replace(' ', '').replace(',', '    ')

    with open(fileForFormat, 'w') as logFileFinal:
        logFileFinal.write(finalLog)



#   get current date
date = getDate()
#   get random all intens
intens = getIntensity()
#   get case number
case = getCase()
#   get status code
status = getStatus()
#   get time from file
time = getTime()
#   push list to another massive 0_o / and generate log file...
pushAnotherListToList(intens,time,case,date,status)
