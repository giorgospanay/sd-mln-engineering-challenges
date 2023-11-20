import parse
import pandas as pd
import numpy as np
import time
from matplotlib import pyplot as plt



def plot_exp1(file_a,file_b):
    # Read files
    df1=pd.read_csv(file_a,sep=" ",header=0)
    df1.replace(0,np.nan,inplace=True)
    df2=pd.read_csv(file_b,sep=" ",header=0)
    df2.replace(0,np.nan,inplace=True)

    # Plot: small datasets, aggregation time
    fig1,ax1=plt.subplots()
    df1a=df1[["dataset","multinet_aggr","muxviz_aggr","pymnet_aggr","py3plex_aggr"]]
    df1a.plot.bar(
        ax=ax1,
        x="dataset",
        logy=True,
        style=['+--','o--','.:','x:'],
        title="Dimension aggregation time, small datasets"
    )
    ax1.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax1.set_ylabel("Dimension aggregation time (sec.)")
    plt.savefig("../logs/plots/exp1a_aggr_real-small_small.png",transparent=True,dpi=300,format="png")
    plt.show()


    # Plot: large datasets, aggregation time
    fig2,ax2=plt.subplots()
    df2a=df2[["dataset","multinet_aggr","muxviz_aggr","pymnet_aggr","py3plex_aggr"]]
    df2a.plot.bar(
        ax=ax2,
        x="dataset",
        logy=True,
        style=['+--','o--','.:','x:'],
        title="Dimension aggregation time, large datasets"
    )
    ax2.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax2.set_ylabel("Dimension aggregation time (sec.)")
    plt.savefig("../logs/plots/exp1b_aggr_real-big_small.png",transparent=True,dpi=300,format="png")
    plt.show()

    return

def plot_exp2(file_a,file_b):
    # Read files
    df1=pd.read_csv(file_a,sep=" ",header=0)
    df1.replace(0,np.nan,inplace=True)
    df2=pd.read_csv(file_b,sep=" ",header=0)
    df2.replace(0,np.nan,inplace=True)

    # Plot: small datasets, load time
    fig1,ax1=plt.subplots()
    df1a=df1[["dataset","multinet_load","muxviz_load","netmem_load","pymnet_load","py3plex_load","mlgjl_load"]]
    df1a.plot.bar(
        ax=ax1,
        x="dataset",
        logy=True,
        style=['+--','o--','2--','.:','x:','d-.'],
        title="Network loading time, small datasets"
    )
    ax1.legend(["multinet","MuxViz","netmem","Pymnet","Py3plex","MLG.jl"])
    ax1.set_ylabel("Network loading time (sec.)")
    plt.savefig("../logs/plots/exp2a_load_real-small_small.png",transparent=True,dpi=300,format="png")
    plt.show()

     # Plot: large datasets, load time
    fig2,ax2=plt.subplots()
    df2a=df2[["dataset","multinet_load","muxviz_load","netmem_load","pymnet_load","py3plex_load","mlgjl_load"]]
    df2a.plot.bar(
        ax=ax2,
        x="dataset",
        logy=True,
        style=['+--','o--','2--','.:','x:','d-.'],
        title="Network loading time, large datasets"
    )
    ax2.legend(["multinet","MuxViz","netmem","Pymnet","Py3plex","MLG.jl"])
    ax2.set_ylabel("Network loading time (sec.)")
    plt.savefig("../logs/plots/exp2a_load_real-large_small.png",transparent=True,dpi=300,format="png")
    plt.show()

    # Plot: small datasets, degree time
    fig3,ax3=plt.subplots()
    df3a=df1[["dataset","multinet_degr","muxviz_degr","netmem_degr","pymnet_degr","py3plex_degr","mlgjl_degr"]]
    df3a.plot.bar(
        ax=ax3,
        x="dataset",
        logy=True,
        style=['+--','o--','2--','.:','x:','d-.'],
        title="Degree calculation time, small datasets"
    )
    ax3.legend(["multinet","MuxViz","netmem","Pymnet","Py3plex","MLG.jl"])
    ax3.set_ylabel("Degree computation time (sec.)")
    plt.savefig("../logs/plots/exp2b_degr_real-small_small.png",transparent=True,dpi=300,format="png")
    plt.show()

    # Plot: large datasets, degree time
    fig4,ax4=plt.subplots()
    df4a=df2[["dataset","multinet_degr","muxviz_degr","netmem_degr","pymnet_degr","py3plex_degr","mlgjl_degr"]]
    df4a.plot.bar(
        ax=ax4,
        x="dataset",
        logy=True,
        style=['+--','o--','2--','.:','x:','d-.'],
        title="Degree calculation time, large datasets"
    )
    ax3.legend(["multinet","MuxViz","netmem","Pymnet","Py3plex","MLG.jl"])
    ax3.set_ylabel("Degree computation time (sec.)")
    plt.savefig("../logs/plots/exp2b_degr_real-large_small.png",transparent=True,dpi=300,format="png")
    plt.show()

    return


