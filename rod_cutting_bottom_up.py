from math import inf

def bottom_up(n, prices):
    r = [0 for i in range(n + 1)]
    for i in range(1,n+1): #for each possible length
        q = float(-inf)
        for j in range(i): #for each valid cut
            q = max(q, prices[j] + r[i-j-1]) #take max profit
        r[i] = q
    print(r)
    return r[n]

print(bottom_up(4, [1,5,8,9]))