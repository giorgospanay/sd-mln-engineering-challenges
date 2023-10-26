import sys
import importlib.util
# Imports for timing and memory trace
import time
import tracemalloc

# Global variables for module importers. See main(.). 
spec=None
module=None

### EXPERIMENT CODE DEFINITIONS ###
# Use module.[necessary_functions()] to import from different libraries.

# experiment 1: Load a network and aggregate
def exp1(filenames):
	# Load the file. Time performance, check memory consumption
	tracemalloc.start()
	time_load_s=time.time()
	# --------------------------
	net=module.load_net(filenames)
	# --------------------------
	time_load_e=time.time()
	time_load_t=time_load_e-time_load_s
	trace_load_curr, trace_load_peak=tracemalloc.get_traced_memory()
	tracemalloc.stop()

	# Sleep to clear traces?
	#time.sleep(3)

	# Aggregate the network. Time performance, check memory consumption
	tracemalloc.start()
	time_aggr_s=time.time()
	# --------------------------
	net_aggr=module.aggregate(net)
	# --------------------------
	time_aggr_e=time.time()
	time_aggr_t=time_aggr_e-time_aggr_s
	trace_aggr_curr,trace_aggr_peak=tracemalloc.get_traced_memory()
	tracemalloc.stop()

	# Print stats.
	print("Loading time (in sec.): "+str(time_load_t))
	print("Loading mem curr (in bytes): "+str(trace_load_curr))
	#print("Loading mem peak: "+str(trace_load_peak))
	print("Aggregate time (in sec.): "+str(time_aggr_t))
	print("Aggregate mem curr (in bytes): "+str(trace_aggr_curr))
	#print("Aggregate mem peak: "+str(trace_aggr_peak))

	# Return aggregated network for debug.
	return net_aggr

# experiment 2: Load a network from files and calculate degree distributions
def exp2(filenames):
	# Load the file. Time performance, check memory consumption
	tracemalloc.start()
	time_load_s=time.time()
	# --------------------------
	net=module.load_net(filenames)
	# --------------------------
	time_load_e=time.time()
	time_load_t=time_load_e-time_load_s
	trace_load_curr, trace_load_peak=tracemalloc.get_traced_memory()
	tracemalloc.stop()

	# Sleep to clear traces?
	#time.sleep(3)

	# Calculate degrees. Time performance, check memory consumption
	tracemalloc.start()
	time_degs_s=time.time()
	# --------------------------
	degs=module.get_degree(net)
	# --------------------------
	time_degs_e=time.time()
	time_degs_t=time_degs_e-time_degs_s
	trace_degs_curr,trace_degs_peak=tracemalloc.get_traced_memory()
	tracemalloc.stop()

	# Print stats.
	print("Loading time (in sec.): "+str(time_load_t))
	print("Loading mem curr (in bytes): "+str(trace_load_curr))
	#print("Loading mem peak: "+str(trace_load_peak))
	print("Degree time (in sec.): "+str(time_degs_t))
	print("Degree mem curr (in bytes): "+str(trace_degs_curr))
	#print("Aggregate mem peak: "+str(trace_aggr_peak))
	return degs

# experiment 3: Load a network from file and run InfoMap
def exp3(filenames):
	# Load the file. Time performance, check memory consumption
	tracemalloc.start()
	time_load_s=time.time()
	# --------------------------
	net=module.load_net(filenames)
	# --------------------------
	time_load_e=time.time()
	time_load_t=time_load_e-time_load_s
	trace_load_curr, trace_load_peak=tracemalloc.get_traced_memory()
	tracemalloc.stop()

	# Sleep to clear traces?
	#time.sleep(3)

	# Run InfoMap. Time performance, check memory consumption
	tracemalloc.start()
	time_cdet_s=time.time()
	# --------------------------
	comms=module.run_infomap(net)
	# --------------------------
	time_cdet_e=time.time()
	time_cdet_t=time_cdet_e-time_cdet_s
	trace_cdet_curr,trace_cdet_peak=tracemalloc.get_traced_memory()
	tracemalloc.stop()

	# Print stats.
	print("Loading time (in sec.): "+str(time_load_t))
	print("Loading mem curr (in bytes): "+str(trace_load_curr))
	#print("Loading mem peak: "+str(trace_load_peak))
	print("InfoMap time (in sec.): "+str(time_cdet_t))
	print("InfoMap mem curr (in bytes): "+str(trace_cdet_curr))
	#print("Aggregate mem peak: "+str(trace_aggr_peak))
	return comms

# experiment 4: Build a network from files and visualize with different layouts
def exp4(filenames):
	return


