#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 10:39:47 2022

@author: brian
"""

import numpy as np
import pandas as pd

"""

GreedyChange(money)
    change ← empty collection of coins)
    while money > 0
        coin ← largest denomination that is less than or equal to money
        add a coin with denomination coin to the collection of coins change
        money ← money − coin
    return change

"""

def pick_coin(money,coins):
    for coin in coins:
        if money / coin >= 1:
            #print(coin)
            return coin

def greedychange(money):
    coins = [100, 50, 25, 10, 5, 1]
    change = []
    while money > 0:
        #print(money)
        coin = pick_coin(money,coins)
        #print(coin)
        change.append(coin)
        money -= coin
    return change

"""
RecursiveChange(money, Coins)
    if money = 0
        return 0
    MinNumCoins ← ∞
    for i ← 0 to |Coins| - 1
        if money ≥ coini
            NumCoins ← RecursiveChange(money − coini, Coins)
            if NumCoins + 1 < MinNumCoins
                MinNumCoins ← NumCoins + 1
    return MinNumCoins
"""

def recursive_change(money,coins):
    print(money)
    if money == 0:
        return 0
    minNumCoins = np.inf
    for i in range(len(coins)):
        if money >= coins[i]:
            NumCoins = recursive_change(money-coins[i],coins)
            if NumCoins + 1 < minNumCoins:
                minNumCoins = NumCoins + 1
    return minNumCoins

"""
DPChange(money, Coins)
    MinNumCoins(0) ← 0
    for m ← 1 to money
        MinNumCoins(m) ← ∞
            for i ← 0 to |Coins| - 1
                if m ≥ coini
                    if MinNumCoins(m - coini) + 1 < MinNumCoins(m)
                        MinNumCoins(m) ← MinNumCoins(m - coini) + 1
    output MinNumCoins(money)
"""

def dynamic_change(money,coins):
    coins = [int(i) for i in coins.split(' ')]
    money = int(money)
    
    minNumCoins = {0:0}
    for m in range(1,money+1):
        minNumCoins[m] = np.inf
        for i in range(len(coins)):
            if m>= coins[i]:
                if minNumCoins[m-coins[i]]  + 1 < minNumCoins[m]:
                    minNumCoins[m] = minNumCoins[m-coins[i]] + 1
    return minNumCoins[money]


dynamic_change(18584,'14 5 3 1')


"""
ManhattanTourist(n, m, Down, Right)
    s0, 0 ← 0
    for i ← 1 to n
        si, 0 ← si-1, 0 + downi-1, 0
    for j ← 1 to m
        s0, j ← s0, j−1 + right0, j-1
    for i ← 1 to n
        for j ← 1 to m
            si, j ← max{si - 1, j + downi-1, j, si, j - 1 + righti, j-1}
    return sn, m
