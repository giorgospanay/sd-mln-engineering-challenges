# Run all experiments for paper

# Imports
import subprocess

# Local script imports


# chicken chow main
def main():
	
	# Debug stuff
	cmd1="python3 experiments.py 1 pymnet aucs"
	cmd2="Rscript experiments.R 1 muxviz aucs"

	result1=subprocess.check_output(cmd1, shell=True, stderr=subprocess.STDOUT)
	print(result1)

	result2=subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT)
	print(result2)

	# To call experiment from os:
	# result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)

	# 

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