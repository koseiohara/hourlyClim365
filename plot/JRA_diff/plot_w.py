import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from set_string import set_input_file, set_figname, set_title
from seasonal   import seasonal
from xlabel     import xlabel

def w_mkgrph(ini, fin, data1, data2, flag1, flag2):

    var = 'w'
    var_tex = r'$W$'

    ifile1_ae = set_input_file(data1, ini, fin, 'VINT', 'ae', flag1, 'grd')
    ifile2_ae = set_input_file(data2, ini, fin, 'VINT', 'ae', flag2, 'grd')
    ifile1_ke = set_input_file(data1, ini, fin, 'VINT', 'ke', flag1, 'grd')
    ifile2_ke = set_input_file(data2, ini, fin, 'VINT', 'ke', flag2, 'grd')

    DJF1_ae, MAM1_ae, JJA1_ae, SON1_ae = seasonal(filename=ifile1_ae, hourstep=6, ny=145, leap=False)
    DJF2_ae, MAM2_ae, JJA2_ae, SON2_ae = seasonal(filename=ifile2_ae, hourstep=6, ny=145, leap=False)
    DJF1_ke, MAM1_ke, JJA1_ke, SON1_ke = seasonal(filename=ifile1_ke, hourstep=6, ny=145, leap=False)
    DJF2_ke, MAM2_ke, JJA2_ke, SON2_ke = seasonal(filename=ifile2_ke, hourstep=6, ny=145, leap=False)

    DJF1 = DJF1_ae + DJF1_ke
    MAM1 = MAM1_ae + MAM1_ke
    JJA1 = JJA1_ae + JJA1_ke
    SON1 = SON1_ae + SON1_ke

    DJF2 = DJF2_ae + DJF2_ke
    MAM2 = MAM2_ae + MAM2_ke
    JJA2 = JJA2_ae + JJA2_ke
    SON2 = SON2_ae + SON2_ke

    DJF = 100. * (DJF1-DJF2) / DJF2
    MAM = 100. * (MAM1-MAM2) / MAM2
    JJA = 100. * (JJA1-JJA2) / JJA2
    SON = 100. * (SON1-SON2) / SON2

    figname = set_figname(data1, data2, ini, fin, var, flag1, flag2)

    #title = '{}/{} '.format(data1, data2) + r'$A_Z\%$'
    title = set_title(data1, data2, var_tex)

    fig = plt.figure(figsize=[6,3])
    ax = fig.add_subplot(111)
    DJFline, MAMline, JJAline, SONline = w_ax(ax, DJF, MAM, JJA, SON, title, 1, 5.)

    fig.legend([DJFline, MAMline, JJAline, SONline], ['DJF', 'MAM', 'JJA', 'SON'], loc='upper center', bbox_to_anchor=[0.5,0.02], ncol=4)

    fig.savefig(figname, dpi=350, bbox_inches='tight')

    print('  COMPLETE')
    print('')


def w_ax(ax, DJF, MAM, JJA, SON, title='', ydigit=0, ymajorstep=2.):

    lat = np.linspace(-90., 90., 145)

    alpha = 0.7
    DJFline, = ax.plot(lat, DJF, color='blue'       , alpha=alpha)
    MAMline, = ax.plot(lat, MAM, color='sandybrown' , alpha=alpha)
    JJAline, = ax.plot(lat, JJA, color='red'        , alpha=alpha)
    SONline, = ax.plot(lat, SON, color='deepskyblue', alpha=alpha)

    ax.set_xlim(xmin=lat[0], xmax=lat[-1])
    ax.set_ylim(ymin=-15., ymax=15.)

    lablat = np.array([-90, -60, -30, 0, 30, 60, 90])
    lab = xlabel(lablat)
    ax.set_xticks(lablat)
    ax.set_xticklabels(lab)

    ax.yaxis.set_major_locator(mticker.MultipleLocator(ymajorstep))
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.{}f'.format(ydigit)))
    ax.yaxis.set_minor_locator(mticker.AutoMinorLocator(5))

    ax.grid(axis='both', which='major', linewidth=0.3)
    ax.grid(axis='both', which='minor', linewidth=0.1)
    ax.tick_params(labelsize=13)

    ax.axhline(y=0, color='black', linewidth=0.5)

    if (title != ''):
        ax.set_title(title, fontsize=13, y=0.98, va='bottom')

    return DJFline, MAMline, JJAline, SONline