"""

def readmanhatten(inputstring):
    beginning = inputstring.split('\n')[0].split(' ')
    n = int(beginning[0])
    m = int(beginning[1])
    
    end = '\n'.join(inputstring.split('\n')[1:])
    down = [[int(j) for j in i.split(' ')] for i in end.split('-\n')[0].split('\n')[:-1]]
    right = [[int(j) for j in i.split(' ')] for i in end.split('-\n')[1].split('\n')]
    
    return n,m,down,right

def manhattenTourist(n,m,down,right):
    s = {}
    s['0,0'] = 0
    
    
    for i in range(1,n+1):
        s[str(i)+',0'] = s[str(i-1)+',0'] + down[i-1][0]
    for j in range(1,m+1):
        s['0,'+str(j)] = s['0,'+str(j-1)] + right[0][j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            a = s[str(i-1)+','+str(j)] + down[i-1][j]
            b = s[str(i)+','+str(j-1)] + right[i][j-1]
            s[str(i)+','+str(j)] = np.max([a,b])

    return s[str(n)+','+str(m)]

def gomanhatten(inputstring):
    n,m,down,right = readmanhatten(inputstring)
    return manhattenTourist(n,m,down,right)
    
inputstring = """4 4
1 0 2 4 3
4 6 5 2 1
4 4 5 2 1
5 6 8 5 3
-
3 2 4 0
3 2 4 2
0 7 3 3
3 3 0 2
1 3 2 2"""

inputstring = """2 2
20 0 0
20 0 0
-
0 0
0 0
10 10"""

inputstring = """19 19
1 3 2 4 3 3 4 4 0 3 1 3 2 0 3 2 0 0 0 3
2 0 0 4 0 2 3 4 1 3 1 3 2 4 4 3 1 4 1 3
3 1 4 2 2 4 3 4 2 3 3 2 0 1 2 3 4 0 2 2
2 0 2 4 2 2 1 0 3 1 0 0 4 1 4 3 2 3 3 4
0 0 3 3 2 2 2 3 0 0 1 2 0 4 3 3 1 2 3 0
3 0 3 0 0 3 2 1 2 1 1 0 0 3 0 0 3 0 4 1
2 4 2 1 1 2 2 3 2 4 2 3 2 2 0 4 0 0 0 3
2 0 0 1 0 1 4 0 3 3 3 4 3 4 4 2 0 2 4 1
3 3 2 3 3 3 1 2 4 3 3 3 1 1 2 2 3 2 4 0
2 3 3 2 2 1 3 0 2 1 0 4 2 3 1 1 4 0 2 0
0 0 0 2 2 4 1 3 2 3 0 4 3 0 1 3 3 3 3 0
2 4 2 0 4 0 2 0 1 4 1 0 3 0 1 3 1 1 3 2
3 2 4 1 1 2 4 4 3 4 4 3 4 4 1 3 1 3 2 2
4 1 1 1 2 2 3 2 4 1 0 4 3 3 4 2 4 2 4 3
0 1 3 3 0 3 0 4 3 2 4 2 4 4 0 3 2 3 0 3
1 3 0 0 1 1 2 4 1 1 3 2 0 3 2 3 2 0 2 3
4 4 1 2 4 0 3 2 0 2 3 2 4 1 3 2 4 1 2 4
0 4 2 3 3 1 2 0 1 2 2 1 0 4 4 4 3 1 2 4
4 2 1 4 4 4 0 4 4 4 1 1 2 4 1 3 2 3 1 1
-
4 4 0 1 4 0 1 0 2 4 0 3 4 0 0 3 0 2 1
4 4 3 4 1 4 1 4 3 1 1 2 3 4 4 3 3 4 3
4 3 1 0 1 4 3 4 0 0 3 3 4 2 2 0 3 4 3
0 3 2 1 3 0 3 0 3 4 3 2 3 2 2 3 0 0 0
3 1 4 1 1 0 4 1 4 2 0 1 2 4 2 0 2 2 4
2 1 1 2 1 2 0 0 4 4 3 0 3 2 0 1 0 1 3
0 4 0 2 3 2 1 0 1 1 0 3 4 3 0 1 2 3 3
0 1 3 1 4 1 4 3 0 1 4 2 1 1 2 0 4 2 0
3 1 0 4 0 2 4 2 4 3 4 2 2 4 2 4 4 4 0
2 1 4 4 2 0 1 3 2 4 1 3 2 2 3 1 1 1 2
3 3 1 2 4 3 3 4 1 0 3 2 4 4 1 3 0 2 4
1 2 0 2 1 2 3 3 1 0 0 4 3 2 1 0 0 4 0
3 3 1 2 4 3 3 0 4 2 2 4 1 2 4 2 3 4 0
4 2 4 3 1 1 4 3 0 3 1 1 4 1 3 1 3 0 2
2 4 0 1 0 2 2 0 0 2 0 4 0 2 1 0 2 0 4
1 0 2 1 4 4 4 1 1 3 0 0 3 2 3 4 4 2 1
0 3 3 2 1 4 3 3 2 3 4 3 3 1 3 1 1 3 4
0 1 0 2 1 1 1 2 3 0 3 0 3 3 3 0 1 3 3
4 2 0 4 3 3 0 3 4 3 3 1 3 4 2 4 2 3 0
4 1 0 0 3 3 4 0 2 4 0 4 1 1 4 4 4 2 1"""

gomanhatten(inputstring)





