#!/bin/bash
# Submission script 
#SBATCH --time=0-00:10:00 # days-hh:mm:ss
#SBATCH --output=Likelihood.txt
#
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=5000 # megabytes
#SBATCH --partition=Def
#SBATCH --qos=normal
#SBATCH --job-name=Likelihood
#
echo $1
echo $2
echo $3
echo $4
python Likelihood.py -m $1 -f $2  -n $3 --max $4
python Likelihood.py -m $1 -f $2  -n $3 --max $4 --norm
