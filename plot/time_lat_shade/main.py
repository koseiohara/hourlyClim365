import numpy as np
import datetime

from get_filename    import get_ifile   , get_ofile
from mkdata          import mkDateTime
from plot_energy     import plot_az     , plot_kz      , plot_ae     , plot_ke    , plot_w
from plot_conversion import plot_c_az_kz, plot_c_kz_ae , plot_c_kz_ke, plot_c_kz_w
from plot_qe         import plot_qe     , plot_qe_total
from plot_qz         import plot_qz     , plot_qz_total


data      = 'JRA3Q'
year_beg  = 1980
year_end  = 2023
flags     = ''
extension = 'grd'

ny = 145
lat = np.linspace(-90., 90., ny)

date = mkDateTime()

var = 'az'
ifile = get_ifile(data, year_beg, year_end, var, flags, extension)
ofile = get_ofile(data, year_beg, year_end, var, flags,     'png')
plot_az(ifile, ofile, ny, date, lat)

var = 'kz'
ifile = get_ifile(data, year_beg, year_end, var, flags, extension)
ofile = get_ofile(data, year_beg, year_end, var, flags,     'png')
plot_kz(ifile, ofile, ny, date, lat)

var = 'ae'
ifile = get_ifile(data, year_beg, year_end, var, flags, extension)
ofile = get_ofile(data, year_beg, year_end, var, flags,     'png')
plot_ae(ifile, ofile, ny, date, lat)

var = 'ke'
ifile = get_ifile(data, year_beg, year_end, var, flags, extension)
ofile = get_ofile(data, year_beg, year_end, var, flags,     'png')
plot_ke(ifile, ofile, ny, date, lat)

var = 'w'
ae_ifile = get_ifile(data, year_beg, year_end, 'ae', flags, extension)
ke_ifile = get_ifile(data, year_beg, year_end, 'ke', flags, extension)
ofile    = get_ofile(data, year_beg, year_end,  var, flags,     'png')
plot_w(ae_ifile, ke_ifile, ofile, ny, date, lat)

var = 'c_az_kz'
ifile = get_ifile(data, year_beg, year_end, var, flags, extension)
ofile = get_ofile(data, year_beg, year_end, var, flags,     'png')
plot_c_az_kz(ifile, ofile, ny, date, lat)

var = 'c_kz_ae'
ifile = get_ifile(data, year_beg, year_end, var, flags, extension)
ofile = get_ofile(data, year_beg, year_end, var, flags,     'png')
plot_c_kz_ae(ifile, ofile, ny, date, lat)

var = 'c_kz_ke'
ifile = get_ifile(data, year_beg, year_end, var, flags, extension)
ofile = get_ofile(data, year_beg, year_end, var, flags,     'png')
plot_c_kz_ke(ifile, ofile, ny, date, lat)

var = 'c_kz_w'
ae_ifile = get_ifile(data, year_beg, year_end, 'c_kz_ae', flags, extension)
ke_ifile = get_ifile(data, year_beg, year_end, 'c_kz_ke', flags, extension)
ofile    = get_ofile(data, year_beg, year_end,       var, flags,     'png')
plot_c_kz_w(ae_ifile, ke_ifile, ofile, ny, date, lat)


