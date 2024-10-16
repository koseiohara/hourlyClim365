import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker

from prepare        import prepare_clim as get
from get_timeseries import get_datetime
from set_input_file import set_input_file


def c_kz_ae_mkgrph(figname, title, timestep, dataset, ini, fin, flag):
    fig = plt.figure(figsize=[6,3])
    ax = fig.add_subplot(111)

    c_kz_ae_file = set_input_file(dataset, ini, fin, 'VINT', 'c_kz_ae', flag, 'grd')

    GM, NH, SH = plot_c_kz_ae_ax(ax=ax, filename=c_kz_ae_file, timestep=timestep, title=title)

    legend = ['Global', 'NH', 'SH']
    fig.legend([GM, NH, SH], legend, loc='upper center', bbox_to_anchor=[0.5, 0.02], ncol=3)

    fig.savefig(figname, dpi=350, bbox_inches='tight')

    print('  >> ' + figname)
    print('')


def plot_c_kz_ae_ax(ax, filename, timestep, title=''):

    ydigit = 1
    ymajorstep = 0.5

    date = get_datetime(leap=False, timestep=timestep)

    total = get(filename, 'VINT', -90., 90., timestep)
    north = get(filename, 'VINT',   0., 90., timestep)
    south = get(filename, 'VINT', -90.,  0., timestep)
    
    GM, = ax.plot(date,  total, color='black' , alpha=0.7)
    NH, = ax.plot(date,  north, color='blue'  , alpha=0.7)
    SH, = ax.plot(date,  south, color='red'   , alpha=0.7)

    ax.set_xlim(xmin=date[0], xmax=date[-1])
    ax.set_ylim(ymin=-.5, ymax=2.5)

    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[2,4,6,8,10,12], bymonthday=1))
    ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=1, bymonthday=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

    ax.yaxis.set_major_locator(mticker.MultipleLocator(ymajorstep))
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.{}f'.format(ydigit)))
    ax.yaxis.set_minor_locator(mticker.AutoMinorLocator(5))

    ax.grid(axis='both', which='major', linewidth=0.3)
    ax.grid(axis='both', which='minor', linewidth=0.1)
    ax.tick_params(labelsize=13)

    if (title != ''):
        ax.set_title(title, fontsize=13, y=0.98, va='bottom')

    return GM, NH, SH


