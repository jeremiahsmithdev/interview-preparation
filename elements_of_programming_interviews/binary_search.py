a = [2, 3, 4, 6, 7, 21, 65, 99, 101]

def binary_search(a, x):
    min = 0
    max = len(a)
    while min <= max:
        mid = int((min + max) / 2)
        if a[mid] == x:
            return True
        if a[mid] > x:
            max = mid - 1
        else:
            min = mid + 1

    return False

for element in a:
    print(binary_search(a, element))