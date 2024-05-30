# Run all experiments for paper

## Imports ##
import subprocess
import os, glob
import parse
import pandas as pd
import numpy as np
import time
from matplotlib import pyplot as plt

## Globals ##

# List of Python libraries for experiments
py_libs=["pymnet","py3plex"]
# List of R libraries for experiments
r_libs=["muxviz","multinet","netmem"]
# List of Julia libraries for experiments
jl_libs=["mlgjl"]
# List of all datasets
data_list=["synth","aucs","london","euair","fftw","ff"]

# Path to log exports
log_path="../logs/"


## Execute experiments ##
# Warning: writing to a log file (specifically, decoding the bytestring returned
# 	from calling subprocess shell) assumes a utf-8 encoding. Should be ok in the vast 
#	majority (if not all) of cases.
def run_exp(e_id,pylibs,rlibs,jllibs,datasets):
	global log_path
	# Base commands
	cmdbase_py="python3 experiments.py "
	cmdbase_r="Rscript experiments.R "
	cmdbase_jl="julia experiments.jl "

	# Log write directory
	logwd=log_path+"exp"+str(e_id)+"/"

	# TODO: add special case for synth if needed
	# For all datasets to be read:
	for ds in datasets:
		# Run on all Python libs
		for py_lib in pylibs:
			# Generate command and open shell
			runpy=cmdbase_py+str(e_id)+" "+py_lib+" "+ds
			try:
				time_exec_s=time.time()
				res=subprocess.check_output(runpy,shell=True,timeout=1800,stderr=subprocess.STDOUT)
				time_exec_e=time.time()
				time_exec_t=time_exec_e-time_exec_s
				# Save output to logpath.
				# File naming format: eid_ds(-size)_lib_lang.txt
				with open(logwd+str(e_id)+"_"+ds+"_"+py_lib+"_py.txt","w") as wf:
					wf.write(res.decode("utf-8"))
					wf.write("\n")
					wf.write("Execution time (in sec.): "+str(time_exec_t))
					wf.close()
			except subprocess.CalledProcessError as e:
				# Save error to logpath.
				with open(logwd+str(e_id)+"_"+ds+"_"+py_lib+"_py.txt","w") as wf:
					if e.stdout!=None:
						wf.write(e.stdout.decode("utf-8"))
						wf.write("\n---------------------------\n")
					if e.stderr!=None:
						wf.write(e.stderr.decode("utf-8"))
						wf.write("\n---------------------------\n")
					wf.close()
			except subprocess.TimeoutExpired as to:
				# Save error to logpath.
				with open(logwd+str(e_id)+"_"+ds+"_"+py_lib+"_py.txt","w") as wf:
					wf.write("Timeout: 1800 seconds\n")
					wf.close()
		# Run on all R libs
		for r_lib in rlibs:
			# Generate command and open shell
			runr=cmdbase_r+str(e_id)+" "+r_lib+" "+ds
			try:
				time_exec_s=time.time() 
				res=subprocess.check_output(runr,shell=True,timeout=1800,stderr=subprocess.STDOUT)
				time_exec_e=time.time()
				time_exec_t=time_exec_e-time_exec_s
				# Save output to logpath.
				# File naming format: eid_ds(-size)_lib_lang.txt
				with open(logwd+str(e_id)+"_"+ds+"_"+r_lib+"_r.txt","w") as wf:
					wf.write(res.decode("utf-8"))
					wf.write("\n")
					wf.write("Execution time (in sec.): "+str(time_exec_t))
					wf.close()
			except subprocess.CalledProcessError as e:
				# Save error to logpath.
				with open(logwd+str(e_id)+"_"+ds+"_"+r_lib+"_r.txt","w") as wf:
					if e.stdout!=None:
						wf.write(e.stdout.decode("utf-8"))
						wf.write("\n---------------------------\n")
					if e.stderr!=None:
						wf.write(e.stderr.decode("utf-8"))
						wf.write("\n---------------------------\n")
					wf.close()
			except subprocess.TimeoutExpired as to:
				# Save error to logpath.
				with open(logwd+str(e_id)+"_"+ds+"_"+r_lib+"_r.txt","w") as wf:
					wf.write("Timeout: 1800 seconds\n")
					wf.close()
		# Run on all Julia libs
		for jl_lib in jllibs:
			# Generate command and open shell
			runjl=cmdbase_jl+str(e_id)+" "+jl_lib+" "+ds
			try:
				time_exec_s=time.time()
				res=subprocess.check_output(runjl,shell=True,timeout=1800,stderr=subprocess.STDOUT)
				time_exec_e=time.time()
				time_exec_t=time_exec_e-time_exec_s
				# Save output to logpath.
				# File naming format: eid_ds(-size)_lib_lang.txt
				with open(logwd+str(e_id)+"_"+ds+"_"+jl_lib+"_jl.txt","w") as wf:
					wf.write(res.decode("utf-8"))
					wf.write("\n")
					wf.write("Execution time (in sec.): "+str(time_exec_t))
					wf.close()
			except subprocess.CalledProcessError as e:
				# Save error to logpath.
				with open(logwd+str(e_id)+"_"+ds+"_"+jl_lib+"_jl.txt","w") as wf:
					if e.stdout!=None:
						wf.write(e.stdout.decode("utf-8"))
						wf.write("\n---------------------------\n")
					if e.stderr!=None:
						wf.write(e.stderr.decode("utf-8"))
						wf.write("\n---------------------------\n")
					wf.close()
			except subprocess.TimeoutExpired as to:
				# Save error to logpath.
				with open(logwd+str(e_id)+"_"+ds+"_"+jl_lib+"_jl.txt","w") as wf:
					wf.write("Timeout: 1800 seconds\n")
					wf.close()		

	return





