import os, glob
import parse
import pandas as pd
import numpy as np
import time
from matplotlib import pyplot as plt

# Path to log exports
log_path="../logs/"

# Result parser
def parse_exp1(out1,out2):
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
				# Found timed out experiment, parse filename instead
				if "Timeout" in ln or "Killed" in ln:
					parsed=parse.parse(log_path+"exp1/1_{}_{}_{}.txt",filename)
					lib_name=parsed[1]
					data_name=parsed[0]
					# Programming language should be on parsed[2] if necessary
					break
				elif header_found==0 and not("Exp1:" in ln):
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
	# Sort by dataset and library. Only extract times
	df=df.sort_values(["dataset","library"])
	df=df[["dataset","library","load_time","aggr_time"]]

	# Split into two dataframes for experiments
	# df1: Small datasets (aucs,london,euair)
	# df2: Large datasets (fftw,ff)
	df1=df[df["dataset"].isin(["aucs","london","euair"])]
	df2=df[df["dataset"].isin(["fftw","ff"])]

	# Convert library values to single cols
	ncols1={}
	# Group the DataFrame by 'lib' column and iterate over groups
	for group, data in df1.groupby("library"):
		# Extract columns, and store them in new columns
		ncols1[f"{group}_load"]=data["load_time"].tolist()
		ncols1[f"{group}_aggr"]=data["aggr_time"].tolist()
	plot_df1=pd.DataFrame(ncols1)
	plot_df1["dataset"]=df1["dataset"].unique()
	
	ncols2={}
	# Group the DataFrame by 'lib' column and iterate over groups
	for group, data in df2.groupby("library"):
		# Extract columns, and store them in new columns
		ncols2[f"{group}_load"]=data["load_time"].tolist()
		ncols2[f"{group}_aggr"]=data["aggr_time"].tolist()
	plot_df2=pd.DataFrame(ncols2)
	plot_df2["dataset"]=df2["dataset"].unique()

	# Write dataframes to csv files
	plot_df1.to_csv(out1,sep=" ",index=False)
	plot_df2.to_csv(out2,sep=" ",index=False)

	return

# Result parser, Exp 2
def parse_exp2(out1,out2):
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
				# Found timed out experiment, parse filename instead
				if "Timeout" in ln or "Killed" in ln:
					parsed=parse.parse(log_path+"exp2/2_{}_{}_{}.txt",filename)
					lib_name=parsed[1]
					data_name=parsed[0]
					# Programming language should be on parsed[2] if necessary
					break
				elif header_found==0 and not("Exp2:" in ln):
					continue
				elif "Exp2:" in ln:
					header_found=1
					parsed=parse.parse("Exp2: lib={}, file={}",ln.strip())
					lib_name=parsed[0]
					data_name=parsed[1]
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
	# Done with all files. Aggregate total times.
	df["total_time"]=df.apply(lambda r: r.load_time+r.degr_time, axis=1)
	df.dropna()
	# Sort by dataset and library. Only extract times
	df=df.sort_values(["dataset","library"])
	df=df[["dataset","library","load_time","degr_time"]]

	# Split into two dataframes for experiments
	# df1: Small datasets (aucs,london,euair)
	# df2: Large datasets (fftw,ff)
	df1=df[df["dataset"].isin(["aucs","london","euair"])]
	df2=df[df["dataset"].isin(["fftw","ff"])]

	# Convert library values to single cols
	ncols1={}
	# Group the DataFrame by 'lib' column and iterate over groups
	for group, data in df1.groupby("library"):
		# Extract columns, and store them in new columns
		ncols1[f"{group}_load"]=data["load_time"].tolist()
		ncols1[f"{group}_degr"]=data["degr_time"].tolist()
	plot_df1=pd.DataFrame(ncols1)
	plot_df1["dataset"]=df1["dataset"].unique()
	
	ncols2={}
	# Group the DataFrame by 'lib' column and iterate over groups
	for group, data in df2.groupby("library"):
		# Extract columns, and store them in new columns
		ncols2[f"{group}_load"]=data["load_time"].tolist()
		ncols2[f"{group}_degr"]=data["degr_time"].tolist()
	plot_df2=pd.DataFrame(ncols2)
	plot_df2["dataset"]=df2["dataset"].unique()

	# Write dataframes to csv files
	plot_df1.to_csv(out1,sep=" ",index=False)
	plot_df2.to_csv(out2,sep=" ",index=False)
	return

