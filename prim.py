from pqdict import PQDict
import networkx as nx

def prim(G):
    """ Return MST of the given undirected graph"""
    #sumWeight = 0
    heap = PQDict()
    for u in G.nodes():
        heap[u] = float("inf")

    flag = [False] * len(G)
    pointer = [None] * len(G)
    heap[1] = 0
    pointer[0] = -1
    T = nx.Graph()

    while len(heap) != 0:
        [u, value] = heap.popitem()
        flag[u - 1] = True
        if pointer[u - 1] != -1:
            T.add_edge(pointer[u - 1], u, weight = value)
        #sumWeight += value
        for s,v,w in G.edges(u, data=True):
            if flag[v - 1] is False:
                value = min(heap[v], w['weight'])
                if w['weight'] == value:
                    pointer[v - 1] = u
                heap[v] = value
    return T
