import dwave_networkx as dnx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import networkx as nx
rng = np.random.default_rng()

edge_weights = {}

G = nx.complete_graph(40)

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

pd.DataFrame.from_dict(H).to_csv("Test Clique Hamiltonian")