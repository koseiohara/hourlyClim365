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

data1 = 'JRA55'
data2 = 'JRA3Q'
ini = 1990
fin = 2020
flag1 = ''
flag2 = ''

az_mkgrph(ini, fin, data1, data2, flag1, flag2)

kz_mkgrph(ini, fin, data1, data2, flag1, flag2)

ae_mkgrph(ini, fin, data1, data2, flag1, flag2)

ke_mkgrph(ini, fin, data1, data2, flag1, flag2)

w_mkgrph(ini, fin, data1, data2, flag1, flag2)

c_az_kz_mkgrph(ini, fin, data1, data2, flag1, flag2)

c_kz_ae_mkgrph(ini, fin, data1, data2, flag1, flag2)

c_kz_ke_mkgrph(ini, fin, data1, data2, flag1, flag2)

c_kz_w_mkgrph(ini, fin, data1, data2, flag1, flag2)

qe_mkgrph(ini, fin, data1, data2, flag1, flag2)

qz_mkgrph(ini, fin, data1, data2, flag1, flag2)


'''
flag = '_QFILTER'

var   = 'qe'
title = r'$Q_E \:\left(\mathrm{W \: m^{-2}}\right)$' + '\n12hr Moving Average of Diabatic Heating'
fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
qe_mkgrph(fig, title, dataset, ini, fin, flag)


var   = 'qz'
title = r'$Q_Z \:\left(\mathrm{W \: m^{-2}}\right)$' + '\n12hr Moving Average of Diabatic Heating'
fig   = './figs/{}_{}_{}_{}{}.png'.format(dataset, ini, fin, var, flag)
qz_mkgrph(fig, title, dataset, ini, fin, flag)
'''