# Result parser Exp3
def parse_exp3(out_file):
	return


# Result parser Exp4
def parse_exp4(out1,out2):
	global log_path
	df=pd.DataFrame(columns=["node_size","layer_size","library","genr_time","genr_mem","aggr_time","aggr_mem"])
	# Open all logfiles in path
	for filename in glob.glob(log_path+"exp4/4_*.txt"):
		with open(filename,'r') as f: 
			# Find line starting with Exp1:
			header_found=0
			lib_name=""
			data_name=""
			node_size=0
			layer_size=0
			genr_time=0.0
			genr_mem=0
			aggr_time=0.0
			aggr_mem=0
			for ln in f.readlines():
				# Found timed out experiment, parse filename instead
				if "Timeout" in ln or "Killed" in ln:
					parsed=parse.parse(log_path+"exp4/4_{}_{}_{}.txt",filename)
					lib_name=parsed[1]
					data_name=parsed[0]
					# Programming language should be on parsed[2] if necessary
					break
				elif header_found==0 and not("Exp4:" in ln):
					continue
				elif "Exp4:" in ln:
					header_found=1
					parsed=parse.parse("Exp4: lib={}, file={}",ln.strip())
					lib_name=parsed[0]
					data_name=parsed[1]
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
			
			# Split tokens
			toks=data_name.split("-")
			node_size=int(toks[0])
			layer_size=int(toks[1])

			# Done with lines- add into dataframe
			df.loc[len(df)]={"node_size":node_size,"layer_size":layer_size,"library":lib_name,"genr_time":float(genr_time),"genr_mem":int(genr_mem),"aggr_time":float(aggr_time),"aggr_mem":int(aggr_mem)}

	# Done with all files. Aggregate total times. Visualize. 
	df["total_time"]=df.apply(lambda r: r.genr_time+r.aggr_time, axis=1)
	df.dropna()

	# Split into two dataframes for experiments
	# df1: Layers=2, Nodes=[1000,100000], Edges=sqrt(Nodes)
	# df2: Nodes=1000, Layers=[2,1000], Edges=sqrt(Nodes)
	df1=df[df["layer_size"]==2]
	df2=df[df["node_size"]==1000]

	# Sort by node size and library. Only extract times
	df1=df1.sort_values(["node_size","library"])
	df1=df1[["node_size","library","genr_time","aggr_time"]]
	# Sort by layer size and library. Only keep times
	df2=df2.sort_values(["layer_size","library"])
	df2t=df2[["layer_size","library","genr_time","aggr_time"]]

	# Convert library values to single cols
	ncols1={}
	# Group the DataFrame by 'lib' column and iterate over groups
	for group, data in df1.groupby("library"):
		# Extract columns, and store them in new columns
		ncols1[f"{group}_genr"]=data["genr_time"].tolist()
		ncols1[f"{group}_aggr"]=data["aggr_time"].tolist()
	plot_df1=pd.DataFrame(ncols1)
	plot_df1["node_size"]=df1["node_size"].unique()
	
	ncols2={}
	# Group the DataFrame by 'lib' column and iterate over groups
	for group, data in df2.groupby("library"):
		# Extract columns, and store them in new columns
		ncols2[f"{group}_genr"]=data["genr_time"].tolist()
		ncols2[f"{group}_aggr"]=data["aggr_time"].tolist()
	plot_df2=pd.DataFrame(ncols2)
	plot_df2["layer_size"]=df2["layer_size"].unique()

	# Write dataframes to csv files
	plot_df1.to_csv(out1,sep=" ",index=False)
	plot_df2.to_csv(out2,sep=" ",index=False)
	return