for types in ['', '_QFILTER']:

    var = 'ttswr_qe'
    ifile = get_ifile(data, year_beg, year_end, var, types, extension)
    ofile = get_ofile(data, year_beg, year_end, var, types,     'png')
    plot_qe(ifile, ofile, ny, date, lat, title=r'$Q_E$ by Short Wave Radiation $(\mathrm{W \: m^{-2}})$')

    var = 'ttlwr_qe'
    ifile = get_ifile(data, year_beg, year_end, var, types, extension)
    ofile = get_ofile(data, year_beg, year_end, var, types,     'png')
    plot_qe(ifile, ofile, ny, date, lat, title=r'$Q_E$ by Long Wave Radiation $(\mathrm{W \: m^{-2}})$')

    var = 'lrghr_qe'
    ifile = get_ifile(data, year_beg, year_end, var, types, extension)
    ofile = get_ofile(data, year_beg, year_end, var, types,     'png')
    plot_qe(ifile, ofile, ny, date, lat, title=r'$Q_E$ by Large Scale Condensation $(\mathrm{W \: m^{-2}})$')

    var = 'cnvhr_qe'
    ifile = get_ifile(data, year_beg, year_end, var, types, extension)
    ofile = get_ofile(data, year_beg, year_end, var, types,     'png')
    plot_qe(ifile, ofile, ny, date, lat, title=r'$Q_E$ by Convective Heating $(\mathrm{W \: m^{-2}})$')

    var = 'vdfhr_qe'
    ifile = get_ifile(data, year_beg, year_end, var, types, extension)
    ofile = get_ofile(data, year_beg, year_end, var, types,     'png')
    plot_qe(ifile, ofile, ny, date, lat, title=r'$Q_E$ by Vertical Diffusion $(\mathrm{W \: m^{-2}})$')

    var = 'qe'
    ttswr = get_ifile(data, year_beg, year_end, 'ttswr_qe', types, extension)
    ttlwr = get_ifile(data, year_beg, year_end, 'ttlwr_qe', types, extension)
    lrghr = get_ifile(data, year_beg, year_end, 'lrghr_qe', types, extension)
    cnvhr = get_ifile(data, year_beg, year_end, 'cnvhr_qe', types, extension)
    vdfhr = get_ifile(data, year_beg, year_end, 'vdfhr_qe', types, extension)
    ofile = get_ofile(data, year_beg, year_end,        var, types,     'png')
    plot_qe_total(ttswr, ttlwr, lrghr, cnvhr, vdfhr, ofile, ny, date, lat, title=r'$Q_E$ $(\mathrm{W \: m^{-2}})$')

    var = 'ttswr_qz'
    ifile = get_ifile(data, year_beg, year_end, var, types, extension)
    ofile = get_ofile(data, year_beg, year_end, var, types,     'png')
    plot_qz(ifile, ofile, ny, date, lat, title=r'$Q_Z$ by Short Wave Radiation $(\mathrm{W \: m^{-2}})$')

    var = 'ttlwr_qz'
    ifile = get_ifile(data, year_beg, year_end, var, types, extension)
    ofile = get_ofile(data, year_beg, year_end, var, types,     'png')
    plot_qz(ifile, ofile, ny, date, lat, title=r'$Q_Z$ by Long Wave Radiation $(\mathrm{W \: m^{-2}})$')

    var = 'lrghr_qz'
    ifile = get_ifile(data, year_beg, year_end, var, types, extension)
    ofile = get_ofile(data, year_beg, year_end, var, types,     'png')
    plot_qz(ifile, ofile, ny, date, lat, title=r'$Q_Z$ by Large Scale Condensation $(\mathrm{W \: m^{-2}})$')

    var = 'cnvhr_qz'
    ifile = get_ifile(data, year_beg, year_end, var, types, extension)
    ofile = get_ofile(data, year_beg, year_end, var, types,     'png')
    plot_qz(ifile, ofile, ny, date, lat, title=r'$Q_Z$ by Convective Heating $(\mathrm{W \: m^{-2}})$')

    var = 'vdfhr_qz'
    ifile = get_ifile(data, year_beg, year_end, var, types, extension)
    ofile = get_ofile(data, year_beg, year_end, var, types,     'png')
    plot_qz(ifile, ofile, ny, date, lat, title=r'$Q_Z$ by Vertical Diffusion $(\mathrm{W \: m^{-2}})$')

    var = 'qz'
    ttswr = get_ifile(data, year_beg, year_end, 'ttswr_qz', types, extension)
    ttlwr = get_ifile(data, year_beg, year_end, 'ttlwr_qz', types, extension)
    lrghr = get_ifile(data, year_beg, year_end, 'lrghr_qz', types, extension)
    cnvhr = get_ifile(data, year_beg, year_end, 'cnvhr_qz', types, extension)
    vdfhr = get_ifile(data, year_beg, year_end, 'vdfhr_qz', types, extension)
    ofile = get_ofile(data, year_beg, year_end,        var, types,     'png')
    plot_qz_total(ttswr, ttlwr, lrghr, cnvhr, vdfhr, ofile, ny, date, lat, title=r'$Q_Z$ $(\mathrm{W \: m^{-2}})$')





