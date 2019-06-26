#!/bin/bash
# Submission script 
#SBATCH --time=0-00:30:00 # days-hh:mm:ss
#SBATCH --output=ellipse_DY.txt
#
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=10000 # megabytes
#SBATCH --partition=Def
#SBATCH --qos=normal
#SBATCH --job-name=Ellipses_DY
#

python EllipsesWithDNN.py -m BestModel --DNN --DY --start $1 --end $2

