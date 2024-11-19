import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from set_string import set_input_file, set_figname, set_title
from seasonal   import seasonal
from xlabel     import xlabel

def qe_mkgrph(ini, fin, data1, data2, flag1, flag2):

    var = 'qe'
    var_tex = r'$Q_Z$'

    fig = plt.figure(figsize=[9,3])
    fig.subplots_adjust(wspace=0.25, hspace=0.6)

    axtot = fig.add_subplot(2,3,1)
    axtts = fig.add_subplot(2,3,2)
    axttl = fig.add_subplot(2,3,3)
    axlrg = fig.add_subplot(2,3,4)
    axcnv = fig.add_subplot(2,3,5)
    axvdf = fig.add_subplot(2,3,6)
    axes = [axtot, axtts, axttl, axlrg, axcnv, axvdf]

    elements = [var, 'ttswr_'+var, 'ttlwr_'+var, 'lrghr_'+var, 'cnvhr_'+var, 'vdfhr_'+var]
    titles   = ['Total', 'Short Wave Radiation', 'Long Wave Radiation', 'Large Scale Condensation', 'Convective Heating', 'Vertical Diffusion']

    for i in range(6):
        ifile1 = set_input_file(data1, ini, fin, 'VINT', elements[i], flag1, 'grd')
        ifile2 = set_input_file(data2, ini, fin, 'VINT', elements[i], flag2, 'grd')
        DJF1, MAM1, JJA1, SON1 = seasonal(filename=ifile1, hourstep=6, ny=145, leap=False)
        DJF2, MAM2, JJA2, SON2 = seasonal(filename=ifile2, hourstep=6, ny=145, leap=False)
        DJF = 100. * (DJF1-DJF2) / DJF2
        MAM = 100. * (MAM1-MAM2) / MAM2
        JJA = 100. * (JJA1-JJA2) / JJA2
        SON = 100. * (SON1-SON2) / SON2

        #DJF = DJF1-DJF2
        #MAM = MAM1-MAM2
        #JJA = JJA1-JJA2
        #SON = SON1-SON2

        DJFline, MAMline, JJAline, SONline = qe_ax(axes[i], DJF, MAM, JJA, SON, titles[i], 1, 25.)

    title = set_title(data1, data2, var_tex)
    fig.suptitle(title, fontsize=12, y=0.98, va='bottom')
    fig.legend([DJFline, MAMline, JJAline, SONline], ['DJF', 'MAM', 'JJA', 'SON'], loc='upper center', bbox_to_anchor=[0.5,0.02], ncol=4)

    figname = set_figname(data1, data2, ini, fin, var, flag1, flag2)
    fig.savefig(figname, dpi=350, bbox_inches='tight')

    print('  COMPLETE')
    print('')


def qe_ax(ax, DJF, MAM, JJA, SON, title='', ydigit=0, ymajorstep=2.):

    lat = np.linspace(-90., 90., 145)

    alpha = 0.7
    DJFline, = ax.plot(lat, DJF, color='blue'       , alpha=alpha)
    MAMline, = ax.plot(lat, MAM, color='sandybrown' , alpha=alpha)
    JJAline, = ax.plot(lat, JJA, color='red'        , alpha=alpha)
    SONline, = ax.plot(lat, SON, color='deepskyblue', alpha=alpha)

    ax.set_xlim(xmin=lat[0], xmax=lat[-1])
    ax.set_ylim(ymin=-100., ymax=100.)

    lablat = np.array([-90, -60, -30, 0, 30, 60, 90])
    lab = xlabel(lablat)
    ax.set_xticks(lablat)
    ax.set_xticklabels(lab)

    ax.yaxis.set_major_locator(mticker.MultipleLocator(ymajorstep))
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.{}f'.format(ydigit)))
    ax.yaxis.set_minor_locator(mticker.AutoMinorLocator(5))

    ax.grid(axis='both', which='major', linewidth=0.3)
    ax.grid(axis='both', which='minor', linewidth=0.1)
    ax.tick_params(labelsize=10)

    ax.axhline(y=0, color='black', linewidth=0.5)

    if (title != ''):
        ax.set_title(title, fontsize=10, y=0.98, va='bottom')

    return DJFline, MAMline, JJAline, SONline

