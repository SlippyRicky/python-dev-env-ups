#!/bin/bash

# Create exo_1, exo_2, exo_3 directories and files
for i in {1..3}; do
    dir="exo_$i"
    mkdir -p "$dir"
    cd "$dir" || exit
    touch "${dir}.py"
    touch "${dir}+$i.py"
    touch "${dir}++$i.py"
    cd ..
done
