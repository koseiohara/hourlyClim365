#!/bin/bash

#PBS -q tqueue
#PBS -N ClimShift
#PBS -j oe
#PBS -l nodes=1:ppn=1

DATASET="JRA55"
DIM="VINT"
VAR="qz"
PERIOD_START=1990
PERIOD_END=2020
FLAG="_QFILTER"
FLAG=""
#NOW=$(date "+%Y%m%d_%H%M%S")

RESULT="../output/${DATASET}/result_${DATASET}_${PERIOD_START}_${PERIOD_END}_${DIM}_${VAR}${FLAG}.txt"
NAMELIST="../nml/input_${DATASET}_${PERIOD_START}_${PERIOD_END}_${DIM}_${VAR}${FLAG}.nml"

cd /mnt/jet11/kosei/mim/energetics/hourlyClim365/shift/src/
cat ${NAMELIST} > ${RESULT}

./EXE < ${NAMELIST} >> ${RESULT} 2>&1

