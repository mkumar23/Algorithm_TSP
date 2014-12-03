import networkx as nx
import readData
import sys
import time
import random
import math
from Approximation import mst_approx

def weight(path, G):
	length = 0
	for i in range(0, len(path) - 1):
		length = length + G.get_edge_data(path[i], path[i+1])['weight']
	length = length + G.get_edge_data(path[0], path[-1])['weight']
	return length

def two_swap(nodes):
	length = len(nodes) - 1
	idx1 = random.randint(0, length)
	idx2 = random.randint(idx1, length)
	new_nodes = nodes[:idx1] + nodes[idx1:idx2][::-1] + nodes[idx2:]
	return new_nodes

def SA(nodes, T, T_min, r, G,cutoff):
	while T > T_min:
		new_nodes = two_swap(nodes)
		dE = -(weight(new_nodes, G) - weight(nodes, G))
		if dE > 0:
			nodes = new_nodes
		else:
			if math.exp(dE / T) > random.random():
				nodes = new_nodes
		T = T * r
	return nodes

def simulated_annealiing(G,seed,cutoff):
# 	G, optimal = readData.createGraph(sys.argv[1])
	nodes = G.nodes()
	random.seed(seed)
	random.shuffle(nodes)
	
# 	nodes,_=mst_approx(G)
	T =  G.get_edge_data(max(G.edges())[0], max(G.edges())[1])['weight'] * len(G.nodes())
	r =  0.9999
	final_nodes = SA(nodes, T, 0.001, r, G,cutoff)
# 	print weight(final_nodes, G), optimal
	return final_nodes, weight(final_nodes, G)

# print simulated_annealiing()
