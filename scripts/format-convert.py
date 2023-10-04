

# Convert multiplex edgelist file to general multilayer edgelist file (MuxViz),
# 	in order for load() function to work properly with multiplex edgelists.
# Expected format for multiplex edgelist: layerID nodeSrc nodeDest weight
# Converting to format: nodeSrc layerID nodeDst layerID weight
def multiplex_edge_to_multilayer_edge(read_file,write_file):
	wf=open(write_file,"w")
	with open(read_file,"r") as rf:
		for line in rf.readlines():
			tokens=line.split(" ")
			wf.write(""+tokens[1]+" "+tokens[0]+" "+tokens[2]+" "+tokens[0]+" "+tokens[3])
	wf.close()


# Convert multiplex edgelist, layers, nodes file to multinet native file.
def multiplex_edge_to_multinet_native(read_node,read_edge,read_layer,write_file):
	return



def main():
	multiplex_edge_to_multilayer_edge(
		"../data/london-transport/london_transport_multiplex.edges",
		"../data/london-transport/london_transport_multilayer.edges"
	)

	multiplex_edge_to_multilayer_edge(
		"../data/euair-transport/EUAirTransportation_multiplex.edges",
		"../data/euair-transport/EUAirTransportation_multilayer.edges"
	)

	multiplex_edge_to_multilayer_edge(
		"../data/cs-aarhus/CS-Aarhus_multiplex.edges",
		"../data/cs-aarhus/CS-Aarhus_multilayer.edges"
	)

# Python stuff
if __name__ == "__main__":
	main()