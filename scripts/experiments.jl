using Dates

function load_net(filenames)
    # Implement your load_net function logic here
end

function aggregate(net)
    # Implement your aggregate function logic here
end

function exp1(filenames)
    time_load_s = now()
    net = load_net(filenames)
    time_load_e = now()
    time_load_t = time_load_e - time_load_s

    time_aggr_s = now()
    net_aggr = aggregate(net)
    time_aggr_e = now()
    time_aggr_t = time_aggr_e - time_aggr_s

    println("Loading time: ", time_load_t)
    println("Aggregate time: ", time_aggr_t)
end

function main()
    if length(ARGS) < 3
        println("Not enough arguments given. Usage: julia experiments.jl exp_id library file [size]")
        return
    end

    e_id = parse(Int, ARGS[1])
    lib = ARGS[2]
    file = ARGS[3]

    # Import necessary functions from the library utility file
    include("$lib-util.jl")

    filenames = []

    if file == "synth"
        # Implement file loading logic for synth dataset
    elseif file == "london"
        # Implement file loading logic for london dataset
    elseif file == "euair"
        # Implement file loading logic for euair dataset
    elseif file == "aucs"
        # Implement file loading logic for aucs dataset
    elseif file == "fftw"
        # Implement file loading logic for fftw dataset
    elseif file == "citation"
        # Implement file loading logic for citation dataset
    elseif file == "ff"
        # Implement file loading logic for ff dataset
    else
        println("Dataset not found. See available arguments.")
        return
    end

    println("Exp$e_id: lib=$lib, file=$file")
    
    if e_id == 1
        exp1(filenames)
    elseif e_id == 2
        # Implement logic for experiment 2
    else
        println("Experiment id not found. See comments/paper for available args.")
    end

    println("-------------------------------")
end

# Run main.
main()
