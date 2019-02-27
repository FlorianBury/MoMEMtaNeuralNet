#!/bin/bash

# HtoZA #
python submit_on_slurm.py -n HToZATo2L2B_MH-300_MA-50 -i HToZATo2L2B_MH-300_MA-50.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-200_MA-50 -i HToZATo2L2B_MH-200_MA-50.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-2000_MA-1000 -i HToZATo2L2B_MH-2000_MA-1000.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-250_MA-50 -i HToZATo2L2B_MH-250_MA-50.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-500_MA-400 -i HToZATo2L2B_MH-500_MA-400.root -m  &&
python submit_on_slurm.py -n HToZATo2L2B_MH-1000_MA-200 -i HToZATo2L2B_MH-1000_MA-200.root -m&&
python submit_on_slurm.py -n HToZATo2L2B_MH-300_MA-200 -i HToZATo2L2B_MH-300_MA-200.root -m &&
python submit_on_slurm.py -n HToZATo2L2B_MH-800_MA-400 -i HToZATo2L2B_MH-800_MA-400.root -m &&
python submit_on_slurm.py -n HToZATo2L2B_MH-500_MA-100 -i HToZATo2L2B_MH-500_MA-100.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-500_MA-50 -i HToZATo2L2B_MH-500_MA-50.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-650_MA-50 -i HToZATo2L2B_MH-650_MA-50.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-800_MA-100 -i HToZATo2L2B_MH-800_MA-100.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-1000_MA-50 -i HToZATo2L2B_MH-1000_MA-50.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-300_MA-100 -i HToZATo2L2B_MH-300_MA-100.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-800_MA-700 -i HToZATo2L2B_MH-800_MA-700.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-1000_MA-500 -i HToZATo2L2B_MH-1000_MA-500.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-500_MA-300 -i HToZATo2L2B_MH-500_MA-300.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-200_MA-100 -i HToZATo2L2B_MH-200_MA-100.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-250_MA-100 -i HToZATo2L2B_MH-250_MA-100.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-800_MA-200 -i HToZATo2L2B_MH-800_MA-200.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-800_MA-50 -i HToZATo2L2B_MH-800_MA-50.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-3000_MA-2000 -i HToZATo2L2B_MH-3000_MA-2000.root -m 1000 &&
python submit_on_slurm.py -n HToZATo2L2B_MH-500_MA-200 -i HToZATo2L2B_MH-500_MA-200.root -m 1000 &&

# DY #
python submit_on_slurm.py -n DYJetsToLL_M -i DYJetsToLL_M.root -m 1000 &&
python submit_on_slurm.py -n DYToLL_0J -i DYToLL_0J.root -m 1000 &&
python submit_on_slurm.py -n DYToLL_1J -i DYToLL_1J.root -m 1000 &&
python submit_on_slurm.py -n DYToLL_2J -i DYToLL_2J.root -m 1000 &&

# TTBars #
python submit_on_slurm.py -n TTTo2L2Nu -i TTTo2L2Nu.root -m 1000 && 
python submit_on_slurm.py -n TT_Other -i TT_Otherroot -m 1000 