def plot_exp4(file_a,file_b):
    # Read files
    df1=pd.read_csv(file_a,sep=" ",header=0)
    df1.replace(0,np.nan,inplace=True)
    df2=pd.read_csv(file_b,sep=" ",header=0)
    df2.replace(0,np.nan,inplace=True)

    # Plot: |L|=2, increasing node size
    fig1,ax1=plt.subplots()
    df1a=df1[["node_size","multinet_aggr","muxviz_aggr","pymnet_aggr","py3plex_aggr"]]
    df1a.plot(
        ax=ax1,
        x="node_size",
        logy=True,
        logx=True,
        xticks=df1["node_size"],
        style=['+--','o--','.:','x:'],
        title="Multiplex network aggregation time, increasing #vertices (|L|=2)"
    )
    ax1.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax1.set_xlabel("Number of vertices")
    ax1.set_ylabel("Layer aggregation time (sec.)")
    plt.savefig("../logs/plots/exp4a_aggr_synth-incr-verts_small.png",transparent=True,dpi=300,format="png")
    plt.show()

    # Plot: |V|=1000, increasing layer size
    fig2,ax2=plt.subplots()
    df2a=df2[["layer_size","multinet_aggr","muxviz_aggr","pymnet_aggr","py3plex_aggr"]]
    df2a.plot(
        ax=ax2,
        x="layer_size",
        logy=True,
        logx=True,
        xticks=df2["layer_size"],
        style=['+--','o--','.:','x:'],
        title="Multiplex network aggregation time, increasing #layers (|V|=1000)"
    )
    ax2.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax2.set_xlabel("Number of layers")
    ax2.set_ylabel("Layer aggregation time (sec.)")
    plt.savefig("../logs/plots/exp4b_aggr_synth-incr-layer_small.png",transparent=True,dpi=300,format="png")
    plt.show()

def plot_exp5(file_a,file_b):
    # Read files
    df1=pd.read_csv(file_a,sep=" ",header=0)
    df1.replace(0,np.nan,inplace=True)
    df2=pd.read_csv(file_b,sep=" ",header=0)
    df2.replace(0,np.nan,inplace=True)

    # Plot: |L|=2, increasing node size
    fig1,ax1=plt.subplots()
    df1a=df1[["node_size","multinet_genr","muxviz_genr","netmem_genr","pymnet_genr","py3plex_genr"]]
    df1a.plot(
        ax=ax1,
        x="node_size",
        logy=True,
        logx=True,
        xticks=df1["node_size"],
        style=['+--','o--','2--','.:','x:'],
        title="Multiplex network generation time, increasing #vertices (|L|=2)"
    )
    ax1.legend(["multinet","MuxViz","netmem","Pymnet","Py3plex"])
    ax1.set_xlabel("Number of vertices")
    ax1.set_ylabel("Network generation time (sec.)")
    plt.savefig("../logs/plots/exp5a_netgen-incr-verts_small.png",transparent=True,dpi=300,format="png")
    plt.show()
    
    # Plot: |V|=1000, increasing layer size
    fig2,ax2=plt.subplots()
    df2a=df2[["layer_size","multinet_genr","muxviz_genr","netmem_genr","pymnet_genr","py3plex_genr"]]
    df2a.plot(
        ax=ax2,
        x="layer_size",
        logy=True,
        logx=True,
        xticks=df2["layer_size"],
        style=['+--','o--','2--','.:','x:'],
        title="Multiplex network generation time, increasing #layers (|V|=1000)"
    )
    ax2.legend(["multinet","MuxViz","netmem","Pymnet","Py3plex"])
    ax2.set_xlabel("Number of layers")
    ax2.set_ylabel("Network generation time (sec.)")
    plt.savefig("../logs/plots/exp5b_netgen-incr-layers_small.png",transparent=True,dpi=300,format="png")
    plt.show()




# Mainest of the mains
def main():

    # Run for experiment 1
    #plot_exp1("../logs/plot_exp1a.txt","../logs/plot_exp1b.txt")
    
    # Run for experiment 2
    plot_exp2("../logs/plot_exp2a.txt","../logs/plot_exp2b.txt")


    # # Run for experiment 4
    # plot_exp4("../logs/plot_exp4a.txt","../logs/plot_exp4b.txt")
    # # Run for experiment 5
    # plot_exp5("../logs/plot_exp5a.txt","../logs/plot_exp5b.txt")

    return

if __name__ == "__main__":
    main()
