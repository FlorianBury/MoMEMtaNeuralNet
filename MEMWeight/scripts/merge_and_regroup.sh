#!/bin/bash

path="/home/ucl/cp3/fbury/scratch/MoMEMta_output/slurm/*"

for dir in $path; do
    # Extract name of root file from directory #
    if   [ ! -d "${dir}/output/" ]; then
        continue
    fi
    name=$(echo $dir | cut -c70-)
    echo "Directory : "$dir

    # Indide output #
    pushd $dir"/output/"  
    pwd

    if [ -f "output.root" ]; then
        rm output.root # if any was already there
    fi
    for file in "output_*.root"; do
        hadd output.root $file
    done 
    mv output.root $name".root"
    mv $name".root" ../../

    popd 

done 
