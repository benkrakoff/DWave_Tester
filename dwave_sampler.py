#docs for reference
#https://docs.ocean.dwavesys.com/en/stable/docs_system/reference/samplers.html#dwavesampler
#This may be helpful later to keep results
#https://docs.ocean.dwavesys.com/en/stable/docs_dimod/reference/generated/dimod.SampleSet.to_pandas_dataframe.html#dimod.SampleSet.to_pandas_dataframe

from dwave.system import DWaveSampler, EmbeddingComposite, DWaveCliqueSampler
import dwave_networkx as dnx
import networkx as nx
import numpy as np
import pandas as pd
rng = np.random.default_rng()
import time

edge_weights = {}
#G = dnx.pegasus_graph(5)
G = nx.complete_graph(119)

for i in range(5):

    for e in G.edges():
        edge_weights[e] = 2*rng.binomial(1, .5)-1
    H = {}

    for n in G.nodes():
        col = []
        for m in G.nodes():
            if (n, m) in G.edges():
                col.append(edge_weights[(min(n, m), max(n, m))])
            else:
                col.append(0)
        H[n] = col
 
    pd.DataFrame.from_dict(H).to_csv("Clique_Hamiltonian_{k}".format(k = i+6))

    t_1 = time.time()
    #sampler for sparse graphs
    #sampleset = EmbeddingComposite(DWaveSampler()).sample_ising({}, edge_weights, num_reads = 1000)
    #sampler for clique graphs
    sampleset = DWaveCliqueSampler().sample_ising({}, edge_weights, num_reads = 1000)
    t_2 = time.time()

    sampleset.to_pandas_dataframe().to_csv("Clique_Sampler_Data_{k}".format(k=i+6))

    time_data = pd.read_csv("Time_Data")
    time_data.insert(len(time_data.columns), "Clique_Hamiltonian_{k}".format(k = i+6), t_2 - t_1)
    time_data.to_csv("Time_Data")

