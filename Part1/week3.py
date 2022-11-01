#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 13:15:51 2022

@author: brian
"""
"""
MotifEnumeration(Dna, k, d)
    Patterns ← an empty set
    for each k-mer Pattern in Dna
        for each k-mer Pattern’ differing from Pattern by at most d mismatches
            if Pattern' appears in each string from Dna with at most d mismatches
                add Pattern' to Patterns
    remove duplicates from Patterns
    return Patterns


"""
import pandas as pd
import numpy as np
import week2

def kmers(Dna,k):
    myKmers = []
    for piece in Dna:
        for i in range(len(piece)-k+1):
            myKmers.append(piece[i:i+k])
    return myKmers

def kmers_wrong(Dna,k):
    myKmers = []
    
    piece = ''.join([j for i in Dna for j in i])
    
    for i in range(len(piece)-k+1):
        myKmers.append(piece[i:i+k])
    return myKmers

def MotifEnumeration(Dna_in,k,d):
    patterns = []
    Dna = Dna_in.split()
    
    
    for pattern in kmers(Dna,k):
        
        
        for pattern2 in week2.neighbors(pattern, d):
            success = 0
            for piece in Dna:
                for i in range(len(piece)-k+1):
                    if week2.hammingDist(pattern2, piece[i:i+k]) <= d:
                        success = success+1
                        break
                    else:
                        continue
            if success == len(Dna):
                patterns.append(pattern2)
    patterns = list(set(patterns))
    return patterns
                
Motifs = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"
]
                 
def profile(motifs):
    
    prof = {}
    for nuc in ['A','G','C','T']:
        prof[nuc] = [0 for i in motifs[0]]
        
    for i in range(len(motifs[0])):
        for j in range(len(motifs)):
            #print(i)
            #print(motifs[j])
            prof[motifs[j][i]][i] = prof[motifs[j][i]][i]+1/len(motifs)
            
    return pd.DataFrame(prof)

def profilefunc(motifs):
    
    prof = {}
    for nuc in ['A','G','C','T']:
        prof[nuc] = [0 for i in motifs[0]]
        
    for i in range(len(motifs[0])):
        for j in range(len(motifs)):
            #print(i)
            #print(motifs[j])
            prof[motifs[j][i]][i] = prof[motifs[j][i]][i]+1/len(motifs)
            
    return pd.DataFrame(prof)

def entropy(df):
    return df.apply(lambda x: -x*np.log(x)/np.log(2)).fillna(0).sum().sum()
            
profile(Motifs)
profile(['AAAAAA','GGGGGG'])

print(entropy(profile(Motifs)))

entropy(profile(['AAAAAA','GGGGGG']))
            
#%%        
"""
MedianString(Dna, k)
    distance ← ∞
    for each k-mer Pattern from AA…AA to TT…TT
        if distance > d(Pattern, Dna)
             distance ← d(Pattern, Dna)
             Median ← Pattern
    return Median
