# Run all experiments for paper

## Imports ##
import subprocess
import os, glob
import parse
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

## Globals ##

# List of Python libraries for experiments
py_libs=["pymnet","multinet","py3plex","netmem"]
# List of R libraries for experiments
r_libs=["muxviz","multinet","mully"]
# List of Julia libraries for experiments
jl_libs=["mlg"]
# List of all datasets
data_list=["synth","aucs","london","euair","fftw","ff","citation"]

# Path to log exports
log_path="../logs/"

## Auxiliary plot functions ##
# Credit to pascscha for this: https://stackoverflow.com/questions/14270391/how-to-plot-multiple-bars-grouped
def bar_plot(ax, data, colors=None, total_width=0.8, single_width=1, legend=True):
    """Draws a bar plot with multiple bars per data point.

    Parameters
    ----------
    ax : matplotlib.pyplot.axis
        The axis we want to draw our plot on.

    data: dictionary
        A dictionary containing the data we want to plot. Keys are the names of the
        data, the items is a list of the values.

        Example:
        data = {
            "x":[1,2,3],
            "y":[1,2,3],
            "z":[1,2,3],
        }

    colors : array-like, optional
        A list of colors which are used for the bars. If None, the colors
        will be the standard matplotlib color cyle. (default: None)

    total_width : float, optional, default: 0.8
        The width of a bar group. 0.8 means that 80% of the x-axis is covered
        by bars and 20% will be spaces between the bars.

    single_width: float, optional, default: 1
        The relative width of a single bar within a group. 1 means the bars
        will touch eachother within a group, values less than 1 will make
        these bars thinner.

    legend: bool, optional, default: True
        If this is set to true, a legend will be added to the axis.
    """

    # Check if colors where provided, otherwhise use the default color cycle
    if colors is None:
        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    # Number of bars per group
    n_bars = len(data)

    # The width of a single bar
    bar_width = total_width / n_bars

    # List containing handles for the drawn bars, used for the legend
    bars = []

    # Iterate over all data
    for i, (name, values) in enumerate(data.items()):
        # The offset in x direction of that bar
        x_offset = (i - n_bars / 2) * bar_width + bar_width / 2

        # Draw a bar for every value of that type
        for x, y in enumerate(values):
            bar = ax.bar(x + x_offset, y, width=bar_width * single_width, color=colors[i % len(colors)])

        # Add a handle to the last drawn bar, which we'll need for the legend
        bars.append(bar[0])

    # Draw legend if we need
    if legend:
        ax.legend(bars, data.keys())


# if __name__ == "__main__":
#     # Usage example:
#     data = {
#         "a": [1, 2, 3, 2, 1],
#         "b": [2, 3, 4, 3, 1],
#         "c": [3, 2, 1, 4, 2],
#         "d": [5, 9, 2, 1, 8],
#         "e": [1, 3, 2, 2, 3],
#         "f": [4, 3, 1, 1, 4],
#     }

#     fig, ax = plt.subplots()
#     bar_plot(ax, data, total_width=.8, single_width=.9)
#     plt.show()

## Execute experiments ##
# Warning: writing to a log file (specifically, decoding the bytestring returned
# 	from calling subprocess shell) assumes a utf-8 encoding. Should be ok in the vast 
#	majority of cases.
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
				res=subprocess.check_output(runpy,shell=True,stderr=subprocess.STDOUT)
				# Save output to logpath.
				# File naming format: eid_ds(-size)_lib_lang.txt
				with open(logwd+str(e_id)+"_"+ds+"_"+py_lib+"_py.txt","w") as wf:
					wf.write(res.decode("utf-8"))
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
		# Run on all R libs
		for r_lib in rlibs:
			# Generate command and open shell
			runr=cmdbase_r+str(e_id)+" "+r_lib+" "+ds
			try:
				res=subprocess.check_output(runr,shell=True,stderr=subprocess.STDOUT)
				# Save output to logpath.
				# File naming format: eid_ds(-size)_lib_lang.txt
				with open(logwd+str(e_id)+"_"+ds+"_"+r_lib+"_r.txt","w") as wf:
					wf.write(res.decode("utf-8"))
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
		# Run on all Julia libs
		for jl_lib in jllibs:
			# Generate command and open shell
			runjl=cmdbase_jl+str(e_id)+" "+jl_lib+" "+ds
			try:
				res=subprocess.check_output(runjl,shell=True,stderr=subprocess.STDOUT)
				# Save output to logpath.
				# File naming format: eid_ds(-size)_lib_lang.txt
				with open(logwd+str(e_id)+"_"+ds+"_"+jl_lib+"_jl.txt","w") as wf:
					wf.write(res.decode("utf-8"))
					wf.close()
			except subprocess.CalledProcessError as e:
				# Save error to logpath.
				with open(logwd+str(e_id)+"_"+ds+"_"+jl_lib+"_jl.txt","w"	) as wf:
					if e.stdout!=None:
						wf.write(e.stdout.decode("utf-8"))
						wf.write("\n---------------------------\n")
					if e.stderr!=None:
						wf.write(e.stderr.decode("utf-8"))
						wf.write("\n---------------------------\n")
					wf.close()		

	return

