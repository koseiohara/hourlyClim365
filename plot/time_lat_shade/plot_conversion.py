import numpy as np
import matplotlib.pyplot as plt

from mkdata   import mkdata
from decolate import decolate


convmin = -5.
convmax =  5.

def plot_c_az_kz(ifile, ofile, ny, date, lat, title=r'$C\left(A_Z, K_Z\right) \: (\mathrm{W \: m^{-2}})$'):
    input = mkdata(ifile, ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'coolwarm', convmin, convmax, title=title)

    fig.savefig(ofile, dpi=350, bbox_inches='tight')
    plt.close(fig)


def plot_c_kz_ae(ifile, ofile, ny, date, lat, title=r'$C\left(K_Z, A_E\right) \: (\mathrm{W \: m^{-2}})$'):
    input = mkdata(ifile, ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'coolwarm', convmin, convmax, title=title)

    fig.savefig(ofile, dpi=350, bbox_inches='tight')
    plt.close(fig)


def plot_c_kz_ke(ifile, ofile, ny, date, lat, title=r'$C\left(K_Z, K_E\right) \: (\mathrm{W \: m^{-2}})$'):
    input = mkdata(ifile, ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'coolwarm', convmin, convmax, title=title)

    fig.savefig(ofile, dpi=350, bbox_inches='tight')
    plt.close(fig)


def plot_c_kz_w(ae_ifile, ke_ifile, ofile, ny, date, lat, title=r'$C\left(K_Z, W\right) \: (\mathrm{W \: m^{-2}})$'):
    ae_input = mkdata(ae_ifile, ny)
    ke_input = mkdata(ke_ifile, ny)
    c_kz_w = ae_input + ke_input

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, c_kz_w, 'coolwarm', convmin, convmax, title=title)

    fig.savefig(ofile, dpi=350, bbox_inches='tight')
    plt.close(fig)


