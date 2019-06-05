#!/bin/bash
# Submission script 
#SBATCH --time=0-08:00:00 # days-hh:mm:ss
#SBATCH --output=likelihood.txt
#
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=10000 # megabytes
#SBATCH --partition=Def
#SBATCH --qos=normal
#SBATCH --job-name=Likelihood
#
python Likelihood.py -m $1 -f $2  -n $3 --max $4 --norm
