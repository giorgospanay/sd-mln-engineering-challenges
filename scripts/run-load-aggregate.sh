#!/bin/zsh

# Experiment script for paper "A comparative study of libraries for quantitative 
# multilayer network analysis". Providing a simple shellscript invoking the main 
# functions from each library script, as they are sometimes coded on different 
# languages. For more details, please refer to the documentation on each library's 
# experiment script.
# Author: Georgios Panayiotou


# If needed: change working directory. 
# For now, assuming we are working inside scripts.


# Run each executable. First by file, then by library.

# cs-aarhus
echo "---AUCS---"
python3 load-aggregate/pymnet-load-aggregate.py aucs # Pymnet
# multinet (python)
# MuxViz
# multinet (R)

# Py3plex?
# netmem?
# mully? 
# MLG.jl?
echo "--------------------"
echo ""

# Find other large networks to aggregate into one aspect.





# Rscript script_name.R
# python3 script_name.py
