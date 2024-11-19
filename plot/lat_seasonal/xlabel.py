import numpy as np

def xlabel(lablat):
    len = np.size(lablat)
    lab = ['']*len

    for i in range(len):
        if (lablat[i] < 0):
            lab[i] = '{:2d}S'.format(-lablat[i])
        elif (lablat[i] > 0):
            lab[i] = '{:2d}N'.format(lablat[i])
        else:
            lab[i] = 'EQ'

    return lab

