#!/bin/bash

for dir in exo_{1..8}; do
    if [ -d "$dir" ]; then
        # Navigate into the directory
        cd "$dir"
        # Create a Python file with the same name as the directory
        touch "${dir}.py"
        # Navigate back to the original directory
        cd ..
    fi
done
