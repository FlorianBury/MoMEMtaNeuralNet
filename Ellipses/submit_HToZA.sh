#!/bin/bash
# Submission script 
#SBATCH --time=0-01:00:00 # days-hh:mm:ss
#SBATCH --output=ellipse_HToZA.txt
#
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=20000 # megabytes
#SBATCH --partition=Def
#SBATCH --qos=normal
#SBATCH --job-name=Ellipses_HToZA
#

python EllipsesWithDNN.py -m BestModel -f $1 --DNN --HToZA --force

