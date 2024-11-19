import numpy as np
import matplotlib.pyplot as plt

from mkdata   import mkdata
from decolate import decolate


qemin = -3.
qemax =  3.

def plot_qe(ifile, ofile, ny, date, lat, title=r'$Q_E \: (\mathrm{W \: m^{-2}})$'):
    input = mkdata(ifile, ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'coolwarm', qemin, qemax, title=title)

    fig.savefig(ofile, dpi=350, bbox_inches='tight')
    plt.close(fig)


def plot_qe_total(sw_ifile, lw_ifile, lr_ifile, cn_ifile, vd_ifile, ofile, ny, date, lat, title=r'$Q_E \: (\mathrm{W \: m^{-2}})$'):
    sw_input = mkdata(sw_ifile, ny)
    lw_input = mkdata(lw_ifile, ny)
    lr_input = mkdata(lr_ifile, ny)
    cn_input = mkdata(cn_ifile, ny)
    vd_input = mkdata(vd_ifile, ny)
    total = sw_input + lw_input + lr_input + cn_input + vd_input

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, total, 'coolwarm', qemin, qemax, title=title)

    fig.savefig(ofile, dpi=350, bbox_inches='tight')
    plt.close(fig)


