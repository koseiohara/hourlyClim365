def set_input_file(dataset, ini, fin, dim, var, flag, extension):
    output = '../../shift/output/{}/{}_{}_{}_ALL_{}_SHIFT_{}{}.{}'.format(dataset, dataset, ini, fin, dim, var, flag, extension)
    print('  << ' + output)

    return output


