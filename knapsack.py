
def knapsack(weight, val, size):
    r = [[0 for i in range(size + 1)] for i in range(len(weight))]

    for i in range(len(weight)): #for each row
        for j in range(1,size + 1): #for each col, skipping first
            #can this item fit into the current bag?
            item = weight[i]
            if item <= j: #if selecting this item
                r[i][j] = max(val[i] + r[i - 1][j - weight[i]], r[i - 1][j])
            else:
                r[i][j] = r[i - 1][j] #else take above val

    return r

wt = [1,3,4,5]
val = [1,4,5,7]
size = 7
print(knapsack(wt,val,size))
