'''
Created on Nov 16, 2014

@author: Naman
'''
import sys
from readData import createGraph
from BranchAndBound import branchAndBound
from SA import simulated_annealiing
from Approximation import mst_approx
from greedy import greedy_approx
def solver(argv):
    for i,x in enumerate(argv):
        if argv[i]=='-alg':
            algo=argv[i+1]
        elif argv[i]=='-inst':
            fileName=argv[i+1]
        elif argv[i]=='-time':
            cutoff=int(argv[i+1])
        elif argv[i]=='-seed':
            seed=int(argv[i+1])
            
    G, optimalCost=createGraph(fileName)
    
    if algo=='BnB':
        tour,foundCost=branchAndBound(G,cutoff)
    elif algo=='Approx':
        tour,foundCost=mst_approx(G)
    elif algo=='Heur':
        foundCost=greedy_approx(G)
    elif algo=='LS1':
        tour,foundCost=simulated_annealiing(G,seed)
    
    print tour,foundCost
    

if __name__ == "__main__":
    solver(sys.argv[1:])

# _,bnbCost=simulated_annealiing(G)
# print bnbCost
