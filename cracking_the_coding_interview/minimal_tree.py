#ccti 4.2
#going to leverage binary search to generate this tree

def minimal_tree(a):
    low = 0
    high = len(a)
    mid = (low + high) / 2

    while low <= high:
        insert(a[mid])
        ...

a = [1,1,2,3,4,5,6,7]
minimal_tree(a)