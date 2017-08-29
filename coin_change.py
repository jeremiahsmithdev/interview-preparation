#https://www.hackerrank.com/challenges/coin-change

#!/bin/python3

import sys

def get_ways_recurse(coins, money, index, memo):
    if money == 0:
        return 1
    if index >= len(coins):
        return 0
    key = str(money) + "-" + str(index)
    #if key in memo:
    #    return memo[key]
    amount_with_coin = 0
    ways = 0
    while amount_with_coin <= money:
        remaining = money - amount_with_coin
        ways += get_ways_recurse(coins, remaining, index + 1, memo)
        amount_with_coin += coins[index]
    memo[key] = ways
    return ways

def get_ways(coins, money):
    return get_ways_recurse(coins, money, 0, {})

n = 7
c = [2, 3, 6, 7]

ways = get_ways(c, n)
print(ways)

# n, m = input().strip().split(' ')
# n, m = [int(n), int(m)]
# c = list(map(int, input().strip().split(' ')))
# # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
# ways = get_ways(c, n)
# print(ways)