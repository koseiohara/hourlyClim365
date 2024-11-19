def set_input_file(dataset, ini, fin, dim, var, flag, extension):
    if (flag != ''):
        flag = '_' + flag

    output = '../../shift/output/{}/{}_{}_{}_ALL_{}_SHIFT_{}{}.{}'.format(dataset, dataset, ini, fin, dim, var, flag, extension)
    print('  << ' + output)

    return output


def set_figname(data1, data2, ini, fin, var, flag1, flag2):
    if (flag1 == ''):
        flag1 = 'NOFLAG'
    if (flag2 == ''):
        flag2 = 'NOFLAG'

    output = './figs/{}_{}_{}_{}_{}_{}_{}.png'.format(data1, flag1, data2, flag2, ini, fin, var)
    print('  >> ' + output)

    return output


def set_title(data1, data2, var):
    output = 'Relative Change of ' + var + r'($\%$)'
    return output


