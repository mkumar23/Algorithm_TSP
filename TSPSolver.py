'''
Created on Nov 16, 2014

@author: Naman
'''
import networkx as nx
from readData import createGraph
from BranchAndBound import branchAndBound

G, optimalCost=createGraph('C:\\Users\\Naman\\Dropbox\\gatech\\ALGO\\project\\DATA\\ulysses16.tsp')

# G=nx.Graph()
# G.add_edge(1,2,weight=5)
# G.add_edge(2,3,weight=6)
# G.add_edge(3,4,weight=3)
# G.add_edge(4,1,weight=7)
# G.add_edge(2,4,weight=4)
# G.add_edge(1,3,weight=2)
# G.add_edge(1,5,weight=3)
# G.add_edge(2,5,weight=6)
# G.add_edge(3,5,weight=4)
# G.add_edge(4,5,weight=5)


bnbCost=branchAndBound(G)