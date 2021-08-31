from datetime import date
import pandas as pd
from collections import defaultdict
import csv
import numpy as np
from collections import Counter
from itertools import groupby


inputLog = 'logs.txt'
outputLog = 'logs.csv'
path = outputLog


fileForFormat = outputLog

formatFile = open(inputLog, "r")
x = formatFile.read()

finalLog = x.replace('    ', ',')

with open(fileForFormat, 'w') as logFileFinal:
    logFileFinal.write(finalLog)
def fuck1():
    df = pd.read_csv(path, delimiter=',', dtype=str)
    b = df.drop_duplicates()
    # 

    
    # x = b.iloc[[0 -1]]
    # print(str(x))
    val = df.index[-1] + 2
    val = int(val)
    listidx = []

    count4 = -1
    while count4 <= val - 3:
        count4 = count4 + 1
        listidx.append(count4)

    df['idx'] = listidx
    df.to_csv(r'logs.csv', index=None, sep=',')
    print(df)

timelist = []
with open('removetime', 'r') as remTime:
    for lineTime in remTime:
        timelist.append(lineTime)
    timeRange = [line.rstrip() for line in timelist]
# print(timeRange)
datelist = []


def getDate():
    dirtPool = []
    print()
    print(f"Get current date from '{path}'")
    print()

    dateRows = pd.read_csv(path,\
        dtype=str,\
        skiprows=2,\
        nrows=10535041,\
        usecols=[0],\
        delimiter=',')  # get date from csv 1 collumnt
    dirtPool = dateRows.values.tolist() # push to list
        # print(dateRows) # if you need to watch this trash - uncomment
    date = []
    for row in dirtPool:
            for rows in row:
                date.append(rows)
    date1 = [line.rstrip() for line in date]

    woduplicates = [el for el, _ in groupby(date)]

    datepool = [el for el, _ in groupby(woduplicates)] # append to list, delete space and duplicate date

    print(len(datepool))
    return datepool
