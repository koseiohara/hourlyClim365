import datetime
import numpy as np

from filein import filein

def seasonal(filename, hourstep, ny, leap):

    if (leap):
        calendar = datetime.datetime(2000, 1, 1, 0)
        nt = 366 * int(24/hourstep) 
    else:
        calendar = datetime.datetime(2001, 1, 1, 0)
        nt = 365 * int(24/hourstep) 


    ifile = filein(filename = filename, \
                   shape    = [ny]    , \
                   recl     = 4*ny    , \
                   rec      = 1       , \
                   kind     = 4       , \
                   endian   = 'little', \
                   recstep  = 1         )

    DJF = np.zeros(ny)
    MAM = np.zeros(ny)
    JJA = np.zeros(ny)
    SON = np.zeros(ny)

    DJFNUM = 0
    MAMNUM = 0
    JJANUM = 0
    SONNUM = 0

    work_reader = np.empty(ny)

    for t in range(nt):
        ## Pointer Copy
        if (calendar.month == 1 or calendar.month == 2 or calendar.month == 12):
            work_pointer = DJF
            DJFNUM = DJFNUM + 1
        elif (calendar.month == 3 or calendar.month == 4 or calendar.month == 5):
            work_pointer = MAM
            MAMNUM = MAMNUM + 1
        elif (calendar.month == 6 or calendar.month == 7 or calendar.month == 8):
            work_pointer = JJA
            JJANUM = JJANUM + 1
        elif (calendar.month == 9 or calendar.month == 10 or calendar.month == 11):
            work_pointer = SON
            SONNUM = SONNUM + 1


        ### DEBUGGER
        #date = datetime.datetime.strftime(calendar, '%Y/%m/%d %H')
        #print(date, ', DJF : ', id(DJF), ', MAM : ', id(MAM), ', JJA : ', id(JJA), ', SON : ', id(SON), ', WORK : ', id(work_pointer))
        work_reader[:] = ifile.fread()

        work_pointer[:] = work_pointer[:] + work_reader[:]

        calendar = calendar + datetime.timedelta(hours=hourstep)

    #cos = np.cos(np.linspace(-90., 90., ny)*np.pi/180.)
    cos = 1.

    DJF = cos * DJF[::-1] / float(DJFNUM)
    MAM = cos * MAM[::-1] / float(MAMNUM)
    JJA = cos * JJA[::-1] / float(JJANUM)
    SON = cos * SON[::-1] / float(SONNUM)

    #print('DJF :')
    #print(DJF)
    #print('MAM :')
    #print(MAM)
    #print('JJA :')
    #print(JJA)
    #print('SON :')
    #print(SON)

    return DJF, MAM, JJA, SON



#seasonal('../../shift/output/JRA3Q/JRA3Q_1990_2020_ALL_VINT_SHIFT_az.grd', 6, 145, False)

