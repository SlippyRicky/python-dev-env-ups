#!/bin/bash

# Ensure the main directory exists and enter it
mkdir -p Projet_Final
cd Projet_Final || exit

# Loop for the 4 exercises found in the worksheet
for i in {1..4}; do
    dir="exo_$i"
    mkdir -p "$dir"
    cd "$dir" || exit
    
    # Create the standard, plus, and double-plus python files
    touch "exo_$i.py"
    touch "exo+$i.py"
    touch "exo++$i.py"
    
    # Return to the Projet_Final directory
    cd ..
done

echo "Structure for Exercises 1-4 created inside Projet_Final."
