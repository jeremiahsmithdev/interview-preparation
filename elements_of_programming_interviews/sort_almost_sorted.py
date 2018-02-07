from heapq import heappush, heappop

def sort(a, k):
    min_heap = []

    element = 0

    for i in range(k):
        heappush(min_heap, a[element])
        element += 1

    while element < len(a):
        heappush(min_heap, a[element])
        print(heappop(min_heap)) # smallest
        element += 1

    while len(min_heap):
        print(heappop(min_heap))  # smallest

a = [3, -1, 2, 6, 4, 5, 8]

sort(a, 2)