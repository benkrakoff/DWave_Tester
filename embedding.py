import dwave_networkx as dnx
import matplotlib.pyplot as plt

G = dnx.pegasus_graph(2)
dnx.draw_pegasus(G, with_labels=True, crosses=True, node_color="Yellow")
plt.savefig("Plot")