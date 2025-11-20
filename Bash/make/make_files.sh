#!/bin/bash
for i in {1..3}; do
    dir="exo_$i"
    mkdir -p "$dir"
    cd "$dir" || exit
    touch "exo_$i.py"
    touch "exo+$i.py"
    touch "exo++$i.py"
    cd ..
done
