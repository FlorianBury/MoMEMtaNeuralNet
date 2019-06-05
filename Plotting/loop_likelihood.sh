#!/bin/bash

path="/home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/"
number=20000
max=1500
model="BestModel"

sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-200_MA-100_signal_weights.root"       $number $max   
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-200_MA-50_signal_weights.root"        $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-250_MA-100_signal_weights.root"       $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-250_MA-50_signal_weights.root"        $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-300_MA-100_signal_weights.root"       $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-300_MA-200_signal_weights.root"       $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-300_MA-50_signal_weights.root"        $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-500_MA-100_signal_weights.root"       $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-500_MA-200_signal_weights.root"       $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-500_MA-300_signal_weights.root"       $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-500_MA-400_signal_weights.root"       $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-500_MA-50_signal_weights.root"        $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-650_MA-50_signal_weights.root"        $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-800_MA-100_signal_weights.root"       $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-800_MA-200_signal_weights.root"       $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-800_MA-400_signal_weights.root"       $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-800_MA-50_signal_weights.root"        $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-800_MA-700_signal_weights.root"       $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-1000_MA-200_signal_weights.root"         $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-1000_MA-500_signal_weights.root"         $number $max 
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-1000_MA-50_signal_weights.root"         $number $max 
sbatch submit_likelihood.sh $model $path"All_DY.root"                                         $number $max 
sbatch submit_likelihood.sh $model $path"All_TT.root"                                         $number $max 

