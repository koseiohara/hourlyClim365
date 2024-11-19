import numpy as np
import matplotlib.pyplot as plt

from mkdata   import mkdata
from decolate import decolate


enmin = 0.
enmax = 8.

def plot_az(ifile, ofile, ny, date, lat, title=r'$A_Z \: (10^6 \:\mathrm{J \: m^{-2}})$'):
    input = mkdata(ifile, ny) * 1.E-6

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'Reds', enmin, enmax, title=title, contour=True)

    fig.savefig(ofile, dpi=350, bbox_inches='tight')
    plt.close(fig)


def plot_kz(ifile, ofile, ny, date, lat, title=r'$K_Z \: (10^6 \:\mathrm{J \: m^{-2}})$'):
    input = mkdata(ifile, ny) * 1.E-6

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'Reds', enmin, enmax, title=title)

    fig.savefig(ofile, dpi=350, bbox_inches='tight')
    plt.close(fig)


def plot_ae(ifile, ofile, ny, date, lat, title=r'$A_E \: (10^6 \:\mathrm{J \: m^{-2}})$'):
    input = mkdata(ifile, ny) * 1.E-6

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'Reds', enmin, enmax, title=title)

    fig.savefig(ofile, dpi=350, bbox_inches='tight')
    plt.close(fig)


def plot_ke(ifile, ofile, ny, date, lat, title=r'$K_E \: (10^6 \:\mathrm{J \: m^{-2}})$'):
    input = mkdata(ifile, ny) * 1.E-6

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'Reds', enmin, enmax, title=title)

    fig.savefig(ofile, dpi=350, bbox_inches='tight')
    plt.close(fig)


def plot_w(ae_ifile, ke_ifile, ofile, ny, date, lat, title=r'$W \: (10^6 \:\mathrm{J \: m^{-2}})$'):
    ae_input = mkdata(ae_ifile, ny) * 1.E-6
    ke_input = mkdata(ke_ifile, ny) * 1.E-6
    w = ae_input + ke_input

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, w, 'Reds', enmin, enmax, title=title)

    fig.savefig(ofile, dpi=350, bbox_inches='tight')
    plt.close(fig)


