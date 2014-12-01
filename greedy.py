'''
Created on Nov 11, 2014

@author: Mrinal
'''
from pqdict import PQDict
import readData as read

def greedy_approx(G):
    vis = set()
    pq = PQDict()
    tot_length = 0
    seq = []
    start = 1
    curr = start
    vis.add(curr)
    seq.append(curr)
    while len(seq) != len(G.nodes()):
        next = [list for list in (sorted(G.edges(curr, data=True), key=lambda (source,target,data): data['weight'])) if list[1] not in vis][0] 
        curr = next[1]
        vis.add(curr)
        seq.append(curr)
        tot_length += next[2]['weight']
        
    next = [list for list in (sorted(G.edges(curr, data=True), key=lambda (source,target,data): data['weight'])) if list[1] == start][0]
    seq.append(next[1])
    tot_length += next[2]['weight']
#     print optimal, tot_length, tot_length/float(int(optimal))
    return tot_length

# print greed()[1]