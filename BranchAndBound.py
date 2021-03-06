'''
Created on Nov 16, 2014

@author: Naman
'''
from pqdict import PQDict
# from prim import prim
from prim import primWeight
from itertools import count
import time
from math import isinf
INFINITY=10000000
def lowerBound(G,tour):
    nodeList=[node for node in G.nodes() if not node in tour]
#     list(set(G.nodes())-set(tour))
    H=G.subgraph(nodeList)
    lowerBoundValue=0
    for node in nodeList:
        edges=[edge[2]['weight'] for edge in H.edges(node,data=True)]
        if len(edges)>0:
            min1=min(edges)
            lowerBoundValue+=min1
          
        if (len(edges)>1):
            edges.remove(min1)
            min2=min(edges)
            lowerBoundValue+=min2
    minOutgoingEdge=min([G.get_edge_data(tour[-1],node)['weight'] for node in nodeList])
    minIncomingEdge=min([G.get_edge_data(node,tour[0])['weight'] for node in nodeList])
    return (lowerBoundValue/2)+findCost(G, tour)+minIncomingEdge+minOutgoingEdge

# def lowerBound(G,tour):
# #     minPrev=lowerBoundNew(G, tour)
#      
#     nodeList=list(set(G.nodes())-set(tour))
# #     print nodeList
#     minOutgoingEdge=min([G.get_edge_data(tour[-1],node)['weight'] for node in nodeList])
#     minIncomingEdge=min([G.get_edge_data(node,tour[0])['weight'] for node in nodeList])
#     mincurrent=primWeight(G.subgraph(nodeList)) + findCost(G, tour) +minIncomingEdge+minOutgoingEdge
# #     if(mincurrent<minPrev):
# #         return minPrev
#     return mincurrent

def findCost(G,tour):
    cost=0
    if(len(tour)==1):
        return 0
    for i,node in enumerate(tour):
        if i<len(tour)-1:
#             print G.get_edge_data(tour[i],tour[i+1])['weight']
            cost+=G.get_edge_data(tour[i],tour[i+1])['weight']
#         else:
# #             print tour
#             cost+=G.get_edge_data(tour[i],tour[0])['weight']
    return cost
def branchAndBound(G,cutoff,ftrace):
    queue=PQDict()
    bestSolution= INFINITY
    bestTour=[]
    totalNodes=len(G.nodes())
    startNode=G.nodes()[0]
    nodeList=G.nodes()
    nodeList.remove(startNode)
    queue.additem(tuple([startNode]),lowerBound(G,[startNode]))
    
    
    start_time = time.time()
    while(len(queue)!=0):
#         print count
#         count+=1
        coveredNodes,lowerBoundCurrent=queue.popitem()
#         coveredNodes=list(coveredNodes)

        elapsed_time = time.time() - start_time
        if elapsed_time>cutoff:
            if bestSolution==INFINITY:
                return -1,[]
            return bestTour,bestSolution
        
        for neighbor in G.neighbors(coveredNodes[-1]):
            if not neighbor in coveredNodes:
                tempNodes=list(coveredNodes)
                tempNodes.append(neighbor)
                if(len(tempNodes) == totalNodes):
                    cost=findCost(G, tempNodes) + G.get_edge_data(neighbor,startNode)['weight']
                    if(cost < bestSolution):
                        bestSolution= cost
                        bestTour=tempNodes
                        ftrace.write("{0:.2f}".format(elapsed_time*1.0)+','+str(bestSolution)+'\n')
                else:
                    tempLowerBound=lowerBound(G, tempNodes)
                    if tempLowerBound < bestSolution:
                        queue.additem(tuple(tempNodes),tempLowerBound)
#                     else:
#                         print 'prune'
    return bestTour,bestSolution
    
    