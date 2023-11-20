import pymnet
import math

# Path to synth datasets
data_path="../data/synth/"

# Generates a random network in pymnet (code similar to pymnet-util). Extra 
# 	parameter eg: growth rate for edges. Takes numeric values for a linear growth rate
# 	(example: if g=4 then each node has an average degree of 4), or "s" for the number
#	of edges to be equal to sqrt(n*l).
def gen_save_network(n,g,l,file):
	e=0
	# For sqrt(n*l):
	if g=="s":
		e=n*math.sqrt(n)
	elif g==0:
		return # Should not reach here
	# For linear growth:
	else:
		e=n*g
	p=e/math.comb(n,2)
	
	# Generate list of probabilities (same for each layer)
	probs=[p]*l

	# Generate multiplex ER network
	net=pymnet.er(n,p=probs)

	# Save to edge files
	write_edge_files_light(net,file,numericNodes=True,columnSeparator=" ")

# Light version of write_edge_files, edited from pymnet source code. 
# 	Change to a single file for all layers.
def write_edge_files_light(net,outputfiles,columnSeparator="\t",rowSeparator="\n",weights=True,numericNodes=False):
	if numericNodes:
		nodetonumber={}
		for i,node in enumerate(net):
			nodetonumber[node]=i
	ofile=open(outputfiles+".edges",'w')
	for l,layer in enumerate(net.get_layers()):
		for edge in net.A[layer].edges:
			n1,n2=edge[0],edge[1]
			if numericNodes:
				n1,n2=nodetonumber[n1],nodetonumber[n2]
			if weights:
				ofile.write(str(l+1)+columnSeparator+str(n1)+columnSeparator+str(n2)+columnSeparator+str(edge[2])+rowSeparator)
			else:
				ofile.write(str(l+1)+columnSeparator+str(n1)+columnSeparator+str(n2)+rowSeparator)
	ofile.close()

# Generates synthetic data used for experiments. Uses methods from pymnet.
# 	Where necessary, conversion between different formats done with methods
#	from the format-convert.py script.
def main():
	global data_path

	# for n in [1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000]:
	# 	for g in ["s"]:
	# 		name=data_path+str(n)+"-"+str(g)+"-2"
	# 		gen_save_network(n,g,2,name)

	# for n in [10000000,20000000,50000000,100000000]:
	# 	for g in [4]:
	# 		name=data_path+str(n)+"-"+str(g)+"-2"
	# 		gen_save_network(n,g,2,name)

	for l in [5,10,20,50,100,200,500,1000,2000,5000,10000]:
		for g in [4,"s"]:
			name=data_path+"1000-"+str(g)+"-"+str(l)
			gen_save_network(1000,g,l,name)


	# # Generate network for increasing number of nodes. l=2,g="s"
	# for n in [1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000,5000000,10000000]:
	# 	name=data_path+str(n)+"-s-2"
	# 	gen_save_network(n,"s",2,name)
	# # Generate network for different edge rates. n=1000,l=2
	# for g in [4,40,400]:
	# 	name=data_path+"1000-"+str(g)+"-2"
	# 	gen_save_network(1000,g,2,name)
	# # Generate network for increasing number of layers. n=1000,g="s"
	# for l in [5,10,20,50,100,200,500,1000]:
	# 	name=data_path+"1000-s-"+str(l)
	# 	gen_save_network(1000,"s",l,name)

	 
if __name__=="__main__":
	main()

