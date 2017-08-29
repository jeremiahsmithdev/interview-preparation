
def knapsack(weight, val, size, curr_val, index):
    if size == 0:
        return curr_val

    if size < 0 or index >= len(weight):
        return 0

    q = max(knapsack(weight, val, size, curr_val, index + 1), knapsack(weight, val, size - weight[index], curr_val + val[index], index + 1)) #max of picking it, or not

    return q

wt = [1,3,4,5]
val = [1,4,5,7]
size = 7
print(knapsack(wt,val,size, 0, 0))