# Result parser
def parse_exp1(datasets,library_colors):
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
   				# Should reach here after done with header
   				# Line 1: loading time
   				if "Loading time" in ln:
   					parsed=parse.parse("Loading time (in sec.): {}",ln.strip())
   					load_time=parsed[0]
   				# Line 2: loading memory
   				if "Loading mem" in ln:
   					parsed=parse.parse("Loading mem curr (in bytes): {}",ln.strip())
   					load_mem=parsed[0]
   				# Line 3: aggregation time
   				if "Aggregate time" in ln:
   					parsed=parse.parse("Aggregate time (in sec.): {}",ln.strip())
   					aggr_time=parsed[0]
   				# Line 4: aggregation memory
   				if "Aggregate mem" in ln:
   					parsed=parse.parse("Aggregate mem curr (in bytes): {}",ln.strip())
   					aggr_mem=parsed[0]
   			# Done with lines- add into dataframe
   			df.loc[len(df)]={"dataset":data_name,"library":lib_name,"load_time":float(load_time),"load_mem":int(load_mem),"aggr_time":float(aggr_time),"aggr_mem":int(aggr_mem)}

   	# Done with all files. Aggregate total times. Visualize. 
	df["total_time"]=df.apply(lambda r: r.load_time+r.aggr_time, axis=1)

   	# Not used now, might be useful later.
   	#pvt1=pd.pivot_table(df,columns="dataset",index="library")

   	# Plot: bar chart, performance of network loading + aggregation for libraries.
   	#	 Different datasets. Two plots: one for smaller datasets, one for larger. 
	n_lib=len(library_colors)
	n_dset=len(datasets)
	r = np.arange(n_dset)
	width = 1.0/n_lib
	width_counter=0.0

	df_small = df[["dataset","library","load_time","aggr_time","total_time"]].loc[df["dataset"].isin(["aucs","london","euair"])].sort_values(["dataset","library"])
	



	print(df)
	print(df_small)

	# # Get small datasets plot
	# for d in ["aucs","london","euair"]:
	# 	lib_c=0
	# 	for l in ["multinet","muxviz","pymnet"]:
	# 		m_found=df.loc[df["dataset"]==d]
	# 		row_found=m_found.loc[m_found["library"]==l]
	# 		print(row_found)
	# 		plt.bar(r+width_counter,row_found["total_time"],color=library_colors[lib_c],width=width,edgecolor='black',label=l) 
	# 		lib_c=lib_c+1
	# 		width_counter=width_counter+width

	# plt.xlabel("Dataset") 
	# plt.ylabel("Execution time (sec.)") 
	# plt.title("Performance of network loading and layer aggregation") 
	  
	# #plt.grid(linestyle='--') 
	# plt.xticks(r+width,["aucs","muxviz","pymnet"]) 
	# plt.legend() 
	  
	# plt.show() 

	# Get large datasets plot

	df_large = df[["dataset","library","load_time","aggr_time","total_time"]].loc[df["dataset"].isin(["fftw","ff"])].sort_values(["dataset","library"])
	print(df_large)

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
	#run_exp(1,[],["multinet"],[],["ff"])
	run_exp(1,["py3plex"],[],[],["aucs","london","euair","fftw","ff"])

	# Call plot function for exp1
	#parse_exp1(["aucs","london","euair"],["blue","red","green"])

	return

# Python stuff
if __name__ == "__main__":
	main()