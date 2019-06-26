#!/bin/bash
# Submission script 
#SBATCH --time=0-04:00:00 # days-hh:mm:ss
#SBATCH --output=likelihood.txt
#
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=5000 # megabytes
#SBATCH --partition=Def
#SBATCH --qos=normal
#SBATCH --job-name=Likelihood
#
python Likelihood.py -m $1 -f $2  -n $3 --xmax $4 --ymax $4 --norm --suffix $5