# Result parser, Exp 5
def parse_exp5(out1,out2):
	global log_path
	df=pd.DataFrame(columns=["node_size","layer_size","library","genr_time","genr_mem","degr_time","degr_mem"])
	# Open all logfiles in path
	for filename in glob.glob(log_path+"exp5/5_*.txt"):
		with open(filename,'r') as f: 
			# Find line starting with Exp1:
			header_found=0
			lib_name=""
			data_name=""
			layer_size=0
			node_size=0
			genr_time=0.0
			genr_mem=0
			degr_time=0.0
			degr_mem=0
			for ln in f.readlines():
				# Found timed out experiment, parse filename instead
				if "Timeout" in ln or "Killed" in ln:
					parsed=parse.parse(log_path+"exp5/5_{}_{}_{}.txt",filename)
					lib_name=parsed[1]
					data_name=parsed[0]
					# Programming language should be on parsed[2] if necessary
					break
				elif header_found==0 and not("Exp5:" in ln):
					continue
				elif "Exp5:" in ln:
					header_found=1
					parsed=parse.parse("Exp5: lib={}, file={}",ln.strip())
					lib_name=parsed[0]
					data_name=parsed[1]
				
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
			
			# Split tokens
			toks=data_name.split("-")
			node_size=int(toks[0])
			layer_size=int(toks[1])

			# Done with lines- add into dataframe
			df.loc[len(df)]={"node_size":node_size,"layer_size":layer_size,"library":lib_name,"genr_time":float(genr_time),"genr_mem":int(genr_mem),"degr_time":float(degr_time),"degr_mem":int(degr_mem)}

   # Done with all files. Aggregate total times. Visualize. 
	df["total_time"]=df.apply(lambda r: r.genr_time+r.degr_time, axis=1)
	df.dropna()

	# Split into two dataframes for experiments
	# df1: Layers=2, Nodes=[1000,100000], Edges=sqrt(Nodes)
	# df2: Nodes=1000, Layers=[2,1000], Edges=sqrt(Nodes)
	df1=df[df["layer_size"]==2]
	df2=df[df["node_size"]==1000]

	# Sort by node size and library. Only extract times
	df1=df1.sort_values(["node_size","library"])
	df1=df1[["node_size","library","genr_time","degr_time"]]
	# Sort by layer size and library. Only keep times
	df2=df2.sort_values(["layer_size","library"])
	df2t=df2[["layer_size","library","genr_time","degr_time"]]

	# Convert library values to single cols
	ncols1={}
	# Group the DataFrame by 'lib' column and iterate over groups
	for group, data in df1.groupby("library"):
		# Extract columns, and store them in new columns
		ncols1[f"{group}_genr"]=data["genr_time"].tolist()
		ncols1[f"{group}_degr"]=data["degr_time"].tolist()
	plot_df1=pd.DataFrame(ncols1)
	plot_df1["node_size"]=df1["node_size"].unique()
	
	ncols2={}
	# Group the DataFrame by 'lib' column and iterate over groups
	for group, data in df2.groupby("library"):
		# Extract columns, and store them in new columns
		ncols2[f"{group}_genr"]=data["genr_time"].tolist()
		ncols2[f"{group}_degr"]=data["degr_time"].tolist()
	plot_df2=pd.DataFrame(ncols2)
	plot_df2["layer_size"]=df2["layer_size"].unique()

	# Write dataframes to csv files
	plot_df1.to_csv(out1,sep=" ",index=False)
	plot_df2.to_csv(out2,sep=" ",index=False)
	return

