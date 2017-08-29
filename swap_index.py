def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def sort(a,b):
    for i in range(len(a)):
        swap(a, b[i], b[b[i]])
        swap(b, b[i], b[b[i]])

a = ["C","D","E","F","G"]
b = [3,0,4,1,2]
sort(a,b)

print(a)
print(b)