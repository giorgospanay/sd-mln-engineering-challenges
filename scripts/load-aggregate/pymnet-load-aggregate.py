# Loads a network and aggregates it in __

# Imports
import sys
import time
import tracemalloc

# Library import
import pymnet
# NOTE: change library name for printing logfile
lib_name="Pymnet"
# NOTE: change data path accordingly
data_path="../../data/"


# Network loader. Functions used depend on library.
# NOTE: change code here to load a file if using a new lib
def load(filenames):
	node_file=""+data_path+filenames[0]
	edge_file=""+data_path+filenames[1]
	layer_file=""+data_path+filenames[2]
	net=pymnet.netio.read_edge_files(edge_file,layerinput=layer_file,nodeinput=node_file)
	return net


# Network aggregator. Functions used depend on library.
# NOTE: change code here to load a file if using a new lib
def aggregate(net):
	# Aggregate net down to one aspect
	net_agg=pymnet.transforms.aggregate(net,1)
	return net_agg

# Function call for experiment
def experiment(filenames):
	# Load the file. Time performance, check memory consumption
	tracemalloc.start()
	time_load_s=time.time()
	net=load(filenames)
	time_load_e=time.time()
	time_load_t=time_load_e-time_load_s
	trace_load=tracemalloc.get_traced_memory()
	tracemalloc.stop()

	# Sleep? (To clearly check memory consumption over time). Maybe not needed.

	# Aggregate the network. Time performance, check memory consumption
	tracemalloc.start()
	time_aggr_s=time.time()
	net_aggr=aggregate(net)
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



# Chicken chow main. Filepaths used depend on library.
def main():
	global lib_name,data_path
	
	filenames=[]


	if len(sys.argv)<2:
		sys.exit("No file argument given. Available options: {synth N, london, euair, aucs, fftw, citation, ff}")
	file=sys.argv[1]

	# Load synthetic multilayer network data. Expect second argument N (size)
	if file=="synth":
		n=int(sys.argv[2])
		if n==0:
			sys.exit("No size argument given for synthetic data. Available options: {100,200,500,1000,2000,5000,10000,20000,50000}")

		# 

	# Load London transport data (london-transport)
	elif file=="london":
		return
	# Load EUAir transport data (euair-transport)
	elif file=="euair":
		return
	# Load CS@Aarhus data (cs-aarhus)
	elif file=="aucs":
		filenames=["cs-aarhus/CS-Aarhus_nodes.txt","cs-aarhus/CS-Aarhus_multiplex.edges","cs-aarhus/CS-Aarhus_layers.txt"]
	# Load FriendFeed-Twitter data (ff-tw)
	elif file=="fftw":
		return
	# Load citation data (journal-citation)
	elif file=="citation":
		return
	# Load FriendFeed data (friendfeed)
	elif file=="ff":
		return
	# Should not reach here.
	else:
		return

	# In either case, print file stats and call experiment which prints the rest.
	print(""+str(lib_name)+", file="+file)
	experiment(filenames)
	print("-------------------------------")


# Python stuff
if __name__ == "__main__":
	main()