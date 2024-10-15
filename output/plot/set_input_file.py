def set_input_file(dataset, ini, fin, dim, var, flag, extension):
    output = '../{}/{}_{}_{}_ALL_{}_{}{}.{}'.format(dataset, dataset, ini, fin, dim, var, flag, extension)
    print('INPUT FILE : ' + output)

    return output


