import numpy as np
import datetime


def toSeasonal(gmean, isLeap):
    if (isLeap):
        year = 2000
        nt = 366 << 2
    else:
        year = 2001
        nt = 365 << 2
    calendar = datetime.datetime(year, 1, 1, 0)

    month = 1
    DJF = np.zeros(4)
    MAM = np.zeros(4)
    JJA = np.zeros(4)
    SON = np.zeros(4)
    DJFNUM = 0
    MAMNUM = 0
    JJANUM = 0
    SONNUM = 0
    for t in range(nt):
        if (  calendar.month ==  1 or calendar.month ==  2 or calendar.month == 12):
            pointer = DJF
            DJFNUM = DJFNUM + 1
        elif (calendar.month ==  3 or calendar.month ==  4 or calendar.month ==  5):
            pointer = MAM
            MAMNUM = MAMNUM + 1
        elif (calendar.month ==  6 or calendar.month ==  7 or calendar.month ==  8):
            pointer = JJA
            JJANUM = JJANUM + 1
        elif (calendar.month ==  9 or calendar.month == 10 or calendar.month == 11):
            pointer = SON
            SONNUM = SONNUM + 1

        if (  calendar.hour ==  0):
            pointer[0] = pointer[0] + gmean[t]
        elif (calendar.hour ==  6):
            pointer[1] = pointer[1] + gmean[t]
        elif (calendar.hour == 12):
            pointer[2] = pointer[2] + gmean[t]
        elif (calendar.hour == 18):
            pointer[3] = pointer[3] + gmean[t]
        else:
            print('ERROR STOP')
            exit(1)

        calendar = calendar + datetime.timedelta(hours=6)

    DJF[:] = DJF[:] / float(DJFNUM>>2)
    MAM[:] = MAM[:] / float(MAMNUM>>2)
    JJA[:] = JJA[:] / float(JJANUM>>2)
    SON[:] = SON[:] / float(SONNUM>>2)

    return DJF, MAM, JJA, SON



