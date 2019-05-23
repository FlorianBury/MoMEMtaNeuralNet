#!/bin/bash
# Submission script 
#SBATCH --time=0-02:00:00 # days-hh:mm:ss
#SBATCH --output=Xsec.txt
#
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=5000 # megabytes
#SBATCH --partition=Def
#SBATCH --qos=normal
#SBATCH --array=1-100
#

python AcceptanceAndXsecGraph.py --bins 500 --max 3500 --xsec
