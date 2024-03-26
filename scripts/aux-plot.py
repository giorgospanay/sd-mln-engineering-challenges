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
        style=['+--','o--','.:','x:']
        #title="Dimension aggregation time, small datasets"
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
        style=['+--','o--','.:','x:']
        #title="Dimension aggregation time, large datasets"
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
    df1a=df1[["dataset","multinet_load","muxviz_load","pymnet_load","py3plex_load"]]
    df1a.plot.bar(
        ax=ax1,
        x="dataset",
        logy=True,
        style=['+--','o--','.:','x:']
        #title="Network loading time, small datasets"
    )
    ax1.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax1.set_ylabel("Network loading time (sec.)")
    plt.savefig("../logs/plots/exp2a_load_real-small_small.png",transparent=True,dpi=300,format="png")
    plt.show()

     # Plot: large datasets, load time
    fig2,ax2=plt.subplots()
    df2a=df2[["dataset","multinet_load","muxviz_load","pymnet_load","py3plex_load"]]
    df2a.plot.bar(
        ax=ax2,
        x="dataset",
        logy=True,
        style=['+--','o--','.:','x:']
        #title="Network loading time, large datasets"
    )
    ax2.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax2.set_ylabel("Network loading time (sec.)")
    plt.savefig("../logs/plots/exp2a_load_real-large_small.png",transparent=True,dpi=300,format="png")
    plt.show()

    # Plot: small datasets, degree time
    fig3,ax3=plt.subplots()
    df3a=df1[["dataset","multinet_degr","muxviz_degr","pymnet_degr","py3plex_degr","mlgjl_degr"]]
    df3a.plot.bar(
        ax=ax3,
        x="dataset",
        logy=True,
        style=['+--','o--','2--','.:','x:','d-.']
        #title="Degree calculation time, small datasets"
    )
    ax3.legend(["multinet","MuxViz","Pymnet","Py3plex","MLG.jl"])
    ax3.set_ylabel("Degree computation time (sec.)")
    plt.savefig("../logs/plots/exp2b_degr_real-small_small.png",transparent=True,dpi=300,format="png")
    plt.show()

    # Plot: large datasets, degree time
    fig4,ax4=plt.subplots()
    df4a=df2[["dataset","multinet_degr","muxviz_degr","pymnet_degr","py3plex_degr","mlgjl_degr"]]
    df4a.plot.bar(
        ax=ax4,
        x="dataset",
        logy=True,
        style=['+--','o--','.:','x:','d-.']
        #title="Degree calculation time, large datasets"
    )
    ax4.legend(["multinet","MuxViz","Pymnet","Py3plex","MLG.jl"])
    ax4.set_ylabel("Degree computation time (sec.)")
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
        style=['+--','o--','.:','x:']
        #title="Multiplex network aggregation time, increasing #vertices (|L|=2)"
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
        style=['+--','o--','.:','x:']
        #title="Multiplex network aggregation time, increasing #layers (|V|=1000)"
    )
    ax2.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax2.set_xlabel("Number of layers")
    ax2.set_ylabel("Layer aggregation time (sec.)")
    plt.savefig("../logs/plots/exp4b_aggr_synth-incr-layer_small.png",transparent=True,dpi=300,format="png")
    plt.show()

