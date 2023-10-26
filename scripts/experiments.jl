using Dates

# Add include() for library utility files here. Dynamic inclusion does not work 
#   right now (global age errors).
# MLG.jl include
include("mlgjl-util.jl")

# Load network from file and aggregate
function exp1(filenames)
    time_load_s = Dates.value(now())
    net = load_net(filenames)
    time_load_e = Dates.value(now())
    time_load_t = time_load_e - time_load_s

    time_aggr_s = Dates.value(now())
    net_aggr = aggregate(net)
    time_aggr_e = Dates.value(now())
    time_aggr_t = time_aggr_e - time_aggr_s

    println("Loading time (in sec.): ", values(time_load_t)/1000.0)
    println("Aggregate time (in sec.): ", values(time_aggr_t)/1000.0)
    return net_aggr
end

# Load network from file and get degrees
function exp2(filenames)
    time_load_s = Dates.value(now())
    net = load_net(filenames)
    time_load_e = Dates.value(now())
    time_load_t = time_load_e - time_load_s

    time_degs_s = Dates.value(now())
    degs = get_degree(net)
    time_degs_e = Dates.value(now())
    time_degs_t = time_degs_e - time_degs_s

    println("Loading time (in sec.): ", values(time_load_t)/1000.0)
    println("Degree time (in sec.): ", values(time_degs_t)/1000.0)
    return degs
end

# Load network from file and run InfoMap
function exp3(filenames)
    time_load_s = Dates.value(now())
    net = load_net(filenames)
    time_load_e = Dates.value(now())
    time_load_t = time_load_e - time_load_s

    time_cdet_s = Dates.value(now())
    comms = run_infomap(net)
    time_cdet_e = Dates.value(now())
    time_cdet_t = time_cdet_e - time_cdet_s

    println("Loading time (in sec.): ", values(time_load_t)/1000.0)
    println("InfoMap time (in sec.): ", values(time_cdet_t)/1000.0)
    return comms
end

# Generate network and aggregate
function exp4(n,l)
    time_gens_s = Dates.value(now())
    net = gen_network(n,l)
    time_gens_e = Dates.value(now())
    time_gens_t = time_gens_e - time_gens_s

    time_aggr_s = Dates.value(now())
    net_aggr = aggregate(net)
    time_aggr_e = Dates.value(now())
    time_aggr_t = time_aggr_e - time_aggr_s

    println("Generate time (in sec.): ", values(time_gens_t)/1000.0)
    println("Aggregate time (in sec.): ", values(time_aggr_t)/1000.0)
    return net_aggr
end

# Generate network and get degrees
function exp5(n,l)
    ime_gens_s = Dates.value(now())
    net = gen_network(n,l)
    time_gens_e = Dates.value(now())
    time_gens_t = time_gens_e - time_gens_s

    time_degs_s = Dates.value(now())
    degs = get_degree(net)
    time_degs_e = Dates.value(now())
    time_degs_t = time_degs_e - time_degs_s

    println("Generate time (in sec.): ", values(time_gens_t)/1000.0)
    println("Degree time (in sec.): ", values(time_degs_t)/1000.0)
    return degs
end

# Load network from file and visualize
function exp99(filenames)
    # Not available for current libraries. Populate here if necessary.
end

