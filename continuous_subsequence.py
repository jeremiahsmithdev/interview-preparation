#https://www.careercup.com/question?id=6305076727513088

def continuous_subsequence(lst, target):
    start = 0
    end = 0
    sum = 0
    while start < len(lst) - 1:
        if sum == target:
            return True

        if end < len(lst):
            sum += lst[end]

        if sum > target:
            sum -= lst[start]
            start += 1

        end += 1
    return False

A = [23, 5, 4, 7, 2, 11]
tar = 20
print(continuous_subsequence(A, tar))

A = [1, 3, 5, 23, 2]
tar = 8
print(continuous_subsequence(A, tar))

A = [1, 3, 5, 23, 2]
tar = 7
print(continuous_subsequence(A, tar))