# Result parser, Exp 6
def parse_exp6(out1,out2,out3,out4):
	global log_path
	df=pd.DataFrame(columns=["node_size","edge_size","layer_size","library","load_time","load_mem","aggr_time","aggr_mem"])
	# Open all logfiles in path
	for filename in glob.glob(log_path+"exp6/6_*.txt"):
		with open(filename,'r') as f: 
			# Find line starting with Exp1:
			header_found=0
			lib_name=""
			data_name=""
			layer_size=0
			node_size=0
			edge_size=""
			load_time=0.0
			load_mem=0
			aggr_time=0.0
			aggr_mem=0
			for ln in f.readlines():
				# Found timed out experiment, parse filename instead
				if "Timeout" in ln or "Killed" in ln:
					parsed=parse.parse(log_path+"exp6/6_{}_{}_{}.txt",filename)
					lib_name=parsed[1]
					data_name=parsed[0]
					# Programming language should be on parsed[2] if necessary
					break
				elif header_found==0 and not("Exp6:" in ln):
					continue
				elif "Exp6:" in ln:
					header_found=1
					parsed=parse.parse("Exp6: lib={}, file={}",ln.strip())
					lib_name=parsed[0]
					data_name=parsed[1]
				
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
			
			# Split tokens
			toks=data_name.split("-")
			node_size=int(toks[0])
			edge_size=toks[1]
			layer_size=int(toks[2])

			# Done with lines- add into dataframe
			df.loc[len(df)]={"node_size":node_size,"edge_size":edge_size,"layer_size":layer_size,"library":lib_name,"load_time":float(load_time),"load_mem":int(load_mem),"aggr_time":float(aggr_time),"aggr_mem":int(aggr_mem)}

   # Done with all files. Aggregate total times. Visualize. 
	df["total_time"]=df.apply(lambda r: r.load_time+r.aggr_time, axis=1)
	df.dropna()

	# Split into four dataframes for experiments, according to runs
	# df1: n=[1000-10M], e=4, l=2
	# df2: n=[1000-100K], e=s, l=2
	# df3: n=1000, e=4, l=[2,10000]
	# df4: n=1000, e=s, l=[2,10000]
	df1=df[(df["layer_size"]==2) & (df["edge_size"]=="4")]
	df2=df[(df["layer_size"]==2) & (df["edge_size"]=="s")]
	df3=df[(df["node_size"]==1000) & (df["edge_size"]=="4")]
	df4=df[(df["node_size"]==1000) & (df["edge_size"]=="s")]

	# Sort by node size and library. Only extract times
	df1=df1.sort_values(["node_size","library"])
	df1=df1[["node_size","library","load_time","aggr_time"]]
	# Sort by node size and library. Only extract times
	df2=df2.sort_values(["node_size","library"])
	df2=df2[["node_size","library","load_time","aggr_time"]]
	
	# Sort by layer size and library. Only keep times
	df3=df3.sort_values(["layer_size","library"])
	df3=df3[["layer_size","library","load_time","aggr_time"]]
	# Sort by layer size and library. Only keep times
	df4=df4.sort_values(["layer_size","library"])
	df4=df4[["layer_size","library","load_time","aggr_time"]]


	# Convert library values to single cols
	ncols1={}
	# Group the DataFrame by 'lib' column and iterate over groups
	for group, data in df1.groupby("library"):
		# Extract columns, and store them in new columns
		ncols1[f"{group}_load"]=data["load_time"].tolist()
		ncols1[f"{group}_aggr"]=data["aggr_time"].tolist()
	plot_df1=pd.DataFrame(ncols1)
	plot_df1["node_size"]=df1["node_size"].unique()
	
	# Convert library values to single cols
	ncols2={}
	# Group the DataFrame by 'lib' column and iterate over groups
	for group, data in df2.groupby("library"):
		# Extract columns, and store them in new columns
		ncols2[f"{group}_load"]=data["load_time"].tolist()
		ncols2[f"{group}_aggr"]=data["aggr_time"].tolist()
	plot_df2=pd.DataFrame(ncols2)
	plot_df2["node_size"]=df2["node_size"].unique()

	ncols3={}
	# Group the DataFrame by 'lib' column and iterate over groups
	for group, data in df3.groupby("library"):
		# Extract columns, and store them in new columns
		ncols3[f"{group}_load"]=data["load_time"].tolist()
		ncols3[f"{group}_aggr"]=data["aggr_time"].tolist()
	plot_df3=pd.DataFrame(ncols3)
	plot_df3["layer_size"]=df3["layer_size"].unique()

	ncols4={}
	# Group the DataFrame by 'lib' column and iterate over groups
	for group, data in df4.groupby("library"):
		# Extract columns, and store them in new columns
		ncols4[f"{group}_load"]=data["load_time"].tolist()
		ncols4[f"{group}_aggr"]=data["aggr_time"].tolist()
	plot_df4=pd.DataFrame(ncols4)
	plot_df4["layer_size"]=df4["layer_size"].unique()

	# Write dataframes to csv files
	plot_df1.to_csv(out1,sep=" ",index=False)
	plot_df2.to_csv(out2,sep=" ",index=False)
	plot_df3.to_csv(out3,sep=" ",index=False)
	plot_df4.to_csv(out4,sep=" ",index=False)
	return

