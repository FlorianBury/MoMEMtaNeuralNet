#!/bin/bash
# Merge the root files inside a directory into one that gets the name of the dir
path="/home/ucl/cp3/fbury/scratch/MoMEMta_output/slurm/*$1*"

for dir in $path; do
    # Extract name of root file from directory #
    if   [ ! -d "${dir}/output/" ]; then
        continue
    fi
    name=$(echo $dir | cut -c70-)
    echo "Directory : "$dir
    echo "Name : "$name

    # Indide output #
    pushd $dir"/output/" > /dev/null
    pwd

    if [ -f "output.root" ]; then
        rm output.root # if any was already there
    fi
    for file in "output_*.root"; do
        hadd output.root $file
    done 
    mv output.root $name".root"
    mv $name".root" ../../

    popd > /dev/null

done 
