import dwave_networkx as dnx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
rng = np.random.default_rng()

edge_weights = {}

G = dnx.pegasus_graph(2)

for e in G.edges():
    edge_weights[e] = 2*rng.binomial(1, .5)-1

H1 = {}

for n in G.nodes():
    col = []
    for m in G.nodes():
        if (n, m) in G.edges():
            col.append(edge_weights[(min(n, m), max(n, m))])
        else:
            col.append(0)
    H1[n] = col

times = {"Hamiltonian_1":[0]}
pd.DataFrame.from_dict(times).to_csv("Time_Data")