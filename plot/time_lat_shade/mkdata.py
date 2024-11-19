import numpy as np
import datetime
from filein import filein


hstep = 6
days = 365
hrs = int(days * 24 / hstep)
def mkdata(fname, ny):
    inshape = [ny]
    ftype = filein(fname, inshape, 4*ny, 1, 4, 'LITTLE', 1)

    latdelta = np.pi / np.float64(ny-1)
    lat = np.arange(-0.5*np.pi, 0.5*np.pi+latdelta, latdelta)
    #cos = np.cos(lat)

    vint = np.empty([ny,hrs])

    for t in range(0, hrs):
        input_work = ftype.fread()
        #vint[:,t] = input_work[::-1]*cos
        vint[:,t] = input_work[::-1]

    return vint


def mkDateTime():
    initial_date = datetime.datetime(2001, 1, 1, 0)
    dateAndTime = [0]*hrs
    dateAndTime[0] = initial_date

    for h in range(1, hrs):
        dateAndTime[h] = dateAndTime[h-1] + datetime.timedelta(hours=hstep)

    return dateAndTime