# Plotting only network generation time.
def plot_exp5(file_a,file_b):
    # Read files
    df1=pd.read_csv(file_a,sep=" ",header=0)
    df1.replace(0,np.nan,inplace=True)
    df2=pd.read_csv(file_b,sep=" ",header=0)
    df2.replace(0,np.nan,inplace=True)

    # Plot: |L|=2, increasing node size
    fig1,ax1=plt.subplots()
    df1a=df1[["node_size","multinet_genr","muxviz_genr","pymnet_genr","py3plex_genr"]]
    df1a.plot(
        ax=ax1,
        x="node_size",
        logy=True,
        logx=True,
        xticks=df1["node_size"],
        style=['+--','o--','.:','x:']
        #title="Multiplex network generation time, increasing #vertices (|L|=2)"
    )
    ax1.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax1.set_xlabel("Number of vertices")
    ax1.set_ylabel("Network generation time (sec.)")
    plt.savefig("../logs/plots/exp5a_netgen-incr-verts_small.png",transparent=True,dpi=300,format="png")
    plt.show()
    
    # Plot: |V|=1000, increasing layer size
    fig2,ax2=plt.subplots()
    df2a=df2[["layer_size","multinet_genr","muxviz_genr","pymnet_genr","py3plex_genr"]]
    df2a.plot(
        ax=ax2,
        x="layer_size",
        logy=True,
        logx=True,
        xticks=df2["layer_size"],
        style=['+--','o--','.:','x:']
        #title="Multiplex network generation time, increasing #layers (|V|=1000)"
    )
    ax2.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax2.set_xlabel("Number of layers")
    ax2.set_ylabel("Network generation time (sec.)")
    plt.savefig("../logs/plots/exp5b_netgen-incr-layers_small.png",transparent=True,dpi=300,format="png")
    plt.show()

# Plotting only layer aggregation time for all synth. Loading time plotted on exp7 (all libs)
def plot_exp6(file_a,file_b,file_c,file_d):
    df1=pd.read_csv(file_a,sep=" ",header=0)
    df1.replace(0,np.nan,inplace=True)
    df2=pd.read_csv(file_b,sep=" ",header=0)
    df2.replace(0,np.nan,inplace=True)
    df3=pd.read_csv(file_c,sep=" ",header=0)
    df3.replace(0,np.nan,inplace=True)
    df4=pd.read_csv(file_d,sep=" ",header=0)
    df4.replace(0,np.nan,inplace=True)

    # Plot: synth data aggr time, n++ / e=4 / l=2
    fig5,((ax5,ax7),(ax6,ax8))=plt.subplots(2,2)
    df1b=df1[["node_size","multinet_aggr","muxviz_aggr","pymnet_aggr","py3plex_aggr"]]
    df1b.plot(
        ax=ax5,
        x="node_size",
        logy=True,
        logx=True,
        xticks=df1["node_size"],
        style=['+--','o--','.:','x:']
        #title="Degree calculation time, small datasets"
    )
    ax5.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax5.legend().set_visible(False)
    ax5.set_ylabel("")
    ax5.set_xlabel("")
    #plt.savefig("../logs/plots/exp6a_aggr_synth_nplus_e4_l2.png",transparent=True,dpi=300,format="png")
    #plt.show()

    # Plot: synth data degree time, n++ / e=s / l=2
    #fig6,ax6=plt.subplots()
    df2b=df2[["node_size","multinet_aggr","muxviz_aggr","pymnet_aggr","py3plex_aggr"]]
    df2b.plot(
        ax=ax6,
        x="node_size",
        logy=True,
        logx=True,
        xticks=df2["node_size"],
        style=['+--','o--','.:','x:']
        #title="Degree calculation time, small datasets"
    )
    ax6.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax6.legend().set_visible(False)
    ax6.set_ylabel("")
    ax6.set_xlabel("Number of vertices")
    #plt.savefig("../logs/plots/exp6b_aggr_synth_nplus_es_l2.png",transparent=True,dpi=300,format="png")
    #plt.show()

    # Plot: synth data degree time, n=1000 / e=4 / l++
    #fig7,ax7=plt.subplots()
    df3b=df3[["layer_size","multinet_aggr","muxviz_aggr","pymnet_aggr","py3plex_aggr"]]
    df3b.plot(
        ax=ax7,
        x="layer_size",
        logy=True,
        logx=True,
        xticks=df3["layer_size"],
        style=['+--','o--','.:','x:']
        #title="Degree calculation time, small datasets"
    )
    ax7.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax7.legend().set_visible(False)
    ax7.set_ylabel("")
    ax7.set_xlabel("")
    #plt.savefig("../logs/plots/exp6c_aggr_synth_n1000_e4_lplus.png",transparent=True,dpi=300,format="png")
    #plt.show()


    # Plot: synth data degree time, n=1000 / e=s / l++
    #fig8,ax8=plt.subplots()
    df4b=df4[["layer_size","multinet_aggr","muxviz_aggr","pymnet_aggr","py3plex_aggr"]]
    df4b.plot(
        ax=ax8,
        x="layer_size",
        logy=True,
        logx=True,
        xticks=df4["layer_size"],
        style=['+--','o--','.:','x:']
        #title="Degree calculation time, large datasets"
    )
    ax8.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax8.legend().set_visible(False)
    ax8.set_ylabel("")
    ax8.set_xlabel("Number of layers")
    #plt.savefig("../logs/plots/exp6d_aggr_synth_n1000_es_lplus.png",transparent=True,dpi=300,format="png")
    #plt.show()  


    fig5.supylabel("Layer aggregation time (sec.)")

    libs=["multinet","MuxViz","Pymnet","Py3plex"]
    lines_labels = [ax.get_legend_handles_labels() for ax in fig5.axes]
    lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
    fig5.legend(lines,libs,ncol=len(libs),loc="upper center")

    fig5.savefig("../logs/plots/exp6.png",transparent=True,dpi=300,format="png")
    fig5.show()  

    return


