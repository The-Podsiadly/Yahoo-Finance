import time
# st = time.time()

import os, csv, xlrd, re

def getSymbols(dir, filename):
    stockTick = []  # Declare empty array for stock Ticks

    file = os.path.join(dir, filename)
    _, fileExtension = os.path.splitext(file)

    if fileExtension == '.csv':
        with open(file, "r", newline="", encoding="utf8") as _file:  # Open file to read data
            for line in _file:
                # TODO: Get rid of spaces
                l = re.split(',|[|]|;', line)[0].replace('"', "").strip()

                stockTick.append(l)

    elif fileExtension == '.xlsx':
        workbook = xlrd.open_workbook(file)
        sheet = workbook.sheet_by_index(0)
        read = sheet.col_values(0)

        for row in read:
            stockTick.append(row)

    return stockTick


def getFiles(folder):
    root = os.getcwd()
    dir = os.path.join(root,folder)

    (_, _, filenames) = next(os.walk(dir), (None, None, []))

    return dir, filenames



def getList(folder = 'Companies'):
    dir, filenames = getFiles(folder)

    dataSet = []
    for i, f in enumerate(filenames):
        data = getSymbols(dir, f)
        dataSet.extend(data)

    # dataSet = manipulate(data_sets)

    # print(f'Time to get all ticks: {time.time() - st}')

    return dataSet