# Result parser, Exp 7
def parse_exp7(out1,out2,out3,out4):
	global log_path
	df=pd.DataFrame(columns=["node_size","edge_size","layer_size","library","load_time","load_mem","degr_time","degr_mem"])
	# Open all logfiles in path
	for filename in glob.glob(log_path+"exp7/7_*.txt"):
		with open(filename,'r') as f: 
			# Find line starting with Exp1:
			header_found=0
			lib_name=""
			data_name=""
			layer_size=0
			node_size=0
			edge_size=""
			load_time=0.0
			load_mem=0
			degr_time=0.0
			degr_mem=0
			for ln in f.readlines():
				# Found timed out experiment, parse filename instead
				if "Timeout" in ln or "Killed" in ln:
					parsed=parse.parse(log_path+"exp7/7_{}_{}_{}.txt",filename)
					lib_name=parsed[1]
					data_name=parsed[0]
					# Programming language should be on parsed[2] if necessary
					break
				elif header_found==0 and not("Exp7:" in ln):
					continue
				elif "Exp7:" in ln:
					header_found=1
					parsed=parse.parse("Exp7: lib={}, file={}",ln.strip())
					lib_name=parsed[0]
					data_name=parsed[1]
				
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
			
			# Split tokens
			toks=data_name.split("-")
			node_size=int(toks[0])
			edge_size=toks[1]
			layer_size=int(toks[2])

			# Done with lines- add into dataframe
			df.loc[len(df)]={"node_size":node_size,"edge_size":edge_size,"layer_size":layer_size,"library":lib_name,"load_time":float(load_time),"load_mem":int(load_mem),"degr_time":float(degr_time),"degr_mem":int(degr_mem)}

   # Done with all files. Aggregate total times. Visualize. 
	df["total_time"]=df.apply(lambda r: r.load_time+r.degr_time, axis=1)
	df.dropna()

	# Split into four dataframes for experiments, according to runs
	# df1: n=[1000-10M], e=4, l=2
	# df2: n=[1000-100K], e=s, l=2
	# df3: n=1000, e=4, l=[2,10000]
	# df4: n=1000, e=s, l=[2,10000]
	df1=df[(df["layer_size"]==2) & (df["edge_size"]=="4")]
	df2=df[(df["layer_size"]==2) & (df["edge_size"]=="s")]
	df3=df[(df["node_size"]==1000) & (df["edge_size"]=="4")]
	df4=df[(df["node_size"]==1000) & (df["edge_size"]=="s")]

	# Sort by node size and library. Only extract times
	df1=df1.sort_values(["node_size","library"])
	df1=df1[["node_size","library","load_time","degr_time"]]
	# Sort by node size and library. Only extract times
	df2=df2.sort_values(["node_size","library"])
	df2=df2[["node_size","library","load_time","degr_time"]]
	
	# Sort by layer size and library. Only keep times
	df3=df3.sort_values(["layer_size","library"])
	df3=df3[["layer_size","library","load_time","degr_time"]]
	# Sort by layer size and library. Only keep times
	df4=df4.sort_values(["layer_size","library"])
	df4=df4[["layer_size","library","load_time","degr_time"]]


	# Convert library values to single cols
	ncols1={}
	# Group the DataFrame by 'lib' column and iterate over groups
	for group, data in df1.groupby("library"):
		# Extract columns, and store them in new columns
		ncols1[f"{group}_load"]=data["load_time"].tolist()
		ncols1[f"{group}_degr"]=data["degr_time"].tolist()
	plot_df1=pd.DataFrame(ncols1)
	plot_df1["node_size"]=df1["node_size"].unique()
	
	# Convert library values to single cols
	ncols2={}
	# Group the DataFrame by 'lib' column and iterate over groups
	for group, data in df2.groupby("library"):
		# Extract columns, and store them in new columns
		ncols2[f"{group}_load"]=data["load_time"].tolist()
		ncols2[f"{group}_degr"]=data["degr_time"].tolist()
	plot_df2=pd.DataFrame(ncols2)
	plot_df2["node_size"]=df2["node_size"].unique()

	ncols3={}
	# Group the DataFrame by 'lib' column and iterate over groups
	for group, data in df3.groupby("library"):
		# Extract columns, and store them in new columns
		ncols3[f"{group}_load"]=data["load_time"].tolist()
		ncols3[f"{group}_degr"]=data["degr_time"].tolist()
	plot_df3=pd.DataFrame(ncols3)
	plot_df3["layer_size"]=df3["layer_size"].unique()

	ncols4={}
	# Group the DataFrame by 'lib' column and iterate over groups
	for group, data in df4.groupby("library"):
		# Extract columns, and store them in new columns
		ncols4[f"{group}_load"]=data["load_time"].tolist()
		ncols4[f"{group}_degr"]=data["degr_time"].tolist()
	plot_df4=pd.DataFrame(ncols4)
	plot_df4["layer_size"]=df4["layer_size"].unique()


	# Write dataframes to csv files
	plot_df1.to_csv(out1,sep=" ",index=False)
	plot_df2.to_csv(out2,sep=" ",index=False)
	plot_df3.to_csv(out3,sep=" ",index=False)
	plot_df4.to_csv(out4,sep=" ",index=False)
	return