# chicken chow main
def main():
	global py_libs,r_libs,jl_libs,data_list

	# All server calls

	print("Experiment 1 running: Loading real datasets + aggregation")
	# Call exp1: Loading + aggregation, real datasets
	run_exp(1,["pymnet","py3plex"],["muxviz","multinet"],[],["aucs","london","euair","fftw","ff"])
	
	# print("Experiment 2 running: Loading real datasets + degree")
	# # Call exp2: Loading + degree, real datasets
	# run_exp(2,["pymnet","py3plex"],["muxviz","multinet"],["mlgjl"],["aucs","london","euair","fftw","ff"])


	# # [REM] Call exp4: Generate + aggregate, synth networks
	# # Run 1: Keep l=2, iterate n={1000,2000,5000,10000,20000,50000,100000}
	# for n in [1000,2000,5000,10000,20000,50000,100000]:
	# 	dstr=""+str(n)+"-2"
	# 	run_exp(4,["pymnet","py3plex"],["muxviz","multinet"],[],[dstr])
	# # Run 2: Keep n=1000, iterate l={2,5,10,20,50,100,200,500,1000}
	# for l in [5,10,20,50,100,200,500,1000]:
	# 	dstr="1000-"+str(l)
	# 	run_exp(4,["pymnet","py3plex"],["muxviz","multinet"],[],[dstr])	

	# print("Experiment 5 running: Generate multiplex network")
	# # Call exp5: Generate synth networks. Skip degree calc
	# # Run 1: Keep l=2, iterate n={1000-1M}
	# for n in [1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000]:
	# 	dstr=""+str(n)+"-2"
	# 	run_exp(5,["pymnet","py3plex"],["muxviz","multinet"],[],[dstr])
	# # Run 2: Keep n=1000, iterate l={5-10000}
	# for l in [5,10,20,50,100,200,500,1000,2000,5000,10000]:
	# 	dstr="1000-"+str(l)
	# 	run_exp(5,["pymnet","py3plex"],["muxviz","multinet"],[],[dstr])

	# Call exp6: Loading synth + aggregation
	print("Experiment 6 running: Loading synthetic data + aggregation")
	# Run 1: Keep l=2, e=4, iterate n={1000-10M}
	for n in [1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000,5000000,10000000]:
		dstr=""+str(n)+"-4-2"
		run_exp(6,["pymnet","py3plex"],["muxviz","multinet"],[],[dstr])
	# Run 2: Keep l=2, e="s", iterate n={1000-100K}
	for n in [1000,2000,5000,10000,20000,50000,100000]:
		dstr=""+str(n)+"-s-2"
		run_exp(6,["pymnet","py3plex"],["muxviz","multinet"],[],[dstr])
	# Run 3: Keep n=1000, e=4, iterate l={2-10K}
	for l in [5,10,20,50,100,200,500,1000,2000,5000,10000]:
		dstr="1000-4-"+str(l)
		run_exp(6,["pymnet","py3plex"],["muxviz","multinet"],[],[dstr])
	# Run 4a: Keep n=1000, e=s, iterate l={2-10K}
	for l in [5,10,20,50,100,200]:
		dstr="1000-s-"+str(l)
		run_exp(6,["pymnet","py3plex"],["muxviz","multinet"],[],[dstr])

	# # Call exp7: Loading synth + degree
	# print("Experiment 7 running: Loading synthetic data + degree")
	# # Run 1: Keep l=2, e=4, iterate n={1000-10M}
	# for n in [1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000,5000000,10000000]:
	# 	dstr=""+str(n)+"-4-2"
	# 	run_exp(7,["pymnet","py3plex"],["muxviz","multinet"],["mlgjl"],[dstr])
	# # Run 2: Keep l=2, e="s", iterate n={1000-100K}
	# for n in [1000,2000,5000,10000,20000,50000,100000]:
	# 	dstr=""+str(n)+"-s-2"
	# 	run_exp(7,["pymnet","py3plex"],["muxviz","multinet"],["mlgjl"],[dstr])
	# # Run 3: Keep n=1000, e=4, iterate l={2-10K}
	# for l in [5,10,20,50,100,200,500,1000,2000,5000,10000]:
	# 	dstr="1000-4-"+str(l)
	# 	run_exp(7,["pymnet","py3plex"],["muxviz","multinet"],["mlgjl"],[dstr])
	# # Run 4a: Keep n=1000, e=s, iterate l={2-10K}
	# for l in [5,10,20,50,100,200]:
	# 	dstr="1000-s-"+str(l)
	# 	run_exp(7,["pymnet","py3plex"],["muxviz","multinet"],["mlgjl"],[dstr])

	# Call exp8: Load empty + random build
	print("Experiment 8 running: Loading synth empty (1000-0-10) + random building")
	run_exp(8,["pymnet","py3plex"],["muxviz","multinet"],[],["1000-0-10"])

	return

# Python stuff
if __name__ == "__main__":
	main()