# Main call
function main()
    if length(ARGS) < 3
        println("Not enough arguments given. Usage: julia experiments.jl exp_id library file [size]")
        return
    end

    e_id = parse(Int, ARGS[1])
    lib = ARGS[2]
    file = ARGS[3]

    ### LIBRARY MODULE IMPORTS ###
    #
    # Here one should note the file input type for the library.
    # Available codes (feel free to define own if necessary):
    #   1 -- multinet-native, one file for all
    #   2 -- Node/edge/layer files input
    #   3 -- MuxViz input, node/edge/layer-files coded in a semicolon-separated 
    #       config.file
    #   4 -- Custom file for netmem. First line: max_node_id, max_layer_id. Rest is
    #       normal multiplex edgelist file.
    #
    # Notice that code evaluation is not done dynamically- see file header for 
    #   library utility file includes.
    # TODO: Probably needs to be fixed, if more Julia libraries implementing the
    #   same functions are available in the future.
    #
    lib_input_type=0
    if lib=="mlgjl"
        lib_input_type=2
    # 
    # Add other libraries here if necessary...
    #
    else # Should not reach here
        println("Library not found, see arguments.")
        return
    end


    ### DATASET IMPORTS ###
    #
    # Note: filenames should be in a format that the load/build... functions
    #       can process. Define new code for lib_input_type if necessary.
    #
    filenames = []

    # Load synthetic multilayer network data. Expect second argument N (size)
    # NOTE: if necessary, edit filepaths/input format for library
    if file=="synth"
        n=parse(Int,ARGS[4])
        if n==0
            println("No size argument given for synthetic data. Available options: {100,200,500,1000,2000,5000,10000,20000,50000}")
            return
        end 

    # Load London transport data (london-transport).
    elseif file=="london"
        if lib_input_type==1
            filenames=["../data/london-transport/london.mpx"]
            # filenames=["../data/london-transport/london-full.mpx"]
        elseif lib_input_type==2
            filenames=["../data/london-transport/london_transport_nodes.txt","../data/london-transport/london_transport_multiplex.edges","../data/london-transport/london_transport_layers.txt"]
        elseif lib_input_type==3
            filenames=["../data/london-transport/london.config"]
        elseif lib_input_type==4
            filenames=["../data/london-transport/london_transport_netmem.edges"]
        end
    # Load EUAir transport data (euair-transport)
    elseif file=="euair"
        if lib_input_type==1
            filenames=["../data/euair-transport/euair.mpx"]
            # filenames=["../data/euair-transport/euair-full.mpx"]
        elseif lib_input_type==2 
            filenames=["../data/euair-transport/EUAirTransportation_nodes.txt","../data/euair-transport/EUAirTransportation_multiplex.edges","../data/euair-transport/EUAirTransportation_layers.txt"]
        elseif lib_input_type==3
            filenames=["../data/euair-transport/euair.config"]
        elseif lib_input_type==4
            filenames=["../data/euair-transport/EUAirTransportation_netmem.edges"]
        end
    # Load CS@Aarhus data (cs-aarhus)
    elseif file=="aucs"
        if lib_input_type==1
            filenames=["../data/cs-aarhus/aucs.mpx"]
        elseif lib_input_type==2
            filenames=["../data/cs-aarhus/CS-Aarhus_nodes.txt","../data/cs-aarhus/CS-Aarhus_multiplex.edges","../data/cs-aarhus/CS-Aarhus_layers.txt"]
        elseif lib_input_type==3
            filenames=["../data/cs-aarhus/aucs.config"]
        elseif lib_input_type==4
            filenames=["../data/cs-aarhus/CS-Aarhus_netmem.edges"]
        end
    # Load FriendFeed-Twitter data (ff-tw)
    elseif file=="fftw"
        if lib_input_type==1
            filenames=["../data/ff-tw/fftw.mpx"]
        elseif lib_input_type==2
            filenames=["../data/ff-tw/fftw_nodes.txt","../data/ff-tw/fftw_multiplex.edges","../data/ff-tw/fftw_layers.txt"]
        elseif lib_input_type==3
            filenames=["../data/ff-tw/fftw.config"]
        elseif lib_input_type==4
            filenames=["../data/ff-tw/fftw_netmem.edges"]
        end
    # Load FriendFeed data (friendfeed)
    elseif file=="ff"
        if lib_input_type==1
            filenames=["../data/friendfeed/ff_simple.mpx"]
        elseif lib_input_type==2
            filenames=["../data/friendfeed/friendfeed_nodes.txt","../data/friendfeed/friendfeed_multiplex.edges","../data/friendfeed/friendfeed_layers.txt"]
        elseif lib_input_type==3
            filenames=["../data/friendfeed/friendfeed.config"]
        elseif lib_input_type==4
            filenames=["../data/friendfeed/friendfeed_netmem.edges"]
        end
    
    # Should not reach here. Add more cases for datasets here.
    else
        println("Dataset not found. See available arguments.")
        return
    end

    #### TODO: add code to run generation experiments

    ### RUN EXPERIMENTS
    #
    # Note: running Base.invokelatest() to avoid global age errors with module inclusions
    #   Expensive, but open to hearing other solutions. Plus it does not affect the experiments.
    # 
    println("Exp$e_id: lib=$lib, file=$file")
    if e_id == 1
        exp1(filenames)
    elseif e_id == 2
        exp2(filenames)
    elseif e_id==3
        exp3(filenames)
    elseif e_id==4
        exp4(filenames)
    #
    # ...Add other experiments here...
    #
    else
        println("Experiment id not found. See comments/paper for available args.")
    end

    println("-------------------------------")
end

# Run main
main()
