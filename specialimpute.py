import copy
from math import isnan


def SixSort(Data, index, List2, type):
    # Calculate the number of NaN in six rows
    time = 0
    for i in range(6):
        if (isnan(List2[i])):
            time = time + 1

    first = 0
    for i in range(6):
        if (not isnan(List2[i])):
            first = i
        if (first <= 3 and isnan(List2[first + 1]) and (not isnan(List2[first + 2]))):
            List2[first + 1] = (List2[first + 2] + List2[first]) / 2

    first = 0
    for i in range(6):
        if (not isnan(List2[i])):
            first = i
        if (isnan(List2[0]) and (not isnan(List2[1])) and (not isnan(List2[2]))):
            List2[0] = (2 * List2[1] - List2[2])
        elif (isnan(List2[5]) and (not isnan(List2[4])) and (not isnan(List2[3]))):
            List2[5] = (2 * List2[4] - List2[3])
        elif (first <= 3 and isnan(List2[first + 2]) and (not isnan(List2[first])) and (
                not isnan(List2[first + 1]))):
            List2[first + 2] = (2 * List2[first + 1] - List2[first])

    first = 5
    for i in range(6)[::-1]:
        if (not isnan(List2[i])):
            first = i
        if (isnan(List2[4]) and (not isnan(List2[5])) and (not isnan(List2[6]))):
            List2[4] = (2 * List2[5] - List2[6])
        elif (isnan(List2[0]) and (not isnan(List2[1])) and (not isnan(List2[2]))):
            List2[0] = (2 * List2[1] - List2[2])
        elif (first >= 2 and isnan(List2[first - 2]) and (not isnan(List2[first])) and (
                not isnan(List2[first - 1]))):
            List2[first - 2] = (2 * List2[first - 1] - List2[first])

    Data.loc[6 * index, type] = List2[0]
    Data.loc[6 * index + 1, type] = List2[1]
    Data.loc[6 * index + 2, type] = List2[2]
    Data.loc[6 * index + 3, type] = List2[3]
    Data.loc[6 * index + 4, type] = List2[4]
    Data.loc[6 * index + 5, type] = List2[5]

    # return pd.DataFrame(List2,columns=[type])


def Complete(Frame):  # Frame consists of three columns CHLA,Temperature, TotalP
    Data = copy.deepcopy(Frame)

    size = round(len(Data['CHLA']) / 6)
    for i in range(size):
        CHLA = [Data.loc[6 * i, 'CHLA'],
                Data.loc[6 * i + 1, 'CHLA'],
                Data.loc[6 * i + 2, 'CHLA'],
                Data.loc[6 * i + 3, 'CHLA'],
                Data.loc[6 * i + 4, 'CHLA'],
                Data.loc[6 * i + 5, 'CHLA']]
        Temperatue = [Data.loc[6 * i, 'Temperature'],
                      Data.loc[6 * i + 1, 'Temperature'],
                      Data.loc[6 * i + 2, 'Temperature'],
                      Data.loc[6 * i + 3, 'Temperature'],
                      Data.loc[6 * i + 4, 'Temperature'],
                      Data.loc[6 * i + 5, 'Temperature']]
        TotalP = [Data.loc[6 * i, 'TotalP'],
                  Data.loc[6 * i + 1, 'TotalP'],
                  Data.loc[6 * i + 2, 'TotalP'],
                  Data.loc[6 * i + 3, 'TotalP'],
                  Data.loc[6 * i + 4, 'TotalP'],
                  Data.loc[6 * i + 5, 'TotalP']]
        SixSort(Data, i, CHLA, "CHLA")
        SixSort(Data, i, Temperatue, "Temperature")
        SixSort(Data, i, TotalP, "TotalP")

    Data = Data.dropna()

    return Data
