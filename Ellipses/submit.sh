#!/bin/bash
# Submission script 
#SBATCH --time=0-02:00:00 # days-hh:mm:ss
#SBATCH --output=ellipse.txt
#
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=10000 # megabytes
#SBATCH --partition=Def
#SBATCH --qos=normal
#SBATCH --job-name=Ellipses
#

python EllipsesWithDNN.py -m $1 -f $2 --DNN --force

