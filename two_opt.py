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

def randomPerturbation(tour):
    cities=random.sample(range(0,len(tour)),4)
    cities.sort()
    c1,c2,c3,c4=cities[0],cities[1],cities[2],cities[3]
    tour1,tour2,tour3,tour4=[],[],[],[]
    length=len(tour)
    i=c1
    while i!=c2:
        tour1.append(tour[i])
        i=(i+1)%length
    i=c2
    while i!=c3:
        tour2.append(tour[i])
        i=(i+1)%length
    
    i=c3
    while i!=c4:
        tour3.append(tour[i])
        i=(i+1)%length
    
    i=c4
    while i!=c1:
        tour4.append(tour[i])
        i=(i+1)%length
        
    newtour = tour1+ tour3[::-1]+tour4[::-1]+tour2
#     print c1,c2,c3,c4
#     print tour[:c1],
#     print tour[c3:c4][::-1],
#     print tour[c1:c2],
#     print tour[c3:c2][::-1],
#     print tour[c4:]
#     newTour=tour[:c1]+tour[c3:c4][::-1]+tour[c1:c2]+tour[c3:c2][::-1]+ tour[c4:]

    return newtour
    
    
    
def two_opt(G,cutoff,seed,ftrace):
    tour=G.nodes()
    random.seed(seed)
    random.shuffle(tour)
    tour,_=mst_approx(G)
    
    nodeCount=len(tour)
    bestDistanceSoFar=findCost(G, tour)
    bestTour=tour
    count=0
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time>cutoff:
            return bestTour,bestDistanceSoFar
        
        lastBest=bestDistanceSoFar
        bestInThisIteration=bestDistanceSoFar
        bestTourInThisIteraion=tour
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

#              First find
                newTour=two_swap(tour,i,j)
                newDistance=findCost(G, newTour)
#                 print newDistance
                if newDistance<bestDistanceSoFar:
                    print newDistance
                    tour=newTour
                    bestDistanceSoFar=newDistance
                    bestTour=newTour
                    ftrace.write("{0:.2f}".format(elapsed_time*1.0)+','+str(bestDistanceSoFar)+'\n')

#              Best FInd
#                 newTour=two_swap(tour,i,j)
#                 newDistance=findCost(G, newTour)
#                 if newDistance<bestInThisIteration:
#                     bestTourInThisIteraion=newTour
#                     bestInThisIteration=newDistance
#                     ftrace.write("{0:.2f}".format(elapsed_time*1.0)+','+str(bestDistanceSoFar)+'\n')

#         if bestInThisIteration < bestDistanceSoFar:
#             bestDistanceSoFar=bestInThisIteration
#             bestTour=bestTourInThisIteraion
#             tour=bestTourInThisIteraion
#             print bestDistanceSoFar

#       Random perturbation
        if bestDistanceSoFar==lastBest:
            count+=1
        else:
            count=0
        if count>3:
            tour=randomPerturbation(bestTour)
            print findCost(G, tour)
            print 'random perturb'
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