def createProfile(datepool):
    df = pd.read_csv(path, delimiter=',', usecols=[0], dtype=str)
    b = df.drop_duplicates()
    # 

    
    # x = b.iloc[[0 -1]]
    # print(str(x))
    val = df.index[-1] + 2
    val = int(val)
    listidx = []

    count4 = -1
    while count4 <= val - 3:
        count4 = count4 + 1
        listidx.append(count4)

    df['idx'] = listidx
    # print(df)

    for row in b.itertuples():
        trash = row[0] + 1
        datelist.append(trash)
    # x = df.iloc[[-1]]
    # print(x[0])
    date1 = []
    date2 = []
    currentNumMonth = "{0}".format(len(datelist))
    floatNumMonth = int(currentNumMonth) - 2
    count = -1
    while count <= floatNumMonth:
        count = count + 1
        # print(f'first row number: {datelist[count] + 1}') # first row for date
        date1.append(datelist[count] + 1)
    count2 = 0
    while count2 <= floatNumMonth:
        count2 = count2 + 1
        # print(f'second row number: {datelist[count2]}') # second row for date
        date2.append(datelist[count2])

    date2.append(int(val))
    print(len(date1))
    print(len(date2))



    
    count3 = -1
    
    while count3 <= 0:
        final = []
        count3 = count3 + 1
        intenRows = pd.read_csv(path,\
        dtype=str,\
        skiprows=date1[count3],\
        nrows=date2[count3],\
        usecols=[1],\
        delimiter=',')
        # b = intenRows[~intenRows.time.str.contains("00:59:00")]
        a = intenRows.loc[intenRows['00:00:00'].isin(['00:59:00','01:59:00','02:59:00','03:59:00','04:59:00','05:59:00','06:59:00','07:59:00','08:59:00','09:59:00',\
            '10:59:00','11:59:00','12:59:00','13:59:00','14:59:00','15:59:00','16:59:00','17:59:00','18:59:00','19:59:00','20:59:00','21:59:00','22:59:00','23:59:00',])]
        b = a.drop_duplicates()
        # print(b)
        print(b)
        s = b.index.tolist()
        # print(s)
        final.append(0)
        for row in s:
            final.append(row)
        # print(len(final))
        count5 = -1

        count7 = -1
        count6 = 0
        
        uc1 = []
        uc2 = []
        uc3 = []
        uc4 = []
        uc5 = []
        uc6 = []
        uc7 = []
        uc8 = []
        while count5 <= 22:
            count7 = count7 + 1
            count6 = count6 + 1
            
            count5 = count5 + 1
            # print(f"dick{count5}: ", final[count5])
            # print("cnt start: ",final[count7])
            # print("cnt end: ", final[count6] - 1)
            print(final[count7],' to ',final[count6] - 1)
            fuck3 = pd.read_csv(path, usecols=[2], delimiter=',')
            xz = fuck3.iloc[final[count7]:final[count6] - 1] 
            # dirtPool = fuck3.values.tolist()
            a = xz.groupby(xz.columns.tolist(),as_index=False).size()
            # for row in dirtPool:
            # print(a)
            # fuck3 = pd.read_csv(path, delimiter=',',skiprows=final[count7],nrows=nrows=final[count6] - 1, usecols=[2])
            # a = fuck3.pivot_table(index=list(fuck3), aggfunc='size')
            b = a.iloc[:,1]
            # print(b[1])
            uc1.append(b[0])
            uc2.append(b[1])
            uc3.append(b[2])
            uc4.append(b[3])
            uc5.append(b[4])
            uc6.append(b[5])
            uc7.append(b[6])
            uc8.append(b[7])
        print(uc1)
        print(uc2)
        print(uc3)
        print(uc4)
        print(uc5)
        print(uc6)
        print(uc7)
        print(uc8)

        timeHour = ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00',\
            '11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00',]
        fuck11 = open('profile.csv', 'w')
        fuck11.write('date,time,UC01,UC02,UC03,UC04,UC05,UC06,UC07,UC08\n')
        fuck11.close
        with open('profile.csv', 'a+') as fuck5:
            fuck10 = -1
            while fuck10 <= 22:
                fuck10 = fuck10 + 1
                print(fuck10)
                fuck5.write(f"{datepool[0]},{timeHour[fuck10]},{uc1[fuck10]},{uc2[fuck10]},{uc3[fuck10]},{uc4[fuck10]},{uc5[fuck10]},{uc6[fuck10]},{uc7[fuck10]},{uc8[fuck10]}\n")






# def openLog():
#     count2 = 0

#     fisrtRow = 0
#     SecondRow = 4643 - 1

#     while count2 <=2:
#         count2 = count2 + 1
#         df = pd.read_csv(path, delimiter=',',skiprows=fisrtRow,nrows=SecondRow, usecols=[2])
#         # print(df)
#         a = df.pivot_table(index=list(df), aggfunc='size')
#         uc1.append(a[0])
#         uc2.append(a[1])
#         uc3.append(a[2])
#         uc4.append(a[3])
#         uc5.append(a[4])
#         uc6.append(a[5])
#         uc7.append(a[6])
#         uc8.append(a[7])
    # for row in uc:
        # print(row)
    # print(uc2)
    # D = defaultdict(list)
    # for i,item in enumerate(uc2):
    #     D[item].append(i)
    # D = {k:v for k,v in D.items() if len(v)>1}
    # print(D)

# fuck1()
# openLog()
date = getDate()
createProfile(date)
# fuck3 = pd.read_csv(path,skiprows=60674,nrows=63313, usecols=[2], delimiter=',')
# xz = fuck3.iloc[13154:15793] 
# # dirtPool = fuck3.values.tolist()
# a = xz.groupby(xz.columns.tolist(),as_index=False).size()
# # for row in dirtPool:
# print(a)


# a = fuck3.pivot_table(index=list(fuck3), aggfunc='size')
# a = fuck3.groupby(fuck3.columns.tolist(),as_index=False).size()
# dups = fuck3.groupby(fuck3.columns.tolist()).size().reset_index().rename(columns={0:'count'})
# spisok = Counter(fuck3['UC02'])
# print(spisok)
# uc1.append(a[0])
# uc2.append(a[1])
# uc3.append(a[2])
# uc4.append(a[3])
# uc5.append(a[4])
# uc6.append(a[5])
# uc7.append(a[6])
# uc8.append(a[7])