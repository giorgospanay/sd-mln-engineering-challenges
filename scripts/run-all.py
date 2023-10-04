# Run all experiments for paper

## Imports ##
import subprocess

## Globals ##

# List of Python libraries for experiments
py_libs=["pymnet","multinet","py3plex","netmem"]
# List of R libraries for experiments
r_libs=["muxviz","multinet","mully"]
# List of Julia libraries for experiments
jl_libs=["mlg.jl"]
# List of all datasets
data_list=["synth","aucs","london","euair","fftw","ff","citation"]

# Path to log exports
log_path="../logs/"

## Execute experiments ##
# Warning: writing to a log file (specifically, decoding the bytestring returned
# 	from calling subprocess shell) assumes a utf-8 encoding. Should be ok in the vast 
#	majority of cases.
def exp(e_id,pylibs,rlibs,jllibs,datasets):
	global log_path
	# Base commands
	cmdbase_py="python3 experiments.py "
	cmdbase_r="Rscript experiments.R "
	cmdbase_jl="python3 experiments.py "

	# Log write directory
	logwd=log_path+"exp"+str(e_id)+"/"

	# TODO: add special case for synth if needed
	# For all datasets to be read:
	for ds in datasets:
		# Run on all Python libs
		for py_lib in pylibs:
			# Generate command and open shell
			runpy=cmdbase_py+str(e_id)+" "+py_lib+" "+ds
			res=subprocess.check_output(runpy,shell=True,stderr=subprocess.STDOUT)
			# Save output to logpath.
			# File naming format: eid_ds(-size)_lib_lang.txt
			with open(logwd+str(e_id)+"_"+ds+"_"+py_lib+"_py.txt","w") as wf:
				wf.write(res.decode("utf-8"))
				wf.close()
		# Run on all R libs
		for r_lib in rlibs:
			# Generate command and open shell
			runr=cmdbase_r+str(e_id)+" "+r_lib+" "+ds
			res=subprocess.check_output(runr,shell=True,stderr=subprocess.STDOUT)
			# Save output to logpath.
			# File naming format: eid_ds(-size)_lib_lang.txt
			with open(logwd+str(e_id)+"_"+ds+"_"+r_lib+"_r.txt","w") as wf:
				wf.write(res.decode("utf-8"))
				wf.close()
		# # Run on all Julia libs
		# for jl_lib in jllibs:
		# 	# Generate command and open shell
		# 	runjl=cmdbase_jl+str(e_id)+" "+jl_lib+" "+ds
		# 	res=subprocess.check_output(runjl,shell=True,stderr=subprocess.STDOUT)
		# 	# Save output to logpath.
		# 	# File naming format: eid_ds(-size)_lib_lang.txt
		# 	with open(logwd+str(e_id)+"_"+ds+"_"+jl_lib+"_jl.txt","w") as wf:
		# 		wf.write(res.decode("utf-8"))
		# 		wf.close()

	return

# Result parser
def parse():
	return



# chicken chow main
def main():
	global py_libs,r_libs,jl_libs,data_list
	
	# # Debug stuff
	# cmd1="python3 experiments.py 1 pymnet aucs"
	# cmd2="Rscript experiments.R 1 muxviz aucs"
	# result1=subprocess.check_output(cmd1, shell=True, stderr=subprocess.STDOUT)
	# print(result1)
	# result2=subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT)
	# print(result2)

	# Call experiment function for debug
	exp(1,["pymnet"],["muxviz"],[],["aucs"])

	return


# For experiments in Python: call subprocess.
# python3 experiments.py experiment_id library dataset [size]

# For experiments in R: 
# Rscript experiments.R experiment_id library dataset [size]

# For experiments in Julia:
# 

# Python stuff
if __name__ == "__main__":
	main()