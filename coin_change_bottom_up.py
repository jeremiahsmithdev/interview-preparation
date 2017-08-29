from math import inf

def get_ways(n, c):
    r = [[0 for i in range(len(c))] for i in range(n+1)]

    for i in range(len(c)):
        r[0][i] = 1

    for i in range(1,n+1): #for each length in n
        for j in range(len(c)): #for each cost value
            x = r[i - c[j]][j] if i - c[j] >= 0 else 0 #not 0 if that coin fits into i

            y = r[i][j-1] if j >= 1 else 0

            r[i][j] = x + y

    return r[n][len(c)-1], r

n = 7
c = [2, 3, 6, 7]
res, r = get_ways(n, c)

for row in r:
    print(row)