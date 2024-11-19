import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from parameter import ny, range_south, range_north, latstep, isYrev, isLeap
from diurnal import diurnal


def plot_qz(sw_file, lw_file, lr_file, cn_file, vd_file, figname, title):

    sw_djf, sw_mam, sw_jja, sw_son = diurnal(sw_file, ny, isLeap, latstep, isYrev, range_south, range_north)
    lw_djf, lw_mam, lw_jja, lw_son = diurnal(lw_file, ny, isLeap, latstep, isYrev, range_south, range_north)
    lr_djf, lr_mam, lr_jja, lr_son = diurnal(lr_file, ny, isLeap, latstep, isYrev, range_south, range_north)
    cn_djf, cn_mam, cn_jja, cn_son = diurnal(cn_file, ny, isLeap, latstep, isYrev, range_south, range_north)
    vd_djf, vd_mam, vd_jja, vd_son = diurnal(vd_file, ny, isLeap, latstep, isYrev, range_south, range_north)

    tt_djf = sw_djf + lw_djf + lr_djf + cn_djf + vd_djf
    tt_mam = sw_mam + lw_mam + lr_mam + cn_mam + vd_mam
    tt_jja = sw_jja + lw_jja + lr_jja + cn_jja + vd_jja
    tt_son = sw_son + lw_son + lr_son + cn_son + vd_son

    xlab = ['00-06', '06-12', '12-18', '18-24']

    fig = plt.figure(figsize=[9,3])
    fig.subplots_adjust(wspace=0.25, hspace=0.6)
    tt = fig.add_subplot(231)
    sw = fig.add_subplot(232)
    lw = fig.add_subplot(233)
    lr = fig.add_subplot(234)
    cn = fig.add_subplot(235)
    vd = fig.add_subplot(236)

    djf, mam, jja, son = qz_ax(tt, xlab, tt_djf, tt_mam, tt_jja, tt_son, 'Total')
    qz_ax(sw, xlab, sw_djf, sw_mam, sw_jja, sw_son, 'Short Wave Radiation')
    qz_ax(lw, xlab, lw_djf, lw_mam, lw_jja, lw_son, 'Long Wave Radiation')
    qz_ax(lr, xlab, lr_djf, lr_mam, lr_jja, lr_son, 'Large Scale Condensation')
    qz_ax(cn, xlab, cn_djf, cn_mam, cn_jja, cn_son, 'Convective Heating')
    qz_ax(vd, xlab, vd_djf, vd_mam, vd_jja, vd_son, 'Vertical Diffusion')

    fig.suptitle(title, fontsize=12, y=0.98, va='bottom')
    fig.legend([djf, mam, jja, son], ['DJF', 'MAM', 'JJA', 'SON'], loc='upper center', bbox_to_anchor=[0.5,0.02], ncol=4)

    fig.savefig(figname, dpi=350, bbox_inches='tight')

    print('  ...COMPLETE\n')


def qz_ax(ax, xlab, DJF, MAM, JJA, SON, title=''):

    alpha = 0.7
    DJFline, = ax.plot(xlab, DJF, color='blue'       , alpha=alpha)
    MAMline, = ax.plot(xlab, MAM, color='sandybrown' , alpha=alpha)
    JJAline, = ax.plot(xlab, JJA, color='red'        , alpha=alpha)
    SONline, = ax.plot(xlab, SON, color='deepskyblue', alpha=alpha)

    ax.set_ylim(ymin=-5., ymax=5.)

    ax.yaxis.set_major_locator(mticker.MultipleLocator(2.5))
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.{}f'.format(1)))
    ax.yaxis.set_minor_locator(mticker.AutoMinorLocator(5))

    ax.grid(axis='both', which='major', linewidth=0.3)
    ax.grid(axis='both', which='minor', linewidth=0.1)

    ax.tick_params(labelsize=12)

    if (title != ''):
        ax.set_title(title, fontsize=12, y=0.98, va='bottom')

    ax.axhline(y=0, color='black', linewidth=0.5)

    return DJFline, MAMline, JJAline, SONline


