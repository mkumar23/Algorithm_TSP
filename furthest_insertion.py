'''
Created on Nov 20, 2014

@author: Mrinal
'''
from pqdict import PQDict
import readData as read

def minCost(G,path,node):
    min_cost = float('inf')
    loc = -1
    if len(path) > 1:
        for pos in range(len(path)):
            cost = G.edge[path[pos]][node]['weight'] + G.edge[node][path[pos+1]]['weight'] - G.edge[path[pos]][path[pos+1]]['weight'] if pos+1 < len(path) \
                   else G.edge[path[pos]][node]['weight'] + G.edge[node][path[0]]['weight'] - G[path[pos]][path[0]]['weight']  
            if cost < min_cost: 
                min_cost = cost
                loc = pos+1
    else:
        min_cost = G.edge[path[0]][node]['weight'] + G.edge[node][path[0]]['weight']
        loc = 1
    return loc,min_cost

def greed():
    """ Return MST of the given undirected graph"""
    vis = set()
    tot_weight = 0
    pq = PQDict()            
    path = []
    G,optimal = read.createGraph('Data\\burma14.tsp')
    for node in G.nodes():
        pq.additem(node, float("-inf"))
    
    curr = pq.pop()
    vis.add(curr)
    path.append(curr)
    while len(pq) > 0:
        for s,nod, wt in G.edges(curr, data=True):
            if nod not in vis and -wt['weight'] > pq[nod]: pq.updateitem(nod, -wt['weight']) 
        
        if len(pq)>0:
            ''' Selection Step'''
            top = pq.top()
            vis.add(top)
            curr = pq.pop()
            ''' Insertion Step'''
            loc,cost = minCost(G,path,top)
            path.insert(loc, top)
            tot_weight += cost
            
    print tot_weight,optimal,tot_weight/float(optimal)
    return tot_weight

greed()