# Chicken chow main. Set up so that the same main util template can be used
#   on all experiments; most of the changes need to be done on the load_net(), 
#   build(), aggregate(), ... methods. 
# 
# Expecting commandline arguments for script to run. 
# Example: python3 experiments.py e_id lib file [size]
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
	lib_input_type=0

	# Halt if no arguments. Otherwise get arg for file identifier
	if len(sys.argv)<4:
		sys.exit("Not enough arguments given. Usage: python3 experiments.py exp_id library file [size]")
	e_id=int(sys.argv[1])
	lib=sys.argv[2]
	file=sys.argv[3]

	### LIBRARY MODULE IMPORTS ###
	#
	# Import library util sources. All source util files contain the functions 
	# 	necessary to run experiments as per the paper.
	# In order to run similar experiments for a new library, one should create 
	#	the file (lib)-util.py with the necessary functions (see all other python
	#	utililty scripts listed here) and import the source code here.
	#
	# Also, here one should note the file input type for the library.
	# Available codes (feel free to define own if necessary):
	# 	1 -- multinet-native, one file for all
	#	2 -- Node/edge/layer files input
	#	3 -- MuxViz input, node/edge/layer-files coded in a semicolon-separated 
	#		config.file
	#	4 -- Custom file for netmem. First line: max_node_id, max_layer_id. Rest is
	#		normal multiplex edgelist file.
 	# Pymnet import
	if lib=="pymnet":
		spec=importlib.util.spec_from_file_location("pymnet_util","pymnet-util.py")
		lib_input_type=2
	# Py3plex import
	elif lib=="py3plex":
		spec=importlib.util.spec_from_file_location("py3plex_util","py3plex-util.py")
		lib_input_type=2
	# multinet import
	elif lib=="multinet":
		spec=importlib.util.spec_from_file_location("multinet_util","multinet-util.py")
		lib_input_type=1
	# Should not reach here
	else:
		return
	module=importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)


	### DATASET IMPORTS ###
	#
	# Note: filenames should be in a format that the load/build... functions
	#		can process. Define new code for lib_input_type if necessary.
	#

	# Load synthetic multilayer network data. Expect second argument N (size)
	# NOTE: if necessary, edit filepaths/input format for library
	if file=="synth":
		n=int(sys.argv[4])
		if n==0:
			sys.exit("No size argument given for synthetic data. Available options: {100,200,500,1000,2000,5000,10000,20000,50000}")

		# 

	# Load London transport data (london-transport).
	elif file=="london":
		if lib_input_type==1:
			filenames=["../data/london-transport/london.mpx"]
			# filenames=["../data/london-transport/london-full.mpx"]
		elif lib_input_type==2:	
			filenames=["../data/london-transport/london_transport_nodes.txt","../data/london-transport/london_transport_multiplex.edges","../data/london-transport/london_transport_layers.txt"]
		elif lib_input_type==3:
			filenames=["../data/london-transport/london.config"]
		elif lib_input_type==4:
			filenames=["../data/london-transport/london_transport_netmem.edges"]

	# Load EUAir transport data (euair-transport)
	elif file=="euair":
		if lib_input_type==1:
			filenames=["../data/euair-transport/euair.mpx"]
			# filenames=["../data/euair-transport/euair-full.mpx"]
		elif lib_input_type==2:	
			filenames=["../data/euair-transport/EUAirTransportation_nodes.txt","../data/euair-transport/EUAirTransportation_multiplex.edges","../data/euair-transport/EUAirTransportation_layers.txt"]
		elif lib_input_type==3:
			filenames=["../data/euair-transport/euair.config"]
		elif lib_input_type==4:
			filenames=["../data/euair-transport/EUAirTransportation_netmem.edges"]

	# Load CS@Aarhus data (cs-aarhus)
	elif file=="aucs":
		if lib_input_type==1:
			filenames=["../data/cs-aarhus/aucs.mpx"]
		elif lib_input_type==2:	
			filenames=["../data/cs-aarhus/CS-Aarhus_nodes.txt","../data/cs-aarhus/CS-Aarhus_multiplex.edges","../data/cs-aarhus/CS-Aarhus_layers.txt"]
		elif lib_input_type==3:
			filenames=["../data/cs-aarhus/aucs.config"]
		elif lib_input_type==4:
			filenames=["../data/cs-aarhus/CS-Aarhus_netmem.edges"]
	
	# Load FriendFeed-Twitter data (ff-tw)
	elif file=="fftw":
		if lib_input_type==1:
			filenames=["../data/ff-tw/fftw.mpx"]
		elif lib_input_type==2:	
			filenames=["../data/ff-tw/fftw_nodes.txt","../data/ff-tw/fftw_multiplex.edges","../data/ff-tw/fftw_layers.txt"]
		elif lib_input_type==3:
			filenames=["../data/ff-tw/fftw.config"]
		elif lib_input_type==4:
			filenames=["../data/ff-tw/fftw_netmem.edges"]
	# Load FriendFeed data (friendfeed)
	elif file=="ff":
		if lib_input_type==1:
			filenames=["../data/friendfeed/ff_simple.mpx"]
		elif lib_input_type==2:	
			filenames=["../data/friendfeed/friendfeed_nodes.txt","../data/friendfeed/friendfeed_multiplex.edges","../data/friendfeed/friendfeed_layers.txt"]
		elif lib_input_type==3:
			filenames=["../data/friendfeed/friendfeed.config"]
		elif lib_input_type==4:
			filenames=["../data/friendfeed/friendfeed_netmem.edges"]

	
	# Should not reach here. Add more cases for datasets here.
	else:
		return
	

	### EXPERIMENTS ###

	#Print exp, lib, file stats and call exp# which prints the rest.
	print("Exp"+str(e_id)+": lib="+lib+", file="+file)
	# Experiment 1: Load net from file & aggregate
	if e_id==1:
		exp1(filenames)
	# Experiment 2: Load net from file & calculate degrees
	elif e_id==2:
		exp2(filenames)
	# Experiment 3: Load net from file & run InfoMap
	elif e_id==3:
		exp3(filenames)
	# Experiment 4: Load net from files & visualize layouts.
	elif e_id==4:
		exp4(filenames)
	#
	# ... Other experiments here ...
	#
	# Should not reach here
	else:
		return
	print("-------------------------------")


# Python stuff
if __name__ == "__main__":
	main()