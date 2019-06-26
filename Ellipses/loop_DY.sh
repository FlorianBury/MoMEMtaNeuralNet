#!/bin/bash

end=300000
step=1000
for i in $(seq 0 $step $(($end-$step)))
  do 
     sbatch submit_DY.sh $i $(($i+$step)) 
     echo "Submitting DY job from "$i" to "$(($i+$step))
 done
