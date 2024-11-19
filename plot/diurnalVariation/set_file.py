

def set_ifile(data, year_beg, year_end, var, flags, extension):
    output = '../../shift/output/{}/{}_{}_{}_ALL_VINT_SHIFT_{}{}.{}'.format(data, data, year_beg, year_end, var, flags, extension)
    print('  << ' + output)

    return output


def set_ofile(data, year_beg, year_end, var, flags):
    output = 'figs/{}_{}_{}_{}{}.png'.format(data, year_beg, year_end, var, flags)
    print('  >> ' + output)

    return output


