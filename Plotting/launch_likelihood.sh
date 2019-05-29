#!/bin/bash


python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-200_MA-100_signal_weights.root      -n $2 --max 1000 --norm   
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-200_MA-50_signal_weights.root       -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-250_MA-100_signal_weights.root      -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-250_MA-50_signal_weights.root       -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-300_MA-100_signal_weights.root      -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-300_MA-200_signal_weights.root      -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-300_MA-50_signal_weights.root       -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-500_MA-100_signal_weights.root      -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-500_MA-200_signal_weights.root      -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-500_MA-300_signal_weights.root      -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-500_MA-400_signal_weights.root      -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-500_MA-50_signal_weights.root       -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-650_MA-50_signal_weights.root       -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-800_MA-100_signal_weights.root      -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-800_MA-200_signal_weights.root      -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-800_MA-400_signal_weights.root      -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-800_MA-50_signal_weights.root       -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-800_MA-700_signal_weights.root      -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-1000_MA-200_signal_weights.root     -n $2 --max 1500 --norm 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-1000_MA-500_signal_weights.root     -n $2 --max 1500 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-1000_MA-50_signal_weights.root      -n $2 --max 1500 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-2000_MA-1000_signal_weights.root    -n $2 --max 2500 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-3000_MA-2000_signal_weights.root    -n $2 --max 3500 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/All_DY.root                                        -n $2 --max 1000 --norm
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/All_TT.root                                        -n $2 --max 1000 --norm

python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-200_MA-100_signal_weights.root      -n $2 --max 1000   
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-200_MA-50_signal_weights.root       -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-250_MA-100_signal_weights.root      -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-250_MA-50_signal_weights.root       -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-300_MA-100_signal_weights.root      -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-300_MA-200_signal_weights.root      -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-300_MA-50_signal_weights.root       -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-500_MA-100_signal_weights.root      -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-500_MA-200_signal_weights.root      -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-500_MA-300_signal_weights.root      -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-500_MA-400_signal_weights.root      -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-500_MA-50_signal_weights.root       -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-650_MA-50_signal_weights.root       -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-800_MA-100_signal_weights.root      -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-800_MA-200_signal_weights.root      -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-800_MA-400_signal_weights.root      -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-800_MA-50_signal_weights.root       -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-800_MA-700_signal_weights.root      -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-1000_MA-200_signal_weights.root     -n $2 --max 1500 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-1000_MA-500_signal_weights.root     -n $2 --max 1500 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-1000_MA-50_signal_weights.root      -n $2 --max 1500 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-2000_MA-1000_signal_weights.root    -n $2 --max 2500 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/HToZATo2L2B_MH-3000_MA-2000_signal_weights.root    -n $2 --max 3500 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/All_DY.root                                        -n $2 --max 1000 
python Likelihood.py -m $1 -f /home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/All_TT.root                                        -n $2 --max 1000 

python Likelihood.py -m $1 --PDF

