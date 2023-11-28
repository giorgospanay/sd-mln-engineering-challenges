# Pymnet module for paper benchmark code.
# Library import
import pymnet
import math

# Network loader. Functions used depend on library.
# NOTE: change code here to load a file if using a new lib
def load_net(filenames):
	node_file=filenames[0]
	edge_file=filenames[1]
	layer_file=filenames[2]
	#net=pymnet.netio.read_edge_files(edge_file,layerinput=layer_file,nodeinput=node_file)
	net=pymnet.netio.read_edge_files(edge_file,layerinput=layer_file,nodeinput=node_file,couplings="none")
	return net

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
	#pymnet.webplot(net,outputfile="web_london.html")
	fig=pymnet.draw(net,
		show=True,
        layout="spring",
        layerColorRule={},
        defaultLayerColor="gray",
        nodeLabelRule={},
        defaultEdgeColor="brown",
    )
	return

# InfoMap community detection.
# NOTE: change code here if using a new lib
def run_infomap(net):
	# Not available in pymnet
	return

# Network generation. Params:
# 	n - Number of vertices
# 	l - Number of layers
# Identify number of edges and probability for MLN-ER model G(n,l,p). 
# In this case: e=sqrt(n), p=e/choose(n,2)
def gen_network(n,l):
	e=math.sqrt(n)
	p=e/math.comb(n,2)
	net=pymnet.er_multilayer(n,l,p)
	return net

# # Main plotting for poster visuals
# def main():
# 	#net=load_net(["../data/florentine/Padgett-Florentine-Families_nodes.txt","../data/florentine/Padgett-Florentine-Families_multiplex.edges","../data/florentine/Padgett-Florentine-Families_layers.txt"])
# 	net=load_net(["../data/london-transport/london_transport_nodes.txt","../data/london-transport/london_transport_multiplex.edges","../data/london-transport/london_transport_layers.txt"])
# 	#net=load_net(["../data/cs-aarhus/CS-Aarhus_nodes.txt","../data/cs-aarhus/CS-Aarhus_multiplex.edges","../data/cs-aarhus/CS-Aarhus_layers.txt"])
# 	plot_network(net)

# if __name__ == '__main__':
# 	main()


