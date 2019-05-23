#!/bin/bash

path="/home/ucl/cp3/fbury/scratch/MoMEMta_output/signal_weights_valid/"
number=100
model="BestModel"

sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-200_MA-100_signal_weights.root"       $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-200_MA-50_signal_weights.root"        $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-250_MA-100_signal_weights.root"       $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-250_MA-50_signal_weights.root"        $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-300_MA-100_signal_weights.root"       $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-300_MA-200_signal_weights.root"       $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-300_MA-50_signal_weights.root"        $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-500_MA-100_signal_weights.root"       $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-500_MA-200_signal_weights.root"       $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-500_MA-300_signal_weights.root"       $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-500_MA-400_signal_weights.root"       $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-500_MA-50_signal_weights.root"        $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-650_MA-50_signal_weights.root"        $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-800_MA-100_signal_weights.root"       $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-800_MA-200_signal_weights.root"       $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-800_MA-400_signal_weights.root"       $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-800_MA-50_signal_weights.root"        $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-800_MA-700_signal_weights.root"       $number 1000
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-1000_MA-200_signal_weights.root"      $number 1500
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-1000_MA-500_signal_weights.root"      $number 1500
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-1000_MA-50_signal_weights.root"       $number 1500
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-2000_MA-1000_signal_weights.root"     $number 2500
sbatch submit_likelihood.sh $model $path"HToZATo2L2B_MH-3000_MA-2000_signal_weights.root"     $number 3500
sbatch submit_likelihood.sh $model $path"All_DY.root"                                         $number 1000
sbatch submit_likelihood.sh $model $path"All_TT.root"                                         $number 1000
