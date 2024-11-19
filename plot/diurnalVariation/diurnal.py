import numpy as np

from filein     import filein
from vint2gmean import vint2gmean
from toSeasonal import toSeasonal


def diurnal(ifile, ny, isLeap, latstep, isYrev, range_south, range_north):

    reader = filein(filename = ifile   , \
                    shape    = [ny]    , \
                    recl     = 4*ny    , \
                    rec      = 1       , \
                    kind     = 4       , \
                    endian   = 'LITTLE', \
                    recstep  = 1         )

    if (isLeap):
        nt = 366 << 2
    else:
        nt = 365 << 2

    work_vint = np.empty(ny)
    gmean     = np.empty(nt)
    for t in range(nt):
        work_vint[:] = reader.fread()
        gmean[t] = vint2gmean(work_vint[:], latstep, isYrev, range_south, range_north)

    DJF, MAM, JJA, SON = toSeasonal(gmean[:], isLeap)

    return DJF, MAM, JJA, SON