# Open logfiles from exp6 and compare network loading times for all experiments. 
# 	Only output the smallest in the logfile (assuming no timeout/OOM error, 
# 	which would be 0). This is done for plotting purposes, as the network loading 
#	time is generated from Exp7 final plots.
def compare_load(in6a,in6b,in6c,in6d,in7a,in7b,in7c,in7d,out1,out2,out3,out4):
	# Read files
	df61=pd.read_csv(in6a,sep=" ",header=0)
	df62=pd.read_csv(in6b,sep=" ",header=0)
	df63=pd.read_csv(in6c,sep=" ",header=0)
	df64=pd.read_csv(in6d,sep=" ",header=0)
	df71=pd.read_csv(in7a,sep=" ",header=0)
	df72=pd.read_csv(in7b,sep=" ",header=0)
	df73=pd.read_csv(in7c,sep=" ",header=0)
	df74=pd.read_csv(in7d,sep=" ",header=0)

	# Fix 7_1 (n++,e=4,l=2)
	print(df71)

	mask = (df71["multinet_load"] > df61["multinet_load"]) & (df61["multinet_load"]!=0) | (df71["multinet_load"]==0)
	df71.loc[mask,"multinet_load"] = df61.loc[mask,"multinet_load"]
	#df71["multinet_load"]=df71.apply(lambda x:df71.loc[x.name,"multinet_load"] if mask[x.name] else x["multinet_load"], axis=1)
	
	print(mask)
	print(df61["multinet_load"])
	print(df71["multinet_load"])
	print(df71)

	mask = (df71["muxviz_load"] > df61["muxviz_load"]) & (df61["muxviz_load"]!=0) | (df71["muxviz_load"]==0)
	df71.loc[mask,"muxviz_load"] = df61.loc[mask,"muxviz_load"]

	print(mask)
	print(df61["muxviz_load"])
	print(df71["muxviz_load"])
	print(df71)

	#df71["muxviz_load"]=df71.apply(lambda x:df71.loc[x.name,"muxviz_load"] if mask[x.name] else x["multinet_load"], axis=1)
	mask = (df71["pymnet_load"] > df61["pymnet_load"]) & (df61["pymnet_load"]!=0) | (df71["pymnet_load"]==0)
	df71.loc[mask,"pymnet_load"] = df61.loc[mask,"pymnet_load"]
	#df71["multinet_load"]=df71.apply(lambda x:df71.loc[x.name,"multinet_load"] if mask[x.name] else x["muxviz_load"], axis=1)
	mask = (df71["py3plex_load"] > df61["py3plex_load"]) & (df61["py3plex_load"]!=0) | (df71["py3plex_load"]==0)
	df71.loc[mask,"py3plex_load"] = df61.loc[mask,"py3plex_load"]
	#df71["multinet_load"]=df71.apply(lambda x:df71.loc[x.name,"multinet_load"] if mask[x.name] else x["multinet_load"], axis=1)

	# Fix 7_2 (n++,e=s,l=2)
	mask = (df72["multinet_load"] > df62["multinet_load"]) & (df62["multinet_load"]!=0) | (df72["multinet_load"]==0)
	df72.loc[mask,"multinet_load"] = df62.loc[mask,"multinet_load"]
	mask = (df72["muxviz_load"] > df62["muxviz_load"]) & (df62["muxviz_load"]!=0) | (df72["muxviz_load"]==0)
	df72.loc[mask,"muxviz_load"] = df62.loc[mask,"muxviz_load"]
	mask = (df72["pymnet_load"] > df62["pymnet_load"]) & (df62["pymnet_load"]!=0) | (df72["pymnet_load"]==0)
	df72.loc[mask,"pymnet_load"] = df62.loc[mask,"pymnet_load"]
	mask = (df72["py3plex_load"] > df62["py3plex_load"]) & (df62["py3plex_load"]!=0) | (df72["py3plex_load"]==0)
	df72.loc[mask,"py3plex_load"] = df62.loc[mask,"py3plex_load"]

	# Fix 7_3 (n=1000,e=4,l++)
	mask = (df73["multinet_load"] > df63["multinet_load"]) & (df63["multinet_load"]!=0) | (df73["multinet_load"]==0)
	df73.loc[mask,"multinet_load"] = df63.loc[mask,"multinet_load"]
	mask = (df73["muxviz_load"] > df63["muxviz_load"]) & (df63["muxviz_load"]!=0) | (df73["muxviz_load"]==0)
	df73.loc[mask,"muxviz_load"] = df63.loc[mask,"muxviz_load"]
	mask = (df73["pymnet_load"] > df63["pymnet_load"]) & (df63["pymnet_load"]!=0) | (df73["pymnet_load"]==0)
	df73.loc[mask,"pymnet_load"] = df63.loc[mask,"pymnet_load"]
	mask = (df73["py3plex_load"] > df63["py3plex_load"]) & (df63["py3plex_load"]!=0) | (df73["py3plex_load"]==0)
	df73.loc[mask,"py3plex_load"] = df63.loc[mask,"py3plex_load"]

	# Fix 7_4 (n=1000,e=s,l++)
	mask = (df74["multinet_load"] > df64["multinet_load"]) & (df64["multinet_load"]!=0) | (df74["multinet_load"]==0)
	df74.loc[mask,"multinet_load"] = df64.loc[mask,"multinet_load"]
	mask = (df74["muxviz_load"] > df64["muxviz_load"]) & (df64["muxviz_load"]!=0) | (df74["muxviz_load"]==0)
	df74.loc[mask,"muxviz_load"] = df64.loc[mask,"muxviz_load"]
	mask = (df74["pymnet_load"] > df64["pymnet_load"]) & (df64["pymnet_load"]!=0) | (df74["pymnet_load"]==0)
	df74.loc[mask,"pymnet_load"] = df64.loc[mask,"pymnet_load"]
	mask = (df74["py3plex_load"] > df64["py3plex_load"]) & (df64["py3plex_load"]!=0) | (df74["py3plex_load"]==0)
	df74.loc[mask,"py3plex_load"] = df64.loc[mask,"py3plex_load"]


	# Write dataframes to csv files
	df71.to_csv(out1,sep=" ",index=False)
	df72.to_csv(out2,sep=" ",index=False)
	df73.to_csv(out3,sep=" ",index=False)
	df74.to_csv(out4,sep=" ",index=False)


