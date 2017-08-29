
def is_sequence(a, n):
    start = 0
    end = 0
    temp_sum = a[0]

    while start < len(a):
        if temp_sum < n and end < len(a) - 1:
            end += 1
            temp_sum += a[end]

        if temp_sum > n:
            temp_sum -= a[start]
            start += 1

        if temp_sum == n:
            print(temp_sum)
            return True

    return False

a = [1,3,5,23,2]
n = 28 #problem when n is 26 and pointers are sitting next to each other -- nothing is happening
print(is_sequence(a, n))