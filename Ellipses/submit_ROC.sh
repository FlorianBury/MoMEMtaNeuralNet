#!/bin/bash
# Submission script 
#SBATCH --time=0-04:00:00 # days-hh:mm:ss
#SBATCH --output=ellipse_ROC.txt
#
#SBATCH --ntasks=1
#SBATCH --partition=Def
#SBATCH --qos=normal
#SBATCH --job-name=Ellipses_ROC
#

python EllipsesWithDNN.py -m BestModel -f $1 --ellipse --ROC 

