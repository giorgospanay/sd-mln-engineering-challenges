# MultilayerGraphs.jl Julia module for benchmark code

# Imports
using Graphs, SimpleWeightedGraphs, MultilayerGraphs


# Create node:
# Node("name")
# Create MultilayerVertex List:
# [MV(node,("$(node_name)",)) for node in nodes_list]

# Load a network into memory
function load_net(filenames)
	# Native reading not available in MLG.jl.
	# Instead: construct adjacency matrices for each layer and interlayer.
	# Now we are only dealing with multiplex networks, so no need for interlayers.

	# # TODO: test & fix reading
 #    layers = Dict{Int, SimpleWeightedGraph}()
 #    edges = Dict{Int, Vector{Tuple{Int,Int,Float64}}}()

 #    # Open multiplex edgefile. No header.
 #    open(filenames[2],"r") do file
 #        for line in eachline(file)
 #            layer,node1,node2,weight=split(line)
 #            layer,node1,node2,weight=parse(Int,layer),parse(Int,node1),parse(Int,node2),parse(Float64,weight)

 #            if !haskey(layers, layer)
 #                layers[layer] = SimpleWeightedGraph()
 #                edges[layer] = []
 #            end

 #            add_edge!(layers[layer],node1,node2)
 #            push!(edges[layer],(node1,node2,weight))
 #        end
 #    end

 #    MultilayerDiGraph(layers,[])

 #    multilayer_graph = MultilayerGraph(layers, edges)
 #    return multilayer_graph



    layers = Dict{Int, Layer}()

    # Open multiplex edgefile. No header.
    open(filenames[2],"r") do file
        for line in eachline(file)
            layer,node1,node2,weight=split(line)
            layer,node1,node2,weight=parse(Int,layer),parse(Int,node1),parse(Int,node2),parse(Float64,weight)

            if !haskey(layers, layer)
            	# Construct empty layer and fill later
                layers[layer] = layer_simpledigraph(layer,[],[])
            end

            add_edge!(layers[layer],node1,node2,weight=weight)
        end
    end

    multilayer_graph=MultilayerDiGraph(layers,[])
    return multilayer_graph
end


#
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

# Main function for debug
function main()
	net=load_net(["../data/london-transport/london_transport_nodes.txt","../data/london-transport/london_transport_multiplex.edges","../data/london-transport/london_transport_layers.txt"])
	println(net)
end

# Run
main()

