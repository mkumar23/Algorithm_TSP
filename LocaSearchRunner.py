'''
Created on Dec 3, 2014

@author: Naman
'''
from readData import createGraph
from SA import simulated_annealiing
from two_opt import two_opt
 
 
files=['ulysses16.tsp','berlin52.tsp','kroA100.tsp','ch150.tsp','gr202.tsp']
cutoffs =[300,300,600,600,600]
optimal=[6859,7542,21282,6528,40160]
iter=0
for fileName in files:
    G,optimalCost=createGraph(fileName)
     
    cutoff=cutoffs[iter]
    count=0
    for i in xrange(10):
        currentFileName=fileName[:-4]+'_LS1_'+str(cutoff)+'_'+str(i)
        with open(currentFileName+ '.trace','w') as ftrace, open(currentFileName+ '.sol','w') as fsol:
            tour,foundCost=simulated_annealiing(G,i,cutoff,ftrace,optimal[iter])
            fsol.write(str(foundCost)+'\n')
            tourString=','.join(list(map(str,tour)))+','+str(tour[0])+'\n'
            fsol.write(tourString)
            print foundCost
            print 'naya run chala raha hu me'
    
    iter+=1