#!/bin/bash

for dir in exo_{1..3}; do
  x=0
    if [ -d "$dir" ]; then
        x=+1
        # Navigate into the directory
        cd "$dir"
        # Create a Python file with the same name as the directory
        touch "${dir}_$x.py"
        touch "${dir}+$x.py"
        touch "${dir}++$x.py"
        # Navigate back to the original directory
        cd ..
    fi
done
