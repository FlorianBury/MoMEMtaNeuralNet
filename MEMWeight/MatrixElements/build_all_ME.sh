#!/bin/bash

path="/home/ucl/cp3/fbury/MoMEMtaNeuralNet/MEMWeight/MatrixElements/*"

for dir in $path; do
    if [ ! -d $dir ]; then
        continue
    fi
    pushd $dir > /dev/null
    echo "-----------------------------------------------"
    echo "Inside dir : "$dir
    
    if [ ! -d "$dir/build/" ]; then
        mkdir -p $dir/build
    fi
    pushd build > /dev/null
    
    echo "Using cmake"
    cmake -DCMAKE_PREFIX_PATH=~/.local/include/momemta/ ..
    echo "Using make"
    make -j 4
    
    popd > /dev/null
    popd > /dev/null


done
