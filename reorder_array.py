#https://www.careercup.com/question?id=5756151524229120

def sort(A, B):
    if len(A) != len(B):
        return False
    i = 0
    while i < len(A):
        if B[i] == i:
            i += 1
            continue
        A = swap(A, i, B[i])
        B = swap(B, i, B[i])
    return A, B

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return A

A = ["C", "D", "E", "F", "G"]
B = [4, 3, 1, 0, 2]
A, B = sort(A, B)
print(A)
print(B)

B = [3, 0, 4, 1, 2]
A, B = sort(A, B)
print(A)
print(B)