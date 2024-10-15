import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker

from prepare        import prepare_clim as get
from get_timeseries import get_datetime
from set_input_file import set_input_file


def az_mkgrph(figname, title, timestep, flag):
    fig = plt.figure(figsize=[8,6])
    ax = fig.add_subplot(111)

    az_file = set_input_file('JRA3Q', 1990, 2020, 'VINT', 'az', flag, 'grd')

    GM, NH, SH, TR = plot_az_ax(ax=ax, filename=az_file, timestep=timestep, title=title)

    legend = ['Global', r'30$^\circ \mathrm{N}$-90$^\circ \mathrm{N}$', r'30$^\circ \mathrm{S}$-90$^\circ \mathrm{S}$', r'30$^\circ \mathrm{S}$-30$^\circ \mathrm{N}$']
    fig.legend([GM, NH, SH, TR], legend, loc='upper center', bbox_to_anchor=[0.5, 0.02], ncol=4)

    fig.savefig(figname, dpi=350, bbox_inches='tight')

    print('')
    print('  >> ' + figname)
    print('')


def plot_az_ax(ax, filename, timestep, title=''):

    ydigit = 1
    ymajorstep = 0.5

    date = get_datetime(leap=False, timestep=timestep)

    total = get(filename, 'VINT', -90.,  90., timestep) * 1.E-6
    north = get(filename, 'VINT',  30.,  90., timestep) * 1.E-6
    south = get(filename, 'VINT', -90., -30., timestep) * 1.E-6
    tropic= get(filename, 'VINT', -30.,  30., timestep) * 1.E-6
    
    GM, = ax.plot(date,  total, color='black' , alpha=0.7)
    NH, = ax.plot(date,  north, color='blue'  , alpha=0.7)
    SH, = ax.plot(date,  south, color='red'   , alpha=0.7)
    TR, = ax.plot(date, tropic, color='orange', alpha=0.7)

    ax.set_xlim(xmin=date[0], xmax=date[-1])
    ax.set_ylim(ymin=0., ymax=4.)

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

    return GM, NH, SH, TR


