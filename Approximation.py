import networkx as nx
import readData
from prim import prim
import sys

def dfs(G, i):
    visited[i - 1] = True
    record.append(i)
    for s,t,w in G.edges(i,data=True):
        if visited[t - 1] == False:
            dfs(G, t)

G, optimal = readData.createGraph(sys.argv[1])
T = prim(G)

visited = [False] * len(T)
record = []
dfs(T, 1)

nodes = list(nx.dfs_preorder_nodes(T,1))
length = 0
for i in xrange(len(nodes)-1):
    length += G.get_edge_data(nodes[i], nodes[i+1])['weight']

print length, optimal, float(length)/float(optimal)
