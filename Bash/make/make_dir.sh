#!/bin/bash

for i in {1..2}; do

  name="folder_name"
  dir="${name}_$i"
  mkdir -p "$dir"

  cd "$dir" || exit
  touch "${dir}.py"
  cd ..
done
