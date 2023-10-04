

# Convert multiplex edgelist file to general multilayer edgelist file (MuxViz),
# 	in order for load() function to work properly with multiplex edgelists.
# Expected format for multiplex edgelist: layerID nodeSrc nodeDest weight
# Converting to format: nodeSrc layerID nodeDest layerID weight
def multiplex_edge_to_multilayer_edge(read_file,write_file):
	wf=open(write_file,"w")
	with open(read_file,"r") as rf:
		for line in rf.readlines():
			tokens=line.split(" ")
			wf.write(""+tokens[1]+" "+tokens[0]+" "+tokens[2]+" "+tokens[0]+" "+tokens[3]+"\n")
	wf.close()




def main():
	multiplex_edge_to_multilayer_edge(
		"../data/cs-aarhus/CS-Aarhus_multiplex.edges",
		"../data/cs-aarhus/CS-Aarhus_multilayer.edges"
	)

# Python stuff
if __name__ == "__main__":
	main()