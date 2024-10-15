import numpy as np
import matplotlib.pyplot as plt

from plot_az import az_mkgrph
from plot_qe import qe_mkgrph
from plot_qz import qz_mkgrph



dataset = 'JRA3Q'
ini  = 1990
fin  = 2020
flag = ''


var   = 'az'
fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
title = r'Global Mean $A_Z \: \left(\mathrm{10^6 \: J \: m^{-2}}\right)$'
az_mkgrph(fig, title, 'daily', flag)


#var  = 'qe'
#fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
#title = r'Global Mean $Q_E \: \left(\mathrm{W \: m^{-2}}\right)$'
#qe_mkgrph(fig, title, 'daily', flag)
#
#
#var   = 'qz'
#fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
#title = r'Global Mean $Q_Z \: \left(\mathrm{W \: m^{-2}}\right)$'
#qz_mkgrph(fig, title, 'daily', flag)
#
#
#flag = '_QFILTER'
#
#var   = 'qe'
#fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
#title = r'Global Mean $Q_E \: \left(\mathrm{W \: m^{-2}}\right)$' + '\n12hr Moving Average of Diabatic Heating'
#qe_mkgrph(fig, title, 'daily', flag)
#
#
#var   = 'qz'
#fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
#title = r'Global Mean $Q_Z \: \left(\mathrm{W \: m^{-2}}\right)$' + '\n12hr Moving Average of Diabatic Heating'
#qz_mkgrph(fig, title, 'daily', flag)


