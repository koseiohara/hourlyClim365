

def get_ifile(dataset, year_beg, year_end, var, flags, extension):

    output = '../../shift/output/{}/{}_{}_{}_ALL_VINT_SHIFT_{}{}.{}'.format(dataset, dataset, year_beg, year_end, var, flags, extension)
    print('    << {}'.format(output))
    return output


def get_ofile(dataset, year_beg, year_end, var, flags, extension):

    output = 'figs/{}_{}_{}_clim_{}{}.{}'.format(dataset, year_beg, year_end, var, flags, extension)
    print('    >> {}\n'.format(output))
    return output

