#from introduction to algorithms, chapter 15

#exceeding c stack size -- use another language!

import sys
from math import inf

sys.setrecursionlimit(40000)

def cut_rod(prices, length_of_rod):
    if length_of_rod == 0:
        return 0

    q = -inf

    for i in range(length_of_rod):
        q = max(q, prices[i] + cut_rod(prices, length_of_rod - i))

    return q

prices = [1, 5, 8, 9, 10, 17, 20, 24, 30]

print(cut_rod(prices, 15))