# Plotting both loading time for all synth AND degree calculation time
def plot_exp7(file_a,file_b,file_c,file_d):
    # Read files
    df1=pd.read_csv(file_a,sep=" ",header=0)
    df1.replace(0,np.nan,inplace=True)
    df2=pd.read_csv(file_b,sep=" ",header=0)
    df2.replace(0,np.nan,inplace=True)
    df3=pd.read_csv(file_c,sep=" ",header=0)
    df3.replace(0,np.nan,inplace=True)
    df4=pd.read_csv(file_d,sep=" ",header=0)
    df4.replace(0,np.nan,inplace=True)

    # Plot: synth data load time, n++ / e=4 / l=2
    fig1,((ax1,ax3),(ax2,ax4))=plt.subplots(2,2)
    df1a=df1[["node_size","multinet_load","muxviz_load","pymnet_load","py3plex_load"]]
    df1a.plot(
        ax=ax1,
        x="node_size",
        logy=True,
        logx=True,
        xticks=df1["node_size"],
        style=['+--','o--','.:','x:']
        #title="Network loading time, synthetic data, increasing number of vertices"
    )
    ax1.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax1.legend().set_visible(False)
    #ax1.set_ylabel("Network loading time (sec.)")
    ax1.set_ylabel("")
    #ax1.set_xlabel("Number of vertices")
    ax1.set_xlabel("")
    #plt.savefig("../logs/plots/exp7a_load_synth_nplus_e4_l2.png",transparent=True,dpi=300,format="png")
    #plt.show()

    # Plot: synth data load time, n++ / e=s / l=2
    #fig2,ax2=plt.subplots()
    df2a=df2[["node_size","multinet_load","muxviz_load","pymnet_load","py3plex_load"]]
    df2a.plot(
        ax=ax2,
        x="node_size",
        logy=True,
        logx=True,
        xticks=df2["node_size"],
        style=['+--','o--','.:','x:']
        #title="Network loading time, large datasets"
    )
    ax2.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax2.legend().set_visible(False)
    #ax2.set_ylabel("Network loading time (sec.)")
    ax2.set_ylabel("")
    ax2.set_xlabel("Number of vertices")
    #plt.savefig("../logs/plots/exp7b_load_synth_nplus_es_l2.png",transparent=True,dpi=300,format="png")
    #plt.show()

    # Plot: synth data load time, n=1000 / e=4 / l++
    #fig3,ax3=plt.subplots()
    df3a=df3[["layer_size","multinet_load","muxviz_load","pymnet_load","py3plex_load"]]
    df3a.plot(
        ax=ax3,
        x="layer_size",
        logy=True,
        logx=True,
        xticks=df3["layer_size"],
        style=['+--','o--','.:','x:']
        #title="Network loading time, synthetic data, increasing number of vertices"
    )
    ax3.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax3.legend().set_visible(False)
    #ax3.set_ylabel("Network loading time (sec.)")
    #ax3.set_xlabel("Number of layers")
    ax3.set_ylabel("")
    ax3.set_xlabel("")
    #plt.savefig("../logs/plots/exp7c_load_synth_n1000_e4_lplus.png",transparent=True,dpi=300,format="png")
    #plt.show()

    # Plot: synth data load time, n=1000 / e=s / l++
    #fig4,ax4=plt.subplots()
    df4a=df4[["layer_size","multinet_load","muxviz_load","pymnet_load","py3plex_load"]]
    df4a.plot(
        ax=ax4,
        x="layer_size",
        logy=True,
        logx=True,
        xticks=df4["layer_size"],
        style=['+--','o--','.:','x:']
        #title="Network loading time, large datasets"
    )
    ax4.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax4.legend().set_visible(False)
    #ax4.set_ylabel("Network loading time (sec.)")
    ax4.set_ylabel("")
    ax4.set_xlabel("Number of layers")
    #plt.savefig("../logs/plots/exp7d_load_synth_n1000_es_lplus.png",transparent=True,dpi=300,format="png")
    #plt.show()

    fig1.supylabel("Network loading time (sec.)")

    libs=["multinet","MuxViz","Pymnet","Py3plex"]
    lines_labels = [ax.get_legend_handles_labels() for ax in fig1.axes]
    lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
    fig1.legend(lines,libs,ncol=len(libs),loc="upper center")

    fig1.savefig("../logs/plots/exp7.png",transparent=True,dpi=300,format="png")
    fig1.show()

    #
    ##### Commenting degree plots, unnecessary.
    #
    # # Plot: synth data degree time, n++ / e=4 / l=2
    # fig5,ax5=plt.subplots()
    # df1b=df1[["node_size","multinet_degr","muxviz_degr","pymnet_degr","py3plex_degr","mlgjl_degr"]]
    # df1b.plot(
    #     ax=ax5,
    #     x="node_size",
    #     logy=True,
    #     logx=True,
    #     xticks=df1["node_size"],
    #     style=['+--','o--','.:','x:','d-.']
    #     #title="Degree calculation time, small datasets"
    # )
    # ax5.legend(["multinet","MuxViz","Pymnet","Py3plex","MLG.jl"])
    # ax5.set_ylabel("Degree computation time (sec.)")
    # ax5.set_xlabel("Number of vertices")
    # plt.savefig("../logs/plots/exp7a_degr_synth_nplus_e4_l2.png",transparent=True,dpi=300,format="png")
    # plt.show()


    # # Plot: synth data degree time, n++ / e=s / l=2
    # fig6,ax6=plt.subplots()
    # df2b=df2[["node_size","multinet_degr","muxviz_degr","pymnet_degr","py3plex_degr","mlgjl_degr"]]
    # df2b.plot(
    #     ax=ax6,
    #     x="node_size",
    #     logy=True,
    #     logx=True,
    #     xticks=df2["node_size"],
    #     style=['+--','o--','.:','x:','d-.']
    #     #title="Degree calculation time, large datasets"
    # )
    # ax6.legend(["multinet","MuxViz","Pymnet","Py3plex","MLG.jl"])
    # ax6.set_ylabel("Degree computation time (sec.)")
    # ax6.set_xlabel("Number of vertices")
    # plt.savefig("../logs/plots/exp7b_degr_synth_nplus_es_l2.png",transparent=True,dpi=300,format="png")
    # plt.show()

    # # Plot: synth data degree time, n=1000 / e=4 / l++
    # fig7,ax7=plt.subplots()
    # df3b=df3[["layer_size","multinet_degr","muxviz_degr","pymnet_degr","py3plex_degr","mlgjl_degr"]]
    # df3b.plot(
    #     ax=ax7,
    #     x="layer_size",
    #     logy=True,
    #     logx=True,
    #     xticks=df3["layer_size"],
    #     style=['+--','o--','.:','x:','d-.']
    #     #title="Degree calculation time, small datasets"
    # )
    # ax7.legend(["multinet","MuxViz","Pymnet","Py3plex","MLG.jl"])
    # ax7.set_ylabel("Degree computation time (sec.)")
    # ax7.set_xlabel("Number of layers")
    # plt.savefig("../logs/plots/exp7c_degr_synth_n1000_e4_lplus.png",transparent=True,dpi=300,format="png")
    # plt.show()


    # # Plot: synth data degree time, n=1000 / e=s / l++
    # fig8,ax8=plt.subplots()
    # df4b=df4[["layer_size","multinet_degr","muxviz_degr","pymnet_degr","py3plex_degr","mlgjl_degr"]]
    # df4b.plot(
    #     ax=ax8,
    #     x="layer_size",
    #     logy=True,
    #     logx=True,
    #     xticks=df4["layer_size"],
    #     style=['+--','o--','.:','x:','d-.']
    #     #title="Degree calculation time, large datasets"
    # )
    # ax8.legend(["multinet","MuxViz","Pymnet","Py3plex","MLG.jl"])
    # ax8.set_ylabel("Degree computation time (sec.)")
    # ax8.set_xlabel("Number of layers")
    # plt.savefig("../logs/plots/exp7d_degr_synth_n1000_es_lplus.png",transparent=True,dpi=300,format="png")
    # plt.show()    

    return

