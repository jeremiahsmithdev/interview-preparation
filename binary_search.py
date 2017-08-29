def binary_search_recursive(lst, key, low, high):
    mid = int((low + high) / 2)
    if mid < low or mid > high: #?
        return False
    if lst[mid] == key:
        return mid
    if key < lst[mid]:
        return binary_search_recursive(lst, key, low, mid)
    else:
        return binary_search_recursive(lst, key, mid, high)

def binary_search_iterative(lst, key):
    low = 0
    high = len(lst)
    while True:
        mid = int((low + high) / 2)
        if mid < low or mid > high:
            break
        if lst[mid] == key:
            return mid
        if key < lst[mid]:
            high = mid
        else:
            low = mid
    return False


lst = [2, 3, 4, 5, 8, 11, 13, 15, 16]

#print(binary_search_recursive(lst, 4, 0, len(lst)))

print(binary_search_iterative(lst, 16))