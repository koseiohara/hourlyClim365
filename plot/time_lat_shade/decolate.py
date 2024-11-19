import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates  as mdates
import matplotlib.ticker as mticker
import datetime

#from filein import filein

def decolate(fig, ax, date, lat, shadeData, cmap, vmin, vmax, cbarform='%4.1f', title='', contlabel='', contour=False):

    lat_cosfilter = cosfilter(lat)
    dateField, latField = np.meshgrid(date, lat_cosfilter)

    cnum  = 40
    clevs = np.linspace(vmin, vmax, cnum+1)
    ticknum  = 4
    ticklevs = np.linspace(vmin, vmax, ticknum+1)
    cont = ax.contourf(dateField, latField, shadeData, cmap=cmap, levels=clevs, extend='both')

    if (contlabel == ''):
        cbar = fig.colorbar(cont, ax=ax, pad=0.01, aspect=12, ticks=ticklevs, format=cbarform)
    else:
        cbar = fig.colorbar(cont, ax=ax, pad=0.01, aspect=12, ticks=ticklevs, format=clabform, label=contlabel, labelsize=13)

    if (contour):
        scale = 4
        cnum  = scale * 2 
        clevs = np.linspace(scale*vmin, scale*vmax, cnum+1)
        ax.contour(dateField, latField, shadeData, colors='white', linewidths=0.5, levels=clevs)

    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[2,4,6,8,10,12], bymonthday=1))
    ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=1, bymonthday=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

    ylab_list = np.array([-90, -60, -30, 0, 30, 60, 90])
    ylab_cos  = cosfilter(ylab_list)
    ax.set_yticks(ylab_cos)
    ax.set_yticklabels(mklabels(ylab_list))

    ax.tick_params(labelsize=13)

    ax.set_title(title, fontsize=13)


def cosfilter(lat):
    return np.cos((lat-90.)*np.pi / 180.)


def mklabels(ylab):
    len = np.size(ylab)
    output = ['']*len

    for i in range(len):
        if (ylab[i] < 0):
            output[i] = '{:2d}S'.format(-ylab[i])
        elif (ylab[i] > 0):
            output[i] = '{:2d}N'.format(ylab[i])
        else:
            output[i] = 'EQ'

    return output


