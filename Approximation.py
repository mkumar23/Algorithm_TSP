import networkx as nx
import readData
import prim
import sys
import time

def dfs(G, i):
    visited[i - 1] = True
    record.append(i)
    for s,t,w in G.edges(i,data=True):
        if visited[t - 1] == False:
            dfs(G, t)

start_time = time.time()
G, optimal = readData.createGraph(sys.argv[1])
T, non = prim.primMST(G)

visited = [False] * len(T)
record = []
dfs(T, 1)
#print record
length = 0
for i in xrange(len(record)-1):
    length += G.get_edge_data(record[i], record[i+1])['weight']

total_time = (time.time() - start_time)
print total_time, length, optimal, float(length - int(optimal))/float(optimal)
