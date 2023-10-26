# py3plex module for paper benchmark code.
# Library import
import py3plex
from py3plex.core import multinet
from py3plex.algorithms.community_detection import community_wrapper as cw

# Load network from file. Assuming multiplex edgelist input
def load_net(filenames):
	multilayer_network = multinet.multi_layer_network(network_type="multiplex").load_network(
    	filenames[1], # edges
    	directed=True, # assume false for benchmarks.
    	input_type="multiplex_edges"
    )
	return multilayer_network

# Builds a network from files. First, load half the edges in the file, then add and
#	removes edges from the file until the entire network is built
def build_rem(filenames):
	# Placeholder
	return

# Aggregate all edges in an aspect
def aggregate(net):
	net_aggr=net.aggregate_edges(metric="count",normalize_by="raw")
	return net_aggr

# Get the degree distribution for the network
def get_degree(net):
	return net.get_degrees()

# Visualizes a network
def plot_network(net):
	# Placeholder
	return

# Run InfoMap community detection
def run_infomap(net):
	# Path to InfoMap 0.x binary. Change where appropriate
	partition = cw.infomap_communities(net,
		binary="../bin/infomap-0.x/Infomap",
		multiplex=False,
		verbose=True
	)
	# select top n communities by size
	#top_n = 5
	#partition_counts = dict(Counter(partition.values()))
	#top_n_communities = list(partition_counts.keys())[0:top_n]
	
	return partition