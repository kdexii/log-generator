
import pandas as pd

"""
    Этот скрипт не нужно трогать (кроме path),
    просто указать путь к самописному пулу интенсивностей
    запустить его, он сам создаст все для data.csv и умножит первую колонку 4 раза на X значения

"""

FirstRowForInten = 0 # first date month (example: 01.09.2019)

SecondRowForInten = 8762 # end date month (example: 31.12.2019)

path = 'usage_data.csv'


def xz():
    
    print()
    inten1 = []
    inten2 = []
    inten3 = []
    inten4 = []

    intenRowsDivide = pd.read_csv(path,\
        dtype=float,\
        skiprows=FirstRowForInten,\
        nrows=SecondRowForInten,\
        usecols=[1],\
        delimiter=',')
    IntenList = intenRowsDivide.values.tolist()
    # a = [[float(j)/sum(i) for j in i] for i in randomIntensity]
    print(f"Divide collumn at 0.85")
    for i in IntenList:
        for j in i:
            calc = float(j)*0.85
            inten1.append(calc)
    # print(inten1)
    print()
    print(f"Divide collumn at 0.95")

    for i in IntenList:
        for j in i:
            calc = float(j)*0.95
            inten2.append(calc)
    # print(inten2)
    print()
    print(f"Divide collumn at 0.75")

    for i in IntenList:
        for j in i:
            calc = float(j)*0.75
            inten3.append(calc)
    # print(inten3)
    print()
    print(f"Divide collumn at 0.79")

    for i in IntenList:
        for j in i:
            calc = float(j)*0.79
            inten4.append(calc)
    # print(inten2)
    



    dirtPool = []
    print()
    print(f"Get current date from '{path}'")
    print()


    a = pd.read_csv(path,\
    dtype=str,\
    usecols=[0],\
    delimiter=',')  # get date from csv 1 collumnt
    dirtPool = a.values.tolist() # push to list
    date = []
    for row in dirtPool:
        for rows in row:
            date.append(rows)

    b = pd.read_csv(path,\
    dtype=float,\
    usecols=[1],\
    delimiter=',')  # get date from csv 1 collumnt
    dirtPool = b.values.tolist() # push to list
    bint = []
    for row in dirtPool:
        for rows in row:
            # x = rows[:-5]
            bint.append(rows)
    c = pd.read_csv(path,\
    dtype=float,\
    usecols=[2],\
    delimiter=',')  # get date from csv 1 collumnt
    dirtPool = c.values.tolist() # push to list
    cint = []
    for row in dirtPool:
        for rows in row:
            # x = rows[:-5]
            cint.append(rows)
    d = pd.read_csv(path,\
    dtype=float,\
    usecols=[3],\
    delimiter=',')  # get date from csv 1 collumnt
    dirtPool = d.values.tolist() # push to list
    dint = []
    for row in dirtPool:
        for rows in row:
            # x = rows[:-5]
            dint.append(rows)
    f = pd.read_csv(path,\
    dtype=float,\
    usecols=[4],\
    delimiter=',')  # get date from csv 1 collumnt
    dirtPool = f.values.tolist() # push to list
    fint = []
    for row in dirtPool:
        for rows in row:
            # x = rows[:-5]
            fint.append(rows)
    print(f"len:", len(date),len(bint),len(cint),len(dint),len(fint),len(inten1),len(inten2),len(inten3),len(inten4))
    DataFrameList = pd.DataFrame({\
    'datetime':date,\
    'UC01':bint,\
    'UC02':cint,\
    'UC03':dint,\
    'UC04':fint,\
    'UC05':inten1,\
    'UC06':inten2,\
    'UC07':inten3,'UC08':inten4})
    DataFrameList.to_csv('data.csv', index=False)

xz()
