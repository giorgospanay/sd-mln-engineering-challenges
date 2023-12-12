# Supplemental material for paper "Multilayer network software: A comparative study" 
Supplemental material (benchmark scripts) for the paper "Multilayer network software: A comparative study". See publication here: preprint <>, final <>. 
This repository contains the scripts necessary to replicate the experiments in the paper.

## Requirements
Current versions of Python3, R and Julia are needed to execute the entire range of scripts. The original libraries covered by the paper are: multinet (https://github.com/uuinfolab/r_multinet), MultilayerGraphs.jl (https://github.com/JuliaGraphs/MultilayerGraphs.jl/tree/main), MuxViz (https://github.com/manlius/muxViz), netmem (https://github.com/anespinosa/netmem), Pymnet (https://github.com/bolozna/Multilayer-networks-library) and Py3plex (https://github.com/SkBlaz/py3plex). For library-specific installation instructions, please refer to the respective documentation. 

In addition to these, there are a number of required packages for Python used by the scripts for importing modules, tracking execution time, processing log files and plotting the results. These can be install by executing `pip install parse subprocess pandas numpy matplotlib importlib` in your terminal.

## How to run
To execute the scripts as in their original form, three directories are needed: 
+ `scripts/`: contains all scripts (as in the repository).
+ `data/`: should contain a subfolder for each dataset used (cs-aarhus, london-transport, euair-transport, friendfeed, ff-tw) and one for synthetic data (synth).
+ `logs/`: should contain a subfolder for each experiment run (exp1, exp2, ...) and a subfolder for the plot images created (plots).

The plots featured in the paper are obtained by executing `python3 scripts/run-all.py`. Specifically, for each plot:
+ Network loading results: Exp2 + Exp7
+ Layer aggregation: Exp1 + Exp6
+ Degree computation: Exp2 + Exp7
+ Network generation: Exp5
This runs all experiments for the libraries by creating a new subprocess in the terminal, and executing the appropriate `experiments.(extension)` file, which in turn imports the respective `(lib-code)-util.(extension)` file where library-specific instructions to run that operator are found. By termination of the experiment, logfiles are created in the appropriate folder.

The list of experiment codes is as follows:
* Exp1: loading real datasets + layer aggregation
* Exp2: loading real datasets + degree computation (not currently included in run-all)
* Exp3: loading real datasets + run InfoMap (not working, not included)
* Exp4: generate multiplex networks + layer aggregation (not currently included in run-all)
* Exp5: generate multiplex networks + degree computation 
* Exp6: loading synthetic datasets + layer aggregation
* Exp7: loading synthetic datasets + degree computation
  
To run an experiment individually, you can execute `(prog-lang) experiments.(extension) (e_id) (lib-code) (data-code)` where `(prog-lang)` and `(extension)` is the programming language and script extension of the library respectively, `(lib-code)` is the code for each library (multinet,pymnet,netmem,py3plex,muxviz,mlgjl) and `(data-code)` is the code for each dataset (aucs,london,euair,ff,fftw) or a code for synthetic data (#nodes-avgdeg-#layers).
For example, running `Rscript experiments.R 7 multinet 1000-s-100` executes Exp7 on synthetic data (multiplex network with 1000 vertices, 100 layers and average degree=sqrt(V*L)) on the multinet R library.

Scripts for converting datasets between different input formats for libraries used in the benchmark can be found in `scripts/format-convert.py`. Code for generating synthetic multiplex networks can be seen in `scripts/generate-synth.py`.

## Other notes
To add more libraries to the benchmark, one needs to follow a similar procedure: create a (lib)-util.(extension) file, which implements the functions to be compared, and make sure you add the appropriate codes to the experiment scripts. Similarly for datasets; make sure you add a new subfolder to the `data/` directory, convert it to all formats covered by the libraries and point all the experiment scripts towards the dataset.