# Plotting experiment 8.
def plot_exp8(file_a):
    # Read files
    df1=pd.read_csv(file_a,sep=" ",header=0)
    df1.replace(0,np.nan,inplace=True)

    # Plot: small datasets, aggregation time
    fig1,ax1=plt.subplots()
    df1.plot(
        ax=ax1,
        logy=True,
        style=['+--','o--','.:','x:']
        #title="Dimension aggregation time, small datasets"
    )
    ax1.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax1.set_ylabel("Total time elapsed (sec.)")
    ax1.set_xlabel("Basic manipulation operations done (x10^4)")
    plt.savefig("../logs/plots/exp8_rebuild.png",transparent=True,dpi=300,format="png")
    plt.show()

    return

# Mainest of the mains
def main():

    # # Run for experiment 1
    # plot_exp1("../logs/plot_exp1a.txt","../logs/plot_exp1b.txt")
    
    # # Run for experiment 2
    # plot_exp2("../logs/plot_exp2a.txt","../logs/plot_exp2b.txt")

    # # Run for experiment 4
    # plot_exp4("../logs/plot_exp4a.txt","../logs/plot_exp4b.txt")

    # # Run for experiment 5
    # plot_exp5("../logs/plot_exp5a.txt","../logs/plot_exp5b.txt")

    # Run for experiment 6: aggregating synth
    plot_exp6(
        "../logs/plot_exp6a.txt",
        "../logs/plot_exp6b.txt",
        "../logs/plot_exp6c.txt",
        "../logs/plot_exp6d.txt"
    )

    # Run for experiment 7: loading synth
    plot_exp7(
        "../logs/plot_exp7a_comp.txt",
        "../logs/plot_exp7b_comp.txt",
        "../logs/plot_exp7c_comp.txt",
        "../logs/plot_exp7d_comp.txt"
    )
    
    # Run for experiment 8: network update
    plot_exp8("../logs/plot_exp8.txt")

    return

if __name__ == "__main__":
    main()
