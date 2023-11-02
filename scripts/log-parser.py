import os, glob
import parse
import pandas as pd
import numpy as np
import time
from matplotlib import pyplot as plt

# Path to log exports
log_path="../logs/"

# Result parser
def parse_exp1(out_file):
	global log_path
	df=pd.DataFrame(columns=["dataset","library","load_time","load_mem","aggr_time","aggr_mem"])
	# Open all logfiles in path
	for filename in glob.glob(log_path+"exp1/1_*.txt"):
		with open(filename,'r') as f: 
   			# Find line starting with Exp1:
   			header_found=0
   			lib_name=""
   			data_name=""
   			load_time=0.0
   			load_mem=0
   			aggr_time=0.0
   			aggr_mem=0
   			for ln in f.readlines():
   				if header_found==0 and not("Exp1:" in ln):
   					continue
   				elif "Exp1:" in ln:
   					header_found=1
   					parsed=parse.parse("Exp1: lib={}, file={}",ln.strip())
   					lib_name=parsed[0]
   					data_name=parsed[1]
   				# Found timed out experiment, parse filename instead
   				elif "Timeout" in ln:
   					parsed=parse.parse(log_path+"exp1/1_{}_{}_{}.txt",filename)
   					lib_name=parsed[1]
   					data_name=parsed[0]
   					# Programming language should be on parsed[2] if necessary
   					break
   				# Should reach here after done with header
   				# Line 1: loading time
   				if "Loading time" in ln:
   					parsed=parse.parse("Loading time (in sec.): {}",ln.strip())
   					if not parsed is None:
   						load_time=parsed[0]
   				# Line 2: loading memory
   				if "Loading mem" in ln:
   					parsed=parse.parse("Loading mem curr (in bytes): {}",ln.strip())
   					if not parsed is None:
   						load_mem=parsed[0]
   				# Line 3: aggregation time
   				if "Aggregate time" in ln:
   					parsed=parse.parse("Aggregate time (in sec.): {}",ln.strip())
   					if not parsed is None:
   						aggr_time=parsed[0]
   				# Line 4: aggregation memory
   				if "Aggregate mem" in ln:
   					parsed=parse.parse("Aggregate mem curr (in bytes): {}",ln.strip())
   					if not parsed is None:
   						aggr_mem=parsed[0]
   			# Done with lines- add into dataframe
   			df.loc[len(df)]={"dataset":data_name,"library":lib_name,"load_time":float(load_time),"load_mem":int(load_mem),"aggr_time":float(aggr_time),"aggr_mem":int(aggr_mem)}

   	# Done with all files. Aggregate total times.
	df["total_time"]=df.apply(lambda r: r.load_time+r.aggr_time, axis=1)
	df.dropna()

	# Sort by dataset and library
	df=df.sort_values(["dataset","library"])

	# Write dataframe to csv file
	df.to_csv(out_file,sep=" ",index=False)
	return

# Result parser, Exp 2
def parse_exp2(out_file):
	global log_path
	df=pd.DataFrame(columns=["dataset","library","load_time","load_mem","degr_time","degr_mem"])
	# Open all logfiles in path
	for filename in glob.glob(log_path+"exp2/2_*.txt"):
		with open(filename,'r') as f: 
   			# Find line starting with Exp1:
   			header_found=0
   			lib_name=""
   			data_name=""
   			load_time=0.0
   			load_mem=0
   			degr_time=0.0
   			degr_mem=0
   			for ln in f.readlines():
   				if header_found==0 and not("Exp2:" in ln):
   					continue
   				elif "Exp2:" in ln:
   					header_found=1
   					parsed=parse.parse("Exp2: lib={}, file={}",ln.strip())
   					lib_name=parsed[0]
   					data_name=parsed[1]
   				# Found timed out experiment, parse filename instead
   				elif "Timeout" in ln:
   					parsed=parse.parse(log_path+"exp2/2_{}_{}_{}.txt",filename)
   					lib_name=parsed[1]
   					data_name=parsed[0]
   					# Programming language should be on parsed[2] if necessary
   					break
   				# Should reach here after done with header
   				# Line 1: loading time
   				if "Loading time" in ln:
   					parsed=parse.parse("Loading time (in sec.): {}",ln.strip())
   					if not parsed is None:
   						load_time=parsed[0]
   				# Line 2: loading memory
   				if "Loading mem" in ln:
   					parsed=parse.parse("Loading mem curr (in bytes): {}",ln.strip())
   					if not parsed is None:
   						load_mem=parsed[0]
   				# Line 3: aggregation time
   				if "Degree time" in ln:
   					parsed=parse.parse("Degree time (in sec.): {}",ln.strip())
   					if not parsed is None:
   						degr_time=parsed[0]
   				# Line 4: aggregation memory
   				if "Degree mem" in ln:
   					parsed=parse.parse("Degree mem curr (in bytes): {}",ln.strip())
   					if not parsed is None:
   						degr_mem=parsed[0]
   			# Done with lines- add into dataframe
   			df.loc[len(df)]={"dataset":data_name,"library":lib_name,"load_time":float(load_time),"load_mem":int(load_mem),"degr_time":float(degr_time),"degr_mem":int(degr_mem)}

   	# Done with all files. Aggregate total times. Visualize. 
	df["total_time"]=df.apply(lambda r: r.load_time+r.degr_time, axis=1)
	df.dropna()

	# Sort by dataset and library
	df=df.sort_values(["dataset","library"])

	# Write dataframe to csv file
	df.to_csv(out_file,sep=" ",index=False)
	return

# Result parser Exp3
def parse_exp3(out_file):
	return


