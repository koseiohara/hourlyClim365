from set_file import set_ifile, set_ofile
from plot_qe  import plot_qe
from plot_qz  import plot_qz


DATA = 'JRA3Q'
BEG  = 1980
END  = 2023
EXTENSION = 'grd'


for FLAG in (['', '_QFILTER']):
    VAR = 'qe'
    sw = set_ifile(DATA, BEG, END, 'ttswr_'+VAR, FLAG, EXTENSION)
    lw = set_ifile(DATA, BEG, END, 'ttlwr_'+VAR, FLAG, EXTENSION)
    lr = set_ifile(DATA, BEG, END, 'lrghr_'+VAR, FLAG, EXTENSION)
    cn = set_ifile(DATA, BEG, END, 'cnvhr_'+VAR, FLAG, EXTENSION)
    vd = set_ifile(DATA, BEG, END, 'vdfhr_'+VAR, FLAG, EXTENSION)
    fig = set_ofile(DATA, BEG, END, VAR, FLAG)
    title = r'Diurnal Variation of $Q_E \: \left(\mathrm{W \: m^{-2}}\right)$'

    plot_qe(sw, lw, lr, cn, vd, fig, title)


    VAR = 'qz'
    sw = set_ifile(DATA, BEG, END, 'ttswr_'+VAR, FLAG, EXTENSION)
    lw = set_ifile(DATA, BEG, END, 'ttlwr_'+VAR, FLAG, EXTENSION)
    lr = set_ifile(DATA, BEG, END, 'lrghr_'+VAR, FLAG, EXTENSION)
    cn = set_ifile(DATA, BEG, END, 'cnvhr_'+VAR, FLAG, EXTENSION)
    vd = set_ifile(DATA, BEG, END, 'vdfhr_'+VAR, FLAG, EXTENSION)
    fig = set_ofile(DATA, BEG, END, VAR, FLAG)
    title = r'Diurnal Variation of $Q_Z \: \left(\mathrm{W \: m^{-2}}\right)$'

    plot_qz(sw, lw, lr, cn, vd, fig, title)

