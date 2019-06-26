#!/bin/bash
# Submission script 
#SBATCH --time=1-00:00:00 # days-hh:mm:ss
#SBATCH --output=ellipse.txt
#
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=5000 # megabytes
#SBATCH --partition=Def
#SBATCH --qos=normal
#SBATCH --job-name=Ellipses
#

python EllipsesWithDNN.py -m BestModel -f $1 --DNN --HToZA --DY --TT --ellipse --force_ellipse

