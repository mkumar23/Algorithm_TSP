'''
Created on Nov 30, 2014

@author: Naman
'''
import random
import time
from Approximation import mst_approx

def findCost(G,tour):
    cost=0
    if(len(tour)==1):
        return 0
    for i,node in enumerate(tour):
        if i<len(tour)-1:
            cost+=G.get_edge_data(tour[i],tour[i+1])['weight']
    cost+=G.get_edge_data(tour[i],tour[0])['weight']
    return cost

def two_swap(tour,city1,city2):
    newTour=[]
    for i in xrange(city1):
        newTour.append(tour[i])
    for i in xrange(city2,city1-1,-1):
        newTour.append(tour[i])
    for i in xrange(city2+1,len(tour)):
        newTour.append(tour[i])
    return newTour

def three_swap(tour,city1,city2,city3):
    newTour=[]
    for i in xrange(city1):
        newTour.append(tour[i])
    for i in xrange(city3,city2-1,-1):
        newTour.append(tour[i])
    for i in xrange(city1,city2,1):
        newTour.append(tour[i])
    for i in xrange(city3+1,len(tour)):
        newTour.append(tour[i])

    return newTour  

def two_opt(G,cutoff,seed,ftrace):
    tour=G.nodes()
    random.seed(seed)
    random.shuffle(tour)
    tour,_=mst_approx(G)
    
    nodeCount=len(tour)
    bestDistanceSoFar=findCost(G, tour)
    bestTour=tour
    
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time>cutoff:
            return bestTour,bestDistanceSoFar
        
        for i in xrange(nodeCount):
            for j in xrange(i+1,nodeCount):
#                 newTour=[]
#                 c1=i
#                 c2=(i+1)%nodeCount
#                 c3=j
#                 c4=(j+1)%nodeCount
#                 if G.get_edge_data(tour[c1],tour[c2])['weight'] + G.get_edge_data(tour[c3],tour[c4])['weight'] >G.get_edge_data(tour[c1],tour[c4])['weight'] + G.get_edge_data(tour[c2],tour[c3])['weight']:
#                       newTour[:c1]=tour[:c1]
#                       newTour[c1+1]
                
                
                newTour=two_swap(tour,i,j)
                newDistance=findCost(G, newTour)
                if newDistance<bestDistanceSoFar:
                    print newDistance
                    tour=newTour
                    bestDistanceSoFar=newDistance
                    bestTour=newTour
                    ftrace.write("{0:.2f}".format(elapsed_time*1.0)+','+str(bestDistanceSoFar)+'\n')

#         for i in xrange(nodeCount):
#             for j in xrange(i+1,nodeCount):
#                 for k in xrange(j+1,nodeCount):
#                     newTour=three_swap(tour,i,j,k)
#                     newDistance=findCost(G, newTour)
#                     if newDistance<bestDistanceSoFar:
#                         print newDistance
#                         tour=newTour
#                         bestDistanceSoFar=newDistance
#                         bestTour=newTour
#         print 'whole run'
    return bestTour,bestDistanceSoFar
 
# print three_swap([1,2,3,4,5,6,7,8,9,10],3,5,7)   
