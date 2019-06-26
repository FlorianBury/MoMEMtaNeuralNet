#!/bin/bash
# Submission script 
#SBATCH --time=0-00:30:00 # days-hh:mm:ss
#SBATCH --output=ellipse_TT.txt
#
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=10000 # megabytes
#SBATCH --partition=Def
#SBATCH --qos=normal
#SBATCH --job-name=Ellipses_TT
#

python EllipsesWithDNN.py -m BestModel --DNN --TT  --start $1 --end $2

