'reinit'

VAR='q'

'open ../JRA3Q_1990_2020_ALL_ZONAL_'VAR'_QFILTER.ctl'
say 'open ../JRA3Q_1990_2020_ALL_ZONAL_'VAR'_QFILTER.ctl'

'set zlog on'
'set lev 1000 50'

'display ave('VAR', time=00Z01DEC1999, time=18Z28FEB2000)'
'gxprint 'VAR'_DJF.png'
'clear'

'display ave('VAR', time=00Z01MAR2000, time=18Z31MAY2000)'
'gxprint 'VAR'_MAM.png'
'clear'

'display ave('VAR', time=00Z01JUN2000, time=18Z31AUG2000)'
'gxprint 'VAR'_JJA.png'
'clear'

'display ave('VAR', time=00Z01SEP2000, time=18Z30NOV2000)'
'gxprint 'VAR'_SON.png'
'clear'

