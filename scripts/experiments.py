import sys
import importlib.util

# NOTE: change data path accordingly. This should work if the script is located
#       in scripts/(some_benchmark_folder)/ for the original setup
data_path="../data/"

# Global variables for module importers. See main(.). 
spec=None
module=None

# experiment 1: Load a network and aggregate
def exp1(filenames):
	# Load the file. Time performance, check memory consumption
	tracemalloc.start()
	time_load_s=time.time()
	# --------------------------
	net=module.load(filenames)
	# --------------------------
	time_load_e=time.time()
	time_load_t=time_load_e-time_load_s
	trace_load=tracemalloc.get_traced_memory()
	tracemalloc.stop()

	# Sleep? (To clearly check memory consumption over time). Maybe not needed.

	# Aggregate the network. Time performance, check memory consumption
	tracemalloc.start()
	time_aggr_s=time.time()
	# --------------------------
	net_aggr=module.aggregate(net)
	# --------------------------
	time_aggr_e=time.time()
	time_aggr_t=time_aggr_e-time_aggr_s
	trace_aggr=tracemalloc.get_traced_memory()
	tracemalloc.stop()

	# Print stats.
	print("Loading time: "+str(time_load_t))
	print("Loading mem: "+str(trace_load))
	print("Aggregate time: "+str(time_aggr_t))
	print("Aggregate mem: "+str(trace_aggr))

	# Return aggregated network for debug.
	return net_aggr

# experiment 2: 
def exp2(filenames):
	return

# experiment 3: 
def exp3(filenames):
	return

# experiment 4: 
def exp4(filenames):
	return

# experiment 5: 
def exp5(filenames):
	return

# experiment 6: 
def exp6(filenames):
	return

# experiment 7: 
def exp7(filenames):
	return

# Chicken chow main. Set up so that the same main function template can be used
#   on all experiments; most of the changes need to be done on the load(), 
#   build(), aggregate(), ... and experiment() methods. 
# 
# Expecting commandline arguments for script to run. 
#   Example: python3 experiments.py e_id lib file [size]
#	where:
#		e_id -- The experiment id to run. See details on function comments & paper.
#		lib  -- The Python library to use. Options now: {pymnet, multinet, 
#			netmem, py3plex} 
#		file -- The dataset to use. Options for now: {synth, london, euair, 
#			aucs, fftw, citation, ff}
#		size -- Only applicable for synth; the size (in nodes) of the dataset. 
#			Options for now: {100,200,500,1000,2000,5000,10000,20000,50000}
def main():
	global data_path, spec, module
	filenames=[]

	# Halt if no arguments. Otherwise get arg for file identifier
	if len(sys.argv)<4:
		sys.exit("No file argument given. Available options: {synth N, london, euair, aucs, fftw, citation, ff}")
	e_id=sys.argv[1]
	lib=sys.argv[2]
	file=sys.argv[3]

	### LIBRARY MODULE IMPORTS ###

	# Import library util sources. All source util files contain the functions 
	# 	necessary to run experiments as per the paper.
	# In order to run similar experiments for a new library, one should create 
	#	the file (lib)-util.py with the necessary functions (see all other python
	#	utililty scripts listed here) and import the source code here.
 	# Pymnet import
	if lib=="pymnet":
		spec=importlib.util.spec_from_file_location("pymnet-util","pymnet-util.py")
	# Py3plex import
	elif lib=="py3plex":
		spec=importlib.util.spec_from_file_location("py3plex-util","py3plex-util.py")
	# multinet import
	elif lib=="multinet":
		spec=importlib.util.spec_from_file_location("multinet-util","multinet-util.py")
	# netmem import
	elif lib=="netmem":
		spec=importlib.util.spec_from_file_location("netmem-util","netmem-util.py")
	# Should not reach here
	else:
		return
	module=importlib.util_module_from_spec(spec)
	spec.loader.exec_module(module)


	### DATASET IMPORTS ###

	# Load synthetic multilayer network data. Expect second argument N (size)
	# NOTE: Uncomment (and if necessary, edit) filepaths/input format for library
	if file=="synth":
		n=int(sys.argv[4])
		if n==0:
			sys.exit("No size argument given for synthetic data. Available options: {100,200,500,1000,2000,5000,10000,20000,50000}")

		# 

	# Load London transport data (london-transport).
	elif file=="london":
		filenames=["london-transport/london_transport_nodes.txt","london-transport/london_transport_multiplex.edges","london-transport/london_transport_layers.txt"]
		# filenames=""

	# Load EUAir transport data (euair-transport)
	elif file=="euair":
		filenames=["euair-transport/EUAirTransportation_nodes.txt","euair-transport/EUAirTransportation_multiplex.edges","euair-transport/EUAirTransportation_layers.txt"]
		# filenames=""

	# Load CS@Aarhus data (cs-aarhus)
	elif file=="aucs":
		filenames=["cs-aarhus/CS-Aarhus_nodes.txt","cs-aarhus/CS-Aarhus_multiplex.edges","cs-aarhus/CS-Aarhus_layers.txt"]
		# filenames="cs-aarhus/aucs.mpx"
	
	# Load FriendFeed-Twitter data (ff-tw)
	elif file=="fftw":
		filenames=[]
		# filenames="ff-tw/fftw.mpx"
	
	# Load citation data (journal-citation)
	elif file=="citation":
		filenames=[]
		# filenames=""

	# Load FriendFeed data (friendfeed)
	elif file=="ff":
		filenames=[]
		# filenames=""
	
	# Should not reach here. Add more cases for datasets here.
	else:
		return
	

	### EXPERIMENTS ###

	#Print exp, lib, file stats and call exp# which prints the rest.
	print("Exp"+str(e_id)+": lib="+lib+", file="+file)
	# Experiment 1: Load net from file & aggregate
	if e_id==1:
		exp1(filenames)
	# Experiment 2: 
	elif e_id==2:
		exp2(filenames)
	# Experiment 3: 
	elif e_id==3:
		exp3(filenames)
	# Experiment 4:
	elif e_id==4:
		exp4(filenames)
	# Experiment 5:
	elif e_id==5:
		exp5(filenames)
	# Experiment 6:
	elif e_id==6:
		exp6(filenames)
	# Experiment 7:
	elif e_id==7:
		exp7(filenames)
	# Should not reach here
	else:
		return
	print("-------------------------------")


# Python stuff
if __name__ == "__main__":
	main()