# MultilayerGraphs.jl Julia module for benchmark code

# Imports
using Revise, StatsBase, Distributions
using Graphs, SimpleWeightedGraphs, MetaGraphs, SimpleValueGraphs
using MultilayerGraphs


# Create node:
# Node("name")
# Create MultilayerVertex List:
# [MV(node,("$(node_name)",)) for node in nodes_list]

# Load a network into memory
function load_net(filenames)
	# Native reading not available in MLG.jl.
	# Instead: construct adjacency matrices for each layer and interlayer.
	# Now we are only dealing with multiplex networks, so no need for interlayers.

	# TODO: test & fix reading
    layers = Dict{Int, SimpleGraph}()
    edges = Dict{Int, Vector{Tuple{Int, Int, Float64}}}()

    open(filenames[0],"r") do file
        for line in eachline(file)
            layer,node1,node2,weight=split(line)
            layer,node1,node2,weight=parse(Int,layer),parse(Int,node1),parse(Int,node2),parse(Float64,weight)

            if !haskey(layers, layer)
                layers[layer] = SimpleGraph()
                edges[layer] = []
            end

            add_edge!(layers[layer], node1, node2)
            push!(edges[layer], (node1, node2, weight))
        end
    end

    multilayer_graph = MultilayerGraph(layers, edges)
    return multilayer_graph

end




#
function build_rem(filenames)

end


# Aggregate all layers in an aspect
function aggregate(net)
	# Not available in MLG.jl
end


# Get degree distribution of all actors
function get_degree(net)

end

# Visualize the network
function plot_network(net)
	# Not available in MLG.jl
end

# Run InfoMap
function run_infomap(net)
	# Not available in MLG.jl
end

