import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from set_input_file import set_input_file
from seasonal       import seasonal
from xlabel         import xlabel

def az_mkgrph(figname, title, dataset, ini, fin, flag):

    ifile = set_input_file(dataset, ini, fin, 'VINT', 'az', flag, 'grd')
    DJF, MAM, JJA, SON = seasonal(filename=ifile, hourstep=6, ny=145, leap=False)

    fig = plt.figure(figsize=[6,3])
    ax = fig.add_subplot(111)
    DJFline, MAMline, JJAline, SONline = az_ax(ax, DJF, MAM, JJA, SON, title, 1, 1.)

    fig.legend([DJFline, MAMline, JJAline, SONline], ['DJF', 'MAM', 'JJA', 'SON'], loc='upper center', bbox_to_anchor=[0.5,0.02], ncol=4)

    fig.savefig(figname, dpi=350, bbox_inches='tight')

    print('  >> ' + figname)
    print('')


def az_ax(ax, DJF, MAM, JJA, SON, title='', ydigit=0, ymajorstep=2.):

    lat = np.linspace(-90., 90., 145)

    alpha = 0.7
    DJFline, = ax.plot(lat, DJF*1.E-6, color='blue'       , alpha=alpha)
    MAMline, = ax.plot(lat, MAM*1.E-6, color='sandybrown' , alpha=alpha)
    JJAline, = ax.plot(lat, JJA*1.E-6, color='red'        , alpha=alpha)
    SONline, = ax.plot(lat, SON*1.E-6, color='deepskyblue', alpha=alpha)

    ax.set_xlim(xmin=lat[0], xmax=lat[-1])
    ax.set_ylim(ymin=0., ymax=7.)

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
