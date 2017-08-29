
def remove_duplicates(a):
    id = 1
    for i in range(1,len(a)):
        if a[i] != a[i - 1]:
            a[id] = a[i]
            id += 1
    return id

a = [1,1,1,2]

print(remove_duplicates(a))

print(a)