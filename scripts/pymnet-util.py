# Pymnet module for paper benchmark code.
# Library import
import pymnet

# Network loader. Functions used depend on library.
# NOTE: change code here to load a file if using a new lib
def load_net(filenames):
	node_file=filenames[0]
	edge_file=filenames[1]
	layer_file=filenames[2]
	net=pymnet.netio.read_edge_files(edge_file,layerinput=layer_file,nodeinput=node_file)
	return net

#
# 
def build(filenames):
	return
#
# 
def build_rem(filenames):
	return

# Network aggregator. Functions used depend on library.
# NOTE: change code here if using a new lib
def aggregate(net):
	# Aggregate net down to one aspect
	net_agg=pymnet.transforms.aggregate(net,1)
	return net_agg

# Degree calculator. Functions used depend on library
# NOTE: change code here if using a new lib
def get_degree(net):
	# Get degree distribution for multilayer network
	degs=pymnet.degs(net)
	return degs

# Plot network. Functions used depend on library
# NOTE: change code here if using a new lib
def plot_network(net):
	# Placeholder
	return

# InfoMap community detection. Functions used depend on library
# NOTE: change code here if using a new lib
def run_infomap(net):
	# Not available in pymnet
	return

