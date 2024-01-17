# MultilayerGraphs.jl Julia module for benchmark code

# Imports
using Graphs, SimpleWeightedGraphs, MultilayerGraphs

# Load a network into memory
function load_net(filenames::Vector{String})
	# Native reading not available in MLG.jl.
	# Instead: construct adjacency matrices for each layer and interlayer.
	# Now we are only dealing with multiplex networks, so no need for interlayers.

    # Create empty MLG digraph and populate.
    net=MultilayerGraph(Int64,Float64)
    layers=Dict{Int,Layer}()

    # Open multiplex edgefile. No header.
    open(filenames[2],"r") do file
        for line in eachline(file)
            # Parse line. Format: layer n_src n_dst weight
            layer,node1,node2,weight=split(line)
            layer,node1,node2,weight=parse(Int,layer),parse(Int,node1),parse(Int,node2),parse(Float64,weight)

            # Construct native Node and MV items.
            # Note: the package does not (at the time, I presume) offer a good 
            # 	interface to retrieve nodes and edges from the layer, so this
            # 	information should be kept locally. For the time being, however,
            # 	add_vertex!() and add_edge!() fail if duplicate node is added.
            n1,n2=Node("$node1"),Node("$node2")
            mv1,mv2=MV(n1),MV(n2)
            
            # If first time discovering a layer id:
            if !haskey(layers, layer)
            	# Construct empty layer and fill later
                layers[layer] = layer_simpleweightedgraph(Symbol(layer),MultilayerVertex{nothing}[],MultilayerEdge{}[])
            end

            # Add vertices and edge to layer identified
            fv1=add_vertex!(layers[layer],mv1)
            fv2=add_vertex!(layers[layer],mv2)
            fe1=add_edge!(layers[layer],mv1,mv2,weight)

            # # DEBUG: add vertex checks
            # if fv1
            # 	println("Added mv1 #$node1 to layer #$layer")
            # end
            # if fv2
            # 	println("Added mv2 #$node2 to layer #$layer")
            # end
            # if fe1
            # 	println("Added edge $node1 -> $node2 to layer #$layer")
            # end
            
        end
    end

    #
    # --- MultilayerDiGraph crashes for EUAir. Apparently a known problem
    # ---     to be sorted after PR merging in a dependency?
    #
    
    # Add all the layers in MLG net
    for l in collect(values(layers))
    	add_layer!(net,l)
    end

    # --- Doing this instead: ---
    # Add all layers in MLG net, manually define multiplex interlayers


    return net
end


# TODO:
function build_rem(filenames)
	return
end


# Aggregate all layers in an aspect
function aggregate(net)
	# Not available in MLG.jl
	return
end


# Get degrees of all actors
function get_degree(net)
	return degree(net,vertices(net))
end

# Visualize the network
function plot_network(net)
	# Not available in MLG.jl
	return
end

# Run InfoMap
function run_infomap(net)
	# Not available in MLG.jl
	return
end

# Network generation. Params:
#   n - Number of vertices
#   l - Number of layers
## TODO: if there is a fix, find it.
function gen_network(n,l)
    e=trunc(Int,sqrt(n))
    # Construct nodes list 
    nodes_list=[Node("$i") for i in 1:n]
    # Create empty MLG digraph and populate.
    layers=[]
    for lid in 1:l
        layer_j = Layer(
            Symbol(lid),
            nodes_list,
            e,
            SimpleGraph{Int64}(),
            Float64
        )
        push!(layers,layer_j)
    end

    net=MultilayerGraph(layers,[])

    return net
end

# --- EXTRA FUNCTIONS ---
# Add edge (n1,n2,l) to network net
function add_edge(net,n1,n2,l)
    

    # Construct native Node and MV items.
    # Note: the package does not (at the time, I presume) offer a good 
    #   interface to retrieve nodes and edges from the layer, so this
    #   information should be kept locally. For the time being, however,
    #   add_vertex!() and add_edge!() fail if duplicate node is added.
    n1,n2=Node("$node1"),Node("$node2")
    mv1,mv2=MV(n1),MV(n2)
            
    # If first time discovering a layer id:
    if !haskey(layers, layer)
        # Construct empty layer and fill later
        layers[layer] = layer_simpleweightedgraph(Symbol(layer),MultilayerVertex{nothing}[],MultilayerEdge{}[])
    end

    # Add vertices and edge to layer identified
    fv1=add_vertex!(layers[layer],mv1)
    fv2=add_vertex!(layers[layer],mv2)
    fe1=add_edge!(layers[layer],mv1,mv2,weight) 

    return net   
end

# Remove edge (n1,n2,l) from network net
function rem_edge(net,n1,n2,l)

end

# Main function for debug
function main()
	#net=load_net(["../data/london-transport/london_transport_nodes.txt","../data/london-transport/london_transport_multiplex.edges","../data/london-transport/london_transport_layers.txt"])
	net=gen_network(10,2)
    println(net)
end

# # Run
# main()