"""


def d(pattern,Dna):
    Dna = Dna.split()
    k = len(pattern)
    success = 0
    for piece in Dna:
        hammingdist = np.inf
        for i in range(len(piece)-k+1):
            if hammingdist > week2.hammingDist(pattern, piece[i:i+k]):
                hammingdist = week2.hammingDist(pattern, piece[i:i+k])
                
                
        success = success + hammingdist
    return success


def medianString(k,Dna_in):
    Dna = Dna_in
    distance = np.inf
    #for pattern in week2.neighbors([i for i in range(k)], k):
    #for pattern in kmers(Dna_in.split(),k):
    for pattern in kmers_wrong(Dna_in.split(),k):
        #print(pattern,d(pattern,Dna))
        #if np.any([pattern in i for i in Dna_in.split()]):
        
            if distance > d(pattern,Dna):
                distance = d(pattern,Dna)
                Median = pattern
                print(pattern,distance)
        #else:
            #print(pattern)
    return Median


print(medianString(3,'AAATTGACGCAT GACGACCACGTT CGTCAGCGCCTG GCTGAGCACCGG AGTTCGGGACAG'))

stringy = """ACCGGTATATGCAGTATCATCGATATTAATGGGGCGGTGGAA
GACTTTATCAATGTATGCAGGCCTGTTGGCGGCCAGATTGGC
AGCAACATATGCACCTACAGATGCCATCTCTCATGATATAAG
AAAAGAGTATGCTGCTTTTAGCAAAATCATTGGAAGATTAGT
ACGAACACACACCTATGCGCCTGCCTTCGTAGATCTTCTATA
ATGTTTATCAAACTATGCCCTAGAACTGGTCTGTCACCCATT
ATATGCTTAGAGAGGGGCGTTCCTTTCGTACTCGTAAAATTA
TTCGGGAATGTGCTATGCTCTATAAGTATGATATAGAATTTA
TGCAGATCTTCAGTATGCCCTGCATCTTGTGATCGTTGCCGG
AGCTAACAAGAGATCGACGATTAAGTATGCAGACAGGCTAGA"""

print(medianString(6,stringy))


stringy = """CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC
GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC
GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"""

print(medianString(7,stringy))






#%%

def prob(df,motif):
    myprob = 1
    for i in range(len(df)):
        myprob = myprob*df.iloc[i][motif[i]]
    return myprob
        
print(prob(profile(Motifs),'TCGTGGATTTCC'))


#%%

profile = pd.DataFrame({
    'A': [0.2, 0.2, 0.3, 0.2, 0.3],
    'C': [0.4, 0.3, 0.1, 0.5, 0.1],
    'G': [0.3, 0.3, 0.5, 0.2, 0.4],
    'T': [0.1, 0.2, 0.1, 0.1, 0.2]
})

def mostProb(profile,text):
    mymax = 0
    
    #take a guess for best
    best = ''.join(profile.transpose().idxmax())
    
    for i in range(len(text)-len(profile)+1):
        #print(prob(profile,text[i:i+len(profile)]))
        if mymax < prob(profile,text[i:i+len(profile)]):
            best = text[i:i+len(profile)]
            mymax = prob(profile,text[i:i+len(profile)])
            #print(best,mymax,prob(profile,text[i:i+len(profile)]))
        #print(prob(profile,text[i:i+len(profile)]))
    return best

print(mostProb(profile,'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'))

stringy = """AGGGGGAGCCTCTAACCAAAATTGTGCCGTCATCTGAAAAGGGCGGGCCGCCGCGCTTTAAATCCTTTTGTGGAGAGCGCCAGAGGAGACCCCGGGAGTCTGCCCTCTAAGGCCGGCGACACGTGAAGATGGGTGTCTAGCCCGCATTTCTACTTTTAGATGTTTGTCCCTGGAGCAAACGAATAAACCGGGTGCACTCAGCCCCTACATCCGCATTCTGACAACAACGGGGGTGTTTTGACCACTCTTGTGGCTGAGACCGACCAGATGACGAAAGTACATGAAAAATAAATGGGTTTTCGGGATGGGTCCACCCTCCAGAACGTACCGACGCGCTTCCAAAGCAACATCTACTGCTCCTATAACCTCATGAGCATGACTTTTCTCCCGGGAGGATCGTGGCCGCCGGCTACGAGGAAAACTAGACTATGGTATCACGTCATCACTATTGCTGGTACAACAAGCCAGTTCCGGGGTGGCCATCCGCACTTCTCGCGACCGGCTGGATTCCGGAACTAAGACACGTTACTATTAGGCGTATTGCAGTAGACTAGTTCACACCCTCCGTAAAGACAGGTCAGCGCGACCGCGGTCCTCATGATGTATCGTAATTTCCCAGACCCCAATCGGGACTGTAGAACACCAGCAAATCATCTACGTAGACGTCAGTGCTTCCAACATTTTTGAGACTGCCATAGCGGGTTTTCATTTGGCACCTTATACAAGAATAGAAGATTTATTCCAGTATGACGAGGGGTTCACTTCCACCGAAGTACCAGAGATCGTGGTCTCGCTACACACTATCTCTGTTTTAAGAACAACTGCGGCCCAAGGTGATGTCTGACGATTCAATCCAAGAGTCGGCGTCTATAAAAACTTACATCAACCTAGTGCCTTAGCTGCGTAGTCCCGTTGAGTAAGAGGAATACACGGTGCGCTGCAGAAGTGGTATGCCCCGGTCTAACGTAGGAGGAGGGCATCGCTAGAATGAGAGAGTTCG"""
stringy2 = """0.253 0.265 0.169 0.193 0.301 0.253 0.133 0.277 0.205 0.265 0.277 0.241
0.205 0.229 0.289 0.313 0.301 0.157 0.265 0.229 0.253 0.157 0.193 0.301
0.205 0.253 0.277 0.253 0.217 0.325 0.337 0.217 0.289 0.253 0.265 0.229
0.337 0.253 0.265 0.241 0.181 0.265 0.265 0.277 0.253 0.325 0.265 0.229"""

profile = pd.DataFrame({j:[float(blah) for blah in i.split()] for i,j in zip(stringy2.split('\n'),['A','C','G','T'])})

print(mostProb(profile,stringy))

#%%

"""GreedyMotifSearch(Dna, k, t)
    BestMotifs ← motif matrix formed by first k-mers in each string from Dna
    for each k-mer Motif in the first string from Dna
        Motif1 ← Motif
        for i = 2 to t
            form Profile from motifs Motif1, …, Motifi - 1
            Motifi ← Profile-most probable k-mer in the i-th string in Dna
        Motifs ← (Motif1, …, Motift)
        if Score(Motifs) < Score(BestMotifs)
            BestMotifs ← Motifs
    return BestMotifs"""

#%%

print




























