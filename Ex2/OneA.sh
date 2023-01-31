#!/bin/bash
for i in {1..10}
do
    ( ./hw.out $i > OneA/job$i\_$BASHPID & )
done

