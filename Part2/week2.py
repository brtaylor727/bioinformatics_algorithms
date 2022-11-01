#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 17:33:41 2022

@author: brian
"""

import numpy as np
import random
import pandas as pd
import week1

"""
EulerianCycle(Graph)
    form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
    while there are unexplored edges in Graph
        select a node newStart in Cycle with still unexplored edges
        form Cycle’ by traversing Cycle (starting at newStart) and then randomly walking 
        Cycle ← Cycle’
    return Cycle


You should now be prepared to solve the Eulerian Cycle Problem for any graph.
It may not be obvious, but a good implementation of EulerianCycle will work
in linear time. To achieve this runtime speedup, you would need to use an
efficient data structure in order to maintain the current cycle that Leo is
building as well as the list of unused edges incident to each node and the
list of nodes on the current cycle that have unused edges.


"""

#%%quiz

#1
onestring = """AAAT

AATG

ACCC

ACGC

ATAC

ATCA

ATGC

CAAA

CACC

CATA

CATC

CCAG

CCCA

CGCT

CTCA

GCAT

GCTC

TACG

TCAC

TCAT

TGCA"""

def findStart(formatted):
    return [i for i in formatted if i[:-1] not in [i[1:] for i in formatted]][0]


formatted = onestring.split()
from collections import defaultdict




stringtest = ''


beststring = ''
#for mainkey in keys:
beststrings = []
#while len(beststring) != 24:
for count in range(2000):
    ans = week1.OverlapGraphProblem(' '.join(formatted))
    keys = list(ans.keys())
    mainkey  = keys[np.random.randint(0,len(keys))]
    key = findStart(formatted)
    stringtest = key

    #while key != mainkey:
    while True:
        #if firstrun == True:
        #    key = mainkey
        #    firstrun = False
        try:
            nextkey = ans[key][np.random.randint(0,len(ans[key]))]
            ans[key].remove(nextkey)
        except:
            break
        stringtest = stringtest+nextkey[-1]
        key = nextkey
    beststring = stringtest
    #if len(stringtest) > len(beststring):
    #    beststring = stringtest
    #    print(stringtest,'\n')
    #if len(beststring) == 24:
    beststrings.append(beststring)
    #print(len(beststring))
    
print(beststring,len(beststring),len(formatted)+3)
print(set(beststrings))     

print([i for i in list(set(beststrings)) if len(i) == 24]) #number of kmers + k -1

#%%

def readGraphFile(filename):
    strings = open(inputgraphfile).read().strip().split('\n')
    
    #print(strings)
    
    keys = [int(j[0]) for j in [i.split(': ') for i in strings]]
    values = [list(np.int_(j[1].split())) for j in [i.split(': ') for i in strings]]
    
    
    
    return dict(zip(keys,values))


def EulerianCycle_old(Graph):
    print('start cycle----------------------')
    
    unvisitednodes_rand = list(Graph.keys())
    random.shuffle(unvisitednodes_rand)
    
    
    #firststart = unvisitednodes[np.random.randint(0,len(unvisitednodes))]
    
    for firststart in unvisitednodes_rand:
        cycle = []
        unvisitednodes = list(Graph.keys())
        unvisitednodes.remove(firststart)
        cycle.append(firststart)
        print('firststart:',firststart)
        
        keepgoing = True
        while keepgoing:
            
            if len(unvisitednodes) == 0:
                return cycle
            
            
            availableoptions = Graph[cycle[-1]]
            print('unvisitednodes: ',unvisitednodes)
            
            optionslist = np.arange(len(availableoptions))
            random.shuffle(optionslist)
            
            for iguess in optionslist:
                #print('iguess:',iguess)
                nextstep = availableoptions[iguess]
                print('nextstep:',nextstep)
                print('Trueth:',nextstep in unvisitednodes)
        
                if nextstep in unvisitednodes:
                    unvisitednodes.remove(nextstep)
                    cycle.append(nextstep)
                    keepgoing = True
                    break
                keepgoing = False
                    
    
                 
        if len(cycle) == len(Graph.keys()):
            return cycle
        if len(unvisitednodes) == 0:
            return cycle
                    
                    
def getVisitedEdgesFromCycle(cycle):
    return [(cycle[i],cycle[i+1]) for i in range(len(cycle)-1)]
    
def getUnvisistedVertices(Graph):
    Vertices = []
    for key in Graph.keys():
        for val in Graph[key]:
            Vertices.append((key,val))
    return Vertices

def getUnvisistedVertices_part2(Graph):
    #Graph = readGraphFile(inputgraphfile)
    df = pd.DataFrame(getUnvisistedVertices(Graph))
    sortfit = df.groupby(0).count().sort_values(1,ascending=False)
    df['count'] = df[0].map(sortfit[1])
    df = df.sort_values('count',ascending=False)
    Vertices = list(zip(df[0],df[1]))
    return Vertices

def findFirstStartNode(Graph,Vertices):
    df = pd.DataFrame(getUnvisistedVertices(Graph))
    dfg = pd.concat([df.groupby(1).count(),df.groupby(0).count()],axis=1).fillna(0)
    startnode = (dfg[0] - dfg[1]).sort_values().index[0]
    
    return [i for i in Vertices if i[0] == startnode][-1]

def firstStep(Graph,Vertices,cycle):
    
    
    #firststart = Vertices[0]
    firststart = findFirstStartNode(Graph,Vertices)
    print(firststart)
    
    Graph[firststart[0]].remove(firststart[1])
    Vertices.remove(firststart)
    
    cycle.append(firststart[0])
    cycle.append(firststart[1])

    return

def getNextMove(Graph,Vertices,cycle):
    lastNode = cycle[-1]
    
    try:
        options = Graph[lastNode]
    except KeyError:
        return None
    
    
    #print(options)
    
    if len(options) == 0:
        return None
    else:
        Nextmove = options[-1]
        Graph[lastNode].remove(Nextmove)
        Vertices.remove((lastNode,Nextmove))
        
        cycle.append(Nextmove)
        return Nextmove
    
def permuteCycle(cycle):
    cycle.append(cycle[1])
    cycle.remove(cycle[0])
    
def EulerianCycle(Graph,cycle=[]):
    print('start cycle----------------------')
    
    #startverteces = pd.DataFrame(getUnvisistedVertices(readGraphFile(inputgraphfile))).groupby(0).count().sort_values(1,ascending=False).index
    Vertices = getUnvisistedVertices_part2(Graph)
    
    
    firstStep(Graph,Vertices,cycle)
    print(cycle,len(Vertices))
    
    while len(Vertices) != 0:
        NextMove = getNextMove(Graph,Vertices,cycle)
        
        if NextMove == None:
            #cycle graph
            permuteCycle(cycle)
            #print(cycle)
            continue
        else:
            continue
    
    
    return cycle
    
    
        
        
    
def runEuler(inputfile):
    mygraph = readGraphFile(inputfile)
    cycle = EulerianCycle(mygraph,[])
    return cycle


inputgraphfile = """/Users/brian/Documents/python/Coursera-Bioinfomatics/Part 2/input-graph.txt"""
#inputgraphfile = "/Users/brian/Downloads/dataset_203_2 (2).txt"
#inputgraphfile = """/Users/brian/Documents/python/Coursera-Bioinfomatics/Part 2/input-graph2.txt"""


Graph = readGraphFile(inputgraphfile)
Vertices = getUnvisistedVertices_part2(Graph)

cycle = None
#while cycle == None:
cycle = runEuler(inputgraphfile)

#print(cycle)
ans = ' '.join([str(i) for i in cycle])
print(ans)


f = open('data.txt','w')
f.write(ans)
f.close()

"""
Code Challenge: Solve the Eulerian Path Problem.

