#https://www.hackerrank.com/challenges/coin-change
#difference: we want to return the options
#!/bin/python3

import sys

sys.setrecursionlimit(100000)

import copy

def get_ways_recurse(coins, target, index, current, temp_sol, sol):
    #print(current)
    if current == target:
        sol.append(temp_sol.copy())
        #print(temp_sol)
        return
    if index > len(coins) - 1:
        return
    amount_with_coin = 0
    while amount_with_coin <= target:

        get_ways_recurse(coins, target, index + 1, current + amount_with_coin, temp_sol, sol)

        if len(temp_sol) > 0:
            temp_sol.pop()
        amount_with_coin += coins[index]
        temp_sol.append((coins[index], amount_with_coin))
    return sol

def get_ways(coins, money):
    return get_ways_recurse(coins, money, 0, 0, [], [])

#n, m = input().strip().split(' ')
#n, m = [int(n), int(m)]
#c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
n = 7
c = [2,3,6,7]

ways = get_ways(c, n)
for way in ways:
    print(way)