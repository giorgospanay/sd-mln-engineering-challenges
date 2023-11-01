# py3plex module for paper benchmark code.
# Library import
import py3plex
from py3plex.core import multinet
from py3plex.algorithms.community_detection import community_wrapper as cw
from py3plex.core.multinet import itertools, multi_layer_network
import math
import networkx as nx
import numpy as np

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

# Network generation. Params:
# 	n - Number of vertices
# 	l - Number of layers
# Identify number of edges and probability for MLN-ER model G(n,l,p). 
# In this case: e=sqrt(n), p=e/choose(n,2)
def gen_network(n,l):
	e=math.sqrt(n)
	p=e/math.comb(n,2)
	# # Buggy due to importing random (clashing with python base imports.)
	# # 	See auxiliary function copied from source code.
	# net=random_generators.random_multilayer_ER(n,l,p,directed=False)
	net=random_multiplex_ER2(n,l,p,directed=False)
	return net


# 
# ---------------------------------------------------------------------
# Auxiliary function. Copied as is from py3plex source.
def random_multilayer_ER2(n, l, p, directed=False):
    """ random multilayer ER """

    if directed:
        G = nx.MultiDiGraph()
    else:
        G = nx.MultiGraph()

    network = nx.fast_gnp_random_graph(n, p, directed=directed)
    layers = dict(zip(network.nodes(), np.random.randint(l, size=n)))
    for edge in network.edges():
        G.add_edge((edge[0], layers[edge[0]]), (edge[1], layers[edge[1]]),
                   type="default")

    # construct the ppx object
    no = multi_layer_network(network_type="multilayer").load_network(
        G, input_type="nx", directed=directed)
    return no

def random_multiplex_ER2(n,l,p,directed=False):
    """ random multilayer ER """

    if directed:
        G = nx.MultiDiGraph()
    else:
        G = nx.MultiGraph()

    for lx in range(l):
        network = nx.fast_gnp_random_graph(n, p, seed=None, directed=directed)
        for edge in network.edges():
            G.add_edge((edge[0], lx), (edge[1], lx), type="default")

    # construct the ppx object
    no = multi_layer_network(network_type="multiplex").load_network(
        G, input_type="nx", directed=directed)
    return no