# Portland, Main(e)
def main():
	# # Parse exp1 file
	# parse_exp1("../logs/plot_exp1a.txt","../logs/plot_exp1b.txt")

	# # Parse exp2 file
	# parse_exp2("../logs/plot_exp2a.txt","../logs/plot_exp2b.txt")

	# # # Parse exp4 file
	# # parse_exp4("../logs/plot_exp4a.txt","../logs/plot_exp4b.txt")

	# # Parse exp5 file
	# parse_exp5("../logs/plot_exp5a.txt","../logs/plot_exp5b.txt")

	# # Parse exp6 file
	# parse_exp6("../logs/plot_exp6a.txt","../logs/plot_exp6b.txt", "../logs/plot_exp6c.txt", "../logs/plot_exp6d.txt")

	# # Parse exp7 file
	# parse_exp7("../logs/plot_exp7a.txt","../logs/plot_exp7b.txt", "../logs/plot_exp7c.txt", "../logs/plot_exp7d.txt")

	# Fix exp7 files for plotting: 
	compare_load("../logs/plot_exp6a.txt","../logs/plot_exp6b.txt", "../logs/plot_exp6c.txt", "../logs/plot_exp6d.txt",
				"../logs/plot_exp7a.txt","../logs/plot_exp7b.txt", "../logs/plot_exp7c.txt", "../logs/plot_exp7d.txt",
				"../logs/plot_exp7a_comp.txt","../logs/plot_exp7b_comp.txt", "../logs/plot_exp7c_comp.txt", "../logs/plot_exp7d_comp.txt")

	return

# Python stuff
if __name__ == "__main__":
	main()

