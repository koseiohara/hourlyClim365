'reinit'

VAR.1 = 'qe'
VAR.2 = 'ttswr_qe'
VAR.3 = 'ttlwr_qe'
VAR.4 = 'lrghr_qe'
VAR.5 = 'cnvhr_qe'
VAR.6 = 'vdfhr_qe'

BEG.1 = '00Z01DEC1999'
BEG.2 = '00Z01MAR2000'
BEG.3 = '00Z01JUN2000'
BEG.4 = '00Z01SEP2000'

END.1 = '18Z28FEB2000'
END.2 = '18Z31MAY2000'
END.3 = '18Z31AUG2000'
END.4 = '18Z30NOV2000'

SEASON.1 = 'DJF'
SEASON.2 = 'MAM'
SEASON.3 = 'JJA'
SEASON.4 = 'SON'

i = 1

cmin = -0.001
cmax =  0.001
cint =  0.0001

while (i <= 6)
    say VAR.i
    j = 1
    while (j <= 4)

        say

        ofile = './figs/JRA3Q_1980_2023_ZONAL_'VAR.i'_'SEASON.j'.png'
        say ofile

        'reinit'

        'open ../../output/JRA3Q/JRA3Q_1980_2023_ALL_ZONAL_'VAR.i'_QFILTER.ctl'
        say 'open ../../output/JRA3Q/JRA3Q_1980_2023_ALL_ZONAL_'VAR.i'_QFILTER.ctl'

        'set display color white'
        'set grads off'

        'set zlog on'
        'set lev 1000 10'

        'set xlopts 1 2.5 0.2'
        'set ylopts 1 2.5 0.2'

        'set ylevs 1000 500 300 100 50 30 10'

        say

        'set gxout shaded'
        'color 'cmin' 'cmax' 'cint
        'display ave('VAR.i', time='BEG.j', time='END.j')'
        say 'display ave('VAR.i', time='BEG.j', time='END.j')'
        'xcbar 1.5 9.5 0.35 0.55 -edge triangle -foffset center -fskip 4 -fwidth 0.2 -fheight 0.2'

*        'set strsiz 0.25 0.25'
*        'draw string 5.5 8.4 Geopotential Height and Wind at 850 hPa'

        'gxprint 'ofile

        'clear'
        j = j + 1
    endwhile
    i = i + 1
endwhile


* 'open ../../output/JRA3Q/JRA3Q_1980_2023_ALL_ZONAL_qe_QFILTER.ctl'
* 'set time 00Z02SEP2020'
* 'set lev 850'
* 'set lon 120 150'
* 'set lat 24 46'
* 
* 'set xlopts 1 2.5 0.2'
* 'set ylopts 1 2.5 0.2'
* 
* cmin = 1250
* cmax = 1700
* cint = 25
* ofile = 'MAYSAK2020.png'
* 
* 'set gxout shaded'
* 'color 'cmin' 'cmax' 'cint
* 'display HGTprs'
* 'xcbar 1.5 9.5 0.4 0.7 -edge triangle -foffset center -fskip 4 -fwidth 0.2 -fheight 0.2'
* 'set strsiz 0.15 0.15'
* 'draw string 10.0 0.3 [m]'
* 
* * 'set gxout contour'
* * 'set clab off'
* * 'set ccolor 0'
* * 'set cmin 'cmin
* * 'set cmax 'cmax
* * 'set cint 'cint
* * 'display HGTprs'
* 
* scale = 2.5
* skip  = 25
* 'set gxout vector'
* 'set ccolor 1'
* 'set arrlab off'
* 'display skip(UGRDprs*'scale', 'skip', 'skip');VGRDprs*'scale
* 
* 
* 'set strsiz 0.25 0.25'
* 'draw string 5.5 8.4 Geopotential Height and Wind at 850 hPa'
* 
* 
* 'gxprint 'ofile
* 
* 'quit'
* 
