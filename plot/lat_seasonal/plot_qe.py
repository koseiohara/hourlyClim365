import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from set_input_file import set_input_file
from seasonal       import seasonal
from xlabel         import xlabel

def qe_mkgrph(figname, title, dataset, ini, fin, flag):

    ifiletot = set_input_file(dataset, ini, fin, 'VINT',       'qe', flag, 'grd')
    ifiletts = set_input_file(dataset, ini, fin, 'VINT', 'ttswr_qe', flag, 'grd')
    ifilettl = set_input_file(dataset, ini, fin, 'VINT', 'ttlwr_qe', flag, 'grd')
    ifilelrg = set_input_file(dataset, ini, fin, 'VINT', 'lrghr_qe', flag, 'grd')
    ifilecnv = set_input_file(dataset, ini, fin, 'VINT', 'cnvhr_qe', flag, 'grd')
    ifilevdf = set_input_file(dataset, ini, fin, 'VINT', 'vdfhr_qe', flag, 'grd')

    DJFtot, MAMtot, JJAtot, SONtot = seasonal(filename=ifiletot, hourstep=6, ny=145, leap=False)
    DJFtts, MAMtts, JJAtts, SONtts = seasonal(filename=ifiletts, hourstep=6, ny=145, leap=False)
    DJFttl, MAMttl, JJAttl, SONttl = seasonal(filename=ifilettl, hourstep=6, ny=145, leap=False)
    DJFlrg, MAMlrg, JJAlrg, SONlrg = seasonal(filename=ifilelrg, hourstep=6, ny=145, leap=False)
    DJFcnv, MAMcnv, JJAcnv, SONcnv = seasonal(filename=ifilecnv, hourstep=6, ny=145, leap=False)
    DJFvdf, MAMvdf, JJAvdf, SONvdf = seasonal(filename=ifilevdf, hourstep=6, ny=145, leap=False)

    fig = plt.figure(figsize=[9,3])
    fig.subplots_adjust(wspace=0.25, hspace=0.6)

    total = fig.add_subplot(231)
    ttswr = fig.add_subplot(232)
    ttlwr = fig.add_subplot(233)
    lrghr = fig.add_subplot(234)
    cnvhr = fig.add_subplot(235)
    vdfhr = fig.add_subplot(236)
    
    DJFline, MAMline, JJAline, SONline = qe_ax(total, DJFtot, MAMtot, JJAtot, SONtot, 'Total', 1, 1.)
    qe_ax(ttswr, DJFtts, MAMtts, JJAtts, SONtts, 'Short Wave Radiation'    , 1, 1.)
    qe_ax(ttlwr, DJFttl, MAMttl, JJAttl, SONttl, 'Long Wave Radiation'     , 1, 1.)
    qe_ax(lrghr, DJFlrg, MAMlrg, JJAlrg, SONlrg, 'Large Scale Condensation', 1, 1.)
    qe_ax(cnvhr, DJFcnv, MAMcnv, JJAcnv, SONcnv, 'Convective Heating'      , 1, 1.)
    qe_ax(vdfhr, DJFvdf, MAMvdf, JJAvdf, SONvdf, 'Vertical Diffusion'      , 1, 1.)

    fig.suptitle(title, fontsize=12, y=0.98, va='bottom')
    fig.legend([DJFline, MAMline, JJAline, SONline], ['DJF', 'MAM', 'JJA', 'SON'], loc='upper center', bbox_to_anchor=[0.5,0.02], ncol=4)

    fig.savefig(figname, dpi=350, bbox_inches='tight')

    print('  >> ' + figname)
    print('')


def qe_ax(ax, DJF, MAM, JJA, SON, title='', ydigit=0, ymajorstep=2.):

    lat = np.linspace(-90., 90., 145)

    alpha = 0.7
    DJFline, = ax.plot(lat, DJF, color='blue'       , alpha=alpha)
    MAMline, = ax.plot(lat, MAM, color='sandybrown' , alpha=alpha)
    JJAline, = ax.plot(lat, JJA, color='red'        , alpha=alpha)
    SONline, = ax.plot(lat, SON, color='deepskyblue', alpha=alpha)

    ax.set_xlim(xmin=lat[0], xmax=lat[-1])
    ax.set_ylim(ymin=-1., ymax=3.)

    lablat = np.array([-90, -45, 0, 45, 90])
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