Input: The adjacency list of a directed graph that has an Eulerian path.
Output: An Eulerian path in this graph.
"""
#%%
"""
StringSpelledByGappedPatterns(GappedPatterns, k, d)
    FirstPatterns ← the sequence of initial k-mers from GappedPatterns
    SecondPatterns ← the sequence of terminal k-mers from GappedPatterns
    PrefixString ← StringSpelledByGappedPatterns(FirstPatterns, k)
    SuffixString ← StringSpelledByGappedPatterns(SecondPatterns, k)
    for i = k + d + 1 to |PrefixString|
        if the i-th symbol in PrefixString does not equal the (i - k - d)-th symbol in SuffixString
            return "there is no string spelled by the gapped patterns"
    return PrefixString concatenated with the last k + d symbols of SuffixString

Code Challenge: Implement StringSpelledByGappedPatterns.

Input: Integers k and d followed by a sequence of (k, d)-mers (a1|b1), … , (an|bn) such that Suffix(ai|bi) = Prefix(ai+1|bi+1) for 1 ≤ i ≤ n-1.
Output: A string Text of length k + d + k + n - 1 such that the i-th (k, d)-mer in Text is equal to (ai|bi)  for 1 ≤ i ≤ n (if such a string exists).

"""
stringy = "GACC|GCGC ACCG|CGCC CCGA|GCCG CGAG|CCGG GAGC|CGGA"
def readString(string):
    splitstring = [i.split('|') for i in string.split(' ')]
    return [i[0] for i in splitstring],[i[1] for i in splitstring]

def StringSpelledByGappedPatterns(k, d, GappedPatterns):
    FirstPatterns = readString(GappedPatterns)[0]
    SecondPatterns = readString(GappedPatterns)[1]
    PrefixString = 
    SuffixString = 
    return
    
readString(stringy)