# Result parser Exp4
def parse_exp4(out_file):
	global log_path
	df=pd.DataFrame(columns=["dataset","library","genr_time","genr_mem","aggr_time","aggr_mem"])
	# Open all logfiles in path
	for filename in glob.glob(log_path+"exp4/4_*.txt"):
		with open(filename,'r') as f: 
   			# Find line starting with Exp1:
   			header_found=0
   			lib_name=""
   			data_name=""
   			genr_time=0.0
   			genr_mem=0
   			aggr_time=0.0
   			aggr_mem=0
   			for ln in f.readlines():
   				if header_found==0 and not("Exp4:" in ln):
   					continue
   				elif "Exp4:" in ln:
   					header_found=1
   					parsed=parse.parse("Exp4: lib={}, file={}",ln.strip())
   					lib_name=parsed[0]
   					data_name=parsed[1]
   				# Found timed out experiment, parse filename instead
   				elif "Timeout" in ln:
   					parsed=parse.parse(log_path+"exp4/4_{}_{}_{}.txt",filename)
   					lib_name=parsed[1]
   					data_name=parsed[0]
   					# Programming language should be on parsed[2] if necessary
   					break
   				# Should reach here after done with header
   				# Line 1: generation time
   				if "Generate time" in ln:
   					parsed=parse.parse("Generate time (in sec.): {}",ln.strip())
   					if not parsed is None:
   						genr_time=parsed[0]
   				# Line 2: generation memory
   				if "Generate mem" in ln:
   					parsed=parse.parse("Generate mem curr (in bytes): {}",ln.strip())
   					if not parsed is None:
   						genr_mem=parsed[0]
   				# Line 3: aggregation time
   				if "Aggregate time" in ln:
   					parsed=parse.parse("Aggregate time (in sec.): {}",ln.strip())
   					if not parsed is None:
   						aggr_time=parsed[0]
   				# Line 4: aggregation memory
   				if "Aggregate mem" in ln:
   					parsed=parse.parse("Aggregate mem curr (in bytes): {}",ln.strip())
   					if not parsed is None:
   						aggr_mem=parsed[0]
   			# Done with lines- add into dataframe
   			df.loc[len(df)]={"dataset":data_name,"library":lib_name,"genr_time":float(genr_time),"genr_mem":int(genr_mem),"aggr_time":float(aggr_time),"aggr_mem":int(aggr_mem)}

   	# Done with all files. Aggregate total times. Visualize. 
	df["total_time"]=df.apply(lambda r: r.genr_time+r.aggr_time, axis=1)
	df.dropna()

	# Sort by dataset and library
	df=df.sort_values(["dataset","library"])

	# Write dataframe to csv file
	df.to_csv(out_file,sep=" ",index=False)
	return

# Result parser, Exp 5
def parse_exp5(out_file):
	global log_path
	df=pd.DataFrame(columns=["dataset","library","genr_time","genr_mem","degr_time","degr_mem"])
	# Open all logfiles in path
	for filename in glob.glob(log_path+"exp5/5_*.txt"):
		with open(filename,'r') as f: 
   			# Find line starting with Exp1:
   			header_found=0
   			lib_name=""
   			data_name=""
   			genr_time=0.0
   			genr_mem=0
   			degr_time=0.0
   			degr_mem=0
   			for ln in f.readlines():
   				if header_found==0 and not("Exp5:" in ln):
   					continue
   				elif "Exp5:" in ln:
   					header_found=1
   					parsed=parse.parse("Exp5: lib={}, file={}",ln.strip())
   					lib_name=parsed[0]
   					data_name=parsed[1]
   				# Found timed out experiment, parse filename instead
   				elif "Timeout" in ln:
   					parsed=parse.parse(log_path+"exp5/5_{}_{}_{}.txt",filename)
   					lib_name=parsed[1]
   					data_name=parsed[0]
   					# Programming language should be on parsed[2] if necessary
   					break
   				# Should reach here after done with header
   				# Line 1: generation time
   				if "Generate time" in ln:
   					parsed=parse.parse("Generate time (in sec.): {}",ln.strip())
   					if not parsed is None:
   						genr_time=parsed[0]
   				# Line 2: generation memory
   				if "Generate mem" in ln:
   					parsed=parse.parse("Generate mem curr (in bytes): {}",ln.strip())
   					if not parsed is None:
   						genr_mem=parsed[0]
   				# Line 3: aggregation time
   				if "Degree time" in ln:
   					parsed=parse.parse("Degree time (in sec.): {}",ln.strip())
   					if not parsed is None:
   						degr_time=parsed[0]
   				# Line 4: aggregation memory
   				if "Degree mem" in ln:
   					parsed=parse.parse("Degree mem curr (in bytes): {}",ln.strip())
   					if not parsed is None:
   						degr_mem=parsed[0]
   			# Done with lines- add into dataframe
   			df.loc[len(df)]={"dataset":data_name,"library":lib_name,"genr_time":float(genr_time),"genr_mem":int(genr_mem),"degr_time":float(degr_time),"degr_mem":int(degr_mem)}

   	# Done with all files. Aggregate total times. Visualize. 
	df["total_time"]=df.apply(lambda r: r.genr_time+r.degr_time, axis=1)
	df.dropna()

	# Sort by dataset and library
	df=df.sort_values(["dataset","library"])

	# Write dataframe to csv file
	df.to_csv(out_file,sep=" ",index=False)
	return


# Portland, Main(e)
def main():
	# Parse exp1 file
	parse_exp1("../logs/exp1.txt")

	# Parse exp2 file
	parse_exp2("../logs/exp2.txt")

	# Parse exp4 file
	parse_exp4("../logs/exp4.txt")

	# Parse exp5 file
	parse_exp5("../logs/exp5.txt")

	return

# Python stuff
if __name__ == "__main__":
	main()

