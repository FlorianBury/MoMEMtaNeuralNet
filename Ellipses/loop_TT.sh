#!/bin/bash

end=500000
step=1000
for i in $(seq 0 $step $(($end-$step)))
  do 
     sbatch submit_TT.sh $i $(($i+$step)) 
     echo "Submitting TT job from "$i" to "$(($i+$step))
 done
