import numpy as np

from get_timeseries  import get_from_vint, get_from_gmean, get_datetime


def prepare_clim(filename, dim, south, north, timestep='hourly'):
    perday = 4
    nt = 365*perday

    if (dim.lower() == 'vint'):
        ny = 145
        dlat = 180./(ny-1)
        work = get_from_vint(fname=filename   , \
                             recl=4*ny        , \
                             rec=1            , \
                             kind=4           , \
                             endian='little'  , \
                             recstep=1        , \
                             ny=ny            , \
                             nt=nt            , \
                             latstep=dlat     , \
                             range_south=south, \
                             range_north=north  )
    elif (dim.lower() == 'gmean'):
        work = get_from_gmean(fname=filename , \
                              recl=4         , \
                              rec=1          , \
                              kind=4         , \
                              endian='little', \
                              recstep=1      , \
                              nt=nt            )

    if (timestep == 'daily'):
        nt = int(nt/perday)
        timeseries = np.empty(nt)
        for t in range(nt):
            timeseries[t] = np.mean(work[t*perday:t*perday+perday-1])
    elif (timestep == 'hourly'):
        timeseries = work
    else:
        print('---------------------------------------------')
        print('ERROR STOP')
        print('    Invalid timestep for', filename)
        print('---------------------------------------------')
        raise ValueError

    return timeseries


