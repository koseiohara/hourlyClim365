#import numpy as np
#import matplotlib.pyplot as plt

from plot_az      import az_mkgrph
from plot_kz      import kz_mkgrph
from plot_ae      import ae_mkgrph
from plot_ke      import ke_mkgrph
from plot_w       import  w_mkgrph
from plot_c_az_kz import c_az_kz_mkgrph
from plot_c_kz_ae import c_kz_ae_mkgrph
from plot_c_ke_kz import c_ke_kz_mkgrph
from plot_c_kz_w  import c_kz_w_mkgrph
from plot_qe      import qe_mkgrph
from plot_qz      import qz_mkgrph



dataset = 'JRA3Q'
ini  = 1990
fin  = 2020
timestep = 'hourly'
flag = ''


var   = 'az'
fig   = './figs/{}_{}_{}_{}_{}{}.png'.format(dataset, ini, fin, timestep, var, flag)
title = r'Global Mean $A_Z \: \left(\mathrm{10^6 \: J \: m^{-2}}\right)$'
az_mkgrph(fig, title, timestep, dataset, ini, fin, flag)


var   = 'kz'
fig   = './figs/{}_{}_{}_{}_{}{}.png'.format(dataset, ini, fin, timestep, var, flag)
title = r'Global Mean $K_Z \: \left(\mathrm{10^6 \: J \: m^{-2}}\right)$'
kz_mkgrph(fig, title, timestep, dataset, ini, fin, flag)


var   = 'ae'
fig   = './figs/{}_{}_{}_{}_{}{}.png'.format(dataset, ini, fin, timestep, var, flag)
title = r'Global Mean $A_E \: \left(\mathrm{10^6 \: J \: m^{-2}}\right)$'
ae_mkgrph(fig, title, timestep, dataset, ini, fin, flag)


var   = 'ke'
fig   = './figs/{}_{}_{}_{}_{}{}.png'.format(dataset, ini, fin, timestep, var, flag)
title = r'Global Mean $K_E \: \left(\mathrm{10^6 \: J \: m^{-2}}\right)$'
ke_mkgrph(fig, title, timestep, dataset, ini, fin, flag)


var   = 'w'
fig   = './figs/{}_{}_{}_{}_{}{}.png'.format(dataset, ini, fin, timestep, var, flag)
title = r'Global Mean $W \: \left(\mathrm{10^6 \: J \: m^{-2}}\right)$'
w_mkgrph(fig, title, timestep, dataset, ini, fin, flag)


var   = 'c_az_kz'
fig   = './figs/{}_{}_{}_{}_{}{}.png'.format(dataset, ini, fin, timestep, var, flag)
title = r'Global Mean $C\left(A_Z, K_Z\right) \: \left(\mathrm{W \: m^{-2}}\right)$'
c_az_kz_mkgrph(fig, title, timestep, dataset, ini, fin, flag)


var   = 'c_kz_ae'
fig   = './figs/{}_{}_{}_{}_{}{}.png'.format(dataset, ini, fin, timestep, var, flag)
title = r'Global Mean $C\left(K_Z, A_E\right) \: \left(\mathrm{W \: m^{-2}}\right)$'
c_kz_ae_mkgrph(fig, title, timestep, dataset, ini, fin, flag)


var   = 'c_ke_kz'
fig   = './figs/{}_{}_{}_{}_{}{}.png'.format(dataset, ini, fin, timestep, var, flag)
title = r'Global Mean $C\left(K_E, K_Z\right) \: \left(\mathrm{W \: m^{-2}}\right)$'
c_ke_kz_mkgrph(fig, title, timestep, dataset, ini, fin, flag)


var   = 'c_kz_w'
fig   = './figs/{}_{}_{}_{}_{}{}.png'.format(dataset, ini, fin, timestep, var, flag)
title = r'Global Mean $C\left(K_Z, W\right) \: \left(\mathrm{W \: m^{-2}}\right)$'
c_kz_w_mkgrph(fig, title, timestep, dataset, ini, fin, flag)


var  = 'qe'
fig   = './figs/{}_{}_{}_{}_{}{}.png'.format(dataset, ini, fin, timestep, var, flag)
title = r'Global Mean $Q_E \: \left(\mathrm{W \: m^{-2}}\right)$'
qe_mkgrph(fig, title, timestep, dataset, ini, fin, flag)


var   = 'qz'
fig   = './figs/{}_{}_{}_{}_{}{}.png'.format(dataset, ini, fin, timestep, var, flag)
title = r'Global Mean $Q_Z \: \left(\mathrm{W \: m^{-2}}\right)$'
qz_mkgrph(fig, title, timestep, dataset, ini, fin, flag)


flag = '_QFILTER'

var   = 'qe'
fig   = './figs/{}_{}_{}_{}_{}{}.png'.format(dataset, ini, fin, timestep, var, flag)
title = r'Global Mean $Q_E \: \left(\mathrm{W \: m^{-2}}\right)$' + '\n12hr Moving Average of Diabatic Heating'
qe_mkgrph(fig, title, timestep, dataset, ini, fin, flag)


var   = 'qz'
fig   = './figs/{}_{}_{}_{}_{}{}.png'.format(dataset, ini, fin, timestep, var, flag)
title = r'Global Mean $Q_Z \: \left(\mathrm{W \: m^{-2}}\right)$' + '\n12hr Moving Average of Diabatic Heating'
qz_mkgrph(fig, title, timestep, dataset, ini, fin, flag)


