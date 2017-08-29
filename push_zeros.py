#https://www.careercup.com/question?id=12986664
#consider this as half of a sort -- we are only concerned with copying elements ONE way

A = [1,2,0,4,0,0,8]

swap = 0

for i in range(len(A)):
    if A[i] != 0:
        A[swap] = A[i]
        print(A)
        swap += 1

for i in range(swap, len(A)):
    A[i] = 0

print(A)