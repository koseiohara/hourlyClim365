import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker

from prepare        import prepare_clim as get
from get_timeseries import get_datetime
from set_input_file import set_input_file


def qe_mkgrph(figname, title, timestep, flag):
    fig = plt.figure(figsize=[9,3])
    fig.subplots_adjust(wspace=0.25, hspace=0.6)
    total = fig.add_subplot(231)
    ttswr = fig.add_subplot(232)
    ttlwr = fig.add_subplot(233)
    lrghr = fig.add_subplot(234)
    cnvhr = fig.add_subplot(235)
    vdfhr = fig.add_subplot(236)

    total_file = set_input_file('JRA3Q', 1990, 2020, 'VINT',       'qe', flag, 'grd')
    ttswr_file = set_input_file('JRA3Q', 1990, 2020, 'VINT', 'ttswr_qe', flag, 'grd')
    ttlwr_file = set_input_file('JRA3Q', 1990, 2020, 'VINT', 'ttlwr_qe', flag, 'grd')
    lrghr_file = set_input_file('JRA3Q', 1990, 2020, 'VINT', 'lrghr_qe', flag, 'grd')
    cnvhr_file = set_input_file('JRA3Q', 1990, 2020, 'VINT', 'cnvhr_qe', flag, 'grd')
    vdfhr_file = set_input_file('JRA3Q', 1990, 2020, 'VINT', 'vdfhr_qe', flag, 'grd')

    GM, NH, SH = plot_qe_ax(ax=total, filename=total_file, timestep=timestep, title='Total'                   )
    plot_qe_ax(ax=ttswr, filename=ttswr_file, timestep=timestep, title='Short Wave Radiation'    )
    plot_qe_ax(ax=ttlwr, filename=ttlwr_file, timestep=timestep, title='Long Wave Radiation'     )
    plot_qe_ax(ax=lrghr, filename=lrghr_file, timestep=timestep, title='Large Scale Condensation')
    plot_qe_ax(ax=cnvhr, filename=cnvhr_file, timestep=timestep, title='Convective Heating'      )
    plot_qe_ax(ax=vdfhr, filename=vdfhr_file, timestep=timestep, title='Vertical Diffusion'      )

    fig.suptitle(title, fontsize=12, y=0.98, va='bottom')
    fig.legend([GM, NH, SH], ['Global', 'NH', 'SH'], loc='upper center', bbox_to_anchor=[0.5, 0.02], ncol=3)

    fig.savefig(figname, dpi=350, bbox_inches='tight')

    print('')
    print('  >> ' + figname)
    print('')


def plot_qe_ax(ax, filename, timestep, title=''):

    ydigit = 1
    ymajorstep = 0.5

    date = get_datetime(leap=False, timestep=timestep)

    total = get(filename, 'VINT', -90., 90., timestep)
    north = get(filename, 'VINT',   0., 90., timestep)
    south = get(filename, 'VINT', -90.,  0., timestep)

    #GM = ax.plot(date, total, color='black', label='Global')
    #NH = ax.plot(date, north, color='blue' , label='NH'    )
    #SH = ax.plot(date, south, color='red'  , label='SH'    )
    GM, = ax.plot(date, total, color='black', alpha=0.8)
    NH, = ax.plot(date, north, color='blue' , alpha=0.8)
    SH, = ax.plot(date, south, color='red'  , alpha=0.8)

    ax.set_xlim(xmin=date[0], xmax=date[-1])
    ax.set_ylim(ymin=-0.5, ymax=1.5)

    #ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2, bymonthday=1))
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[2,4,6,8,10,12], bymonthday=1))
    ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=1, bymonthday=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

    ax.yaxis.set_major_locator(mticker.MultipleLocator(ymajorstep))
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.{}f'.format(ydigit)))
    ax.yaxis.set_minor_locator(mticker.AutoMinorLocator(5))

    ax.grid(axis='both', which='major', linewidth=0.3)
    ax.grid(axis='both', which='minor', linewidth=0.1)
    ax.tick_params(labelsize=10)

    if (title != ''):
        ax.set_title(title, fontsize=10, y=0.97)

    return GM, NH, SH


