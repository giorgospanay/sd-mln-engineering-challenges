

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


# Convert multiplex edgelist, layers, nodes file to multinet native file, in.
# 	#TYPE multilayer mode
def multiplex_edge_to_multinet_full(read_actor,read_edge,read_layer,write_file):
	wf=open(write_file,"w")
	rf_actor=open(read_actor,"r")
	rf_edge=open(read_edge,"r")
	rf_layer=open(read_layer,"r")

	# Add multilayer header
	ml_header="#TYPE\nmultilayer\n"

	# Open layers file. Assume directed and no loops for benchmark.
	all_layers="#LAYERS\n"
	layer_lines=rf_layer.readlines()
	layer_count=0
	# Ignore header. No layer attributes. Assuming layer ids start from 1.
	for l in layer_lines[1:]:
		if l.strip()!="":
			layer_count=layer_count+1
	for i in range(1,layer_count+1):
		all_layers=all_layers+str(i)+",DIRECTED\n"

	# Open node attributes file. Assign header columns as attributes, all strings
	actor_attr="#ACTOR ATTRIBUTES\nnodeLabel,STRING\n"
	actor_lines=rf_actor.readlines()
	tokens=actor_lines[0].strip().split(" ")
	# Tokens assumed to be: nodeID nodeLabel [attbs]
	if len(tokens)>2:
		# Assuming all attributes are string.
		for t in tokens[2:]:
			t1=t.strip()
			actor_attr=actor_attr+t1+",STRING\n"
	# Add all actors & vertices
	all_actors="#ACTORS\n"
	all_vertices="#VERTICES\n"
	for a_line in actor_lines[1:]:
		a_tokens=a_line.strip().split(" ")
		# On multiplex edgelist, assume all actors are in all layers.
		all_actors=all_actors+(",".join(a_tokens))+"\n"
		for i in range(1,layer_count+1):
			all_vertices=all_vertices+a_tokens[0]+","+str(i)+"\n"

	# Add edge attribute: weight
	edge_attr="#EDGE ATTRIBUTES\nweight,NUMERIC\n"

	# Read all edges & weights
	all_edges="#EDGES\n"
	edge_lines=rf_edge.readlines()
	# No header- start writing immediately
	for e in edge_lines:
		# Convert multiplex edge (layer nodeSrc nodeDst weight) to 
		#	(nodeSrc layer nodeDst layer weight)
		e_tokens=e.strip().split(" ")
		e_line=",".join([e_tokens[1],e_tokens[0],e_tokens[2],e_tokens[0],e_tokens[3]])
		all_edges=all_edges+e_line+"\n"

	# Now write all into file
	wf.write(ml_header)
	wf.write(actor_attr)
	wf.write(edge_attr)
	wf.write(all_layers)
	wf.write(all_actors)
	wf.write(all_vertices)
	wf.write(all_edges)

	# ...and close the files.
	wf.close()
	rf_actor.close()
	rf_edge.close()
	rf_layer.close()
	return



def main():

	# multiplex_edge_to_multinet_full(
	# 	"../data/london-transport/london_transport_nodes.txt",
	# 	"../data/london-transport/london_transport_multiplex.edges",
	# 	"../data/london-transport/london_transport_layers.txt",
	# 	"../data/london-transport/london-full.mpx"
	# )

	multiplex_edge_to_multinet_full(
		"../data/euair-transport/EUAirTransportation_nodes.txt",
		"../data/euair-transport/EUAirTransportation_multiplex.edges",
		"../data/euair-transport/EUAirTransportation_layers.txt",
		"../data/euair-transport/euair-full.mpx"
	)

	# multiplex_edge_to_multilayer_edge(
	# 	"../data/london-transport/london_transport_multiplex.edges",
	# 	"../data/london-transport/london_transport_multilayer.edges"
	# )
	# multiplex_edge_to_multilayer_edge(
	# 	"../data/euair-transport/EUAirTransportation_multiplex.edges",
	# 	"../data/euair-transport/EUAirTransportation_multilayer.edges"
	# )
	# multiplex_edge_to_multilayer_edge(
	# 	"../data/cs-aarhus/CS-Aarhus_multiplex.edges",
	# 	"../data/cs-aarhus/CS-Aarhus_multilayer.edges"
	# )



# Python stuff
if __name__ == "__main__":
	main()