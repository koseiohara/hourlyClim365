from plot_az       import az_mkgrph
from plot_kz       import kz_mkgrph
from plot_ae       import ae_mkgrph
from plot_ke       import ke_mkgrph
from plot_w        import w_mkgrph
from plot_c_az_kz  import c_az_kz_mkgrph
from plot_c_kz_ae  import c_kz_ae_mkgrph
from plot_c_kz_ke  import c_kz_ke_mkgrph
from plot_c_kz_w   import c_kz_w_mkgrph
from plot_qe       import qe_mkgrph
from plot_qz       import qz_mkgrph

dataset = 'JRA55'
ini = 1990
fin = 2020
flag = ''

var   = 'az'
title = r'$A_Z \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$'
fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
az_mkgrph(fig, title, dataset, ini, fin, flag)


var   = 'kz'
title = r'$K_Z \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$'
fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
kz_mkgrph(fig, title, dataset, ini, fin, flag)


var   = 'ae'
title = r'$A_E \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$'
fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
ae_mkgrph(fig, title, dataset, ini, fin, flag)


var   = 'ke'
title = r'$A_E \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$'
fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
ke_mkgrph(fig, title, dataset, ini, fin, flag)


var   = 'w'
title = r'$W \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$'
fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
w_mkgrph(fig, title, dataset, ini, fin, flag)


var   = 'c_az_kz'
title = r'$C\left(A_Z, K_Z\right) \:\left(\mathrm{W \: m^{-2}}\right)$'
fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
c_az_kz_mkgrph(fig, title, dataset, ini, fin, flag)


var   = 'c_kz_ae'
title = r'$C\left(K_Z, A_E\right) \:\left(\mathrm{W \: m^{-2}}\right)$'
fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
c_kz_ae_mkgrph(fig, title, dataset, ini, fin, flag)


var   = 'c_kz_ke'
title = r'$C\left(K_Z, K_E\right) \:\left(\mathrm{W \: m^{-2}}\right)$'
fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
c_kz_ke_mkgrph(fig, title, dataset, ini, fin, flag)


var   = 'c_kz_w'
title = r'$C\left(K_Z, W\right) \:\left(\mathrm{W \: m^{-2}}\right)$'
fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
c_kz_w_mkgrph(fig, title, dataset, ini, fin, flag)


var   = 'qe'
title = r'$Q_E \:\left(\mathrm{W \: m^{-2}}\right)$'
fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
qe_mkgrph(fig, title, dataset, ini, fin, flag)


var   = 'qz'
title = r'$Q_Z \:\left(\mathrm{W \: m^{-2}}\right)$'
fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
qz_mkgrph(fig, title, dataset, ini, fin, flag)


flag = '_QFILTER'

var   = 'qe'
title = r'$Q_E \:\left(\mathrm{W \: m^{-2}}\right)$' + '\n12hr Moving Average of Diabatic Heating'
fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
qe_mkgrph(fig, title, dataset, ini, fin, flag)


var   = 'qz'
title = r'$Q_Z \:\left(\mathrm{W \: m^{-2}}\right)$' + '\n12hr Moving Average of Diabatic Heating'
fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
qz_mkgrph(fig, title, dataset, ini, fin, flag)


