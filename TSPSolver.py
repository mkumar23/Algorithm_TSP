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
from two_opt import two_opt

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
#     fileName='ulysses16.tsp'
    G, optimalCost=createGraph(fileName)

    print optimalCost    
    if algo=='BnB':
        with open(fileName[:-4]+'_BnB_'+str(cutoff)+'.trace','w') as ftrace:
            tour,foundCost=branchAndBound(G,cutoff,ftrace)
    elif algo=='Approx':
        tour,foundCost=mst_approx(G)
    elif algo=='Heur':
        foundCost=greedy_approx(G)
    elif algo=='LS1':
        with open(fileName[:-4]+'_LS1_'+str(seed)+'_'+str(cutoff)+'.trace','w') as ftrace:
            tour,foundCost=simulated_annealiing(G,seed,cutoff,ftrace)
    elif algo=='LS2':
        with open(fileName[:-4]+'_LS2_'+str(seed)+'_'+str(cutoff)+'.trace','w') as ftrace:
            tour,foundCost=two_opt(G,cutoff,seed,ftrace)
    
    print tour,foundCost
    

if __name__ == "__main__":
    solver(sys.argv[1:])

# _,bnbCost=simulated_annealiing(G)
# print bnbCost
