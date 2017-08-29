a = [1, 2, 3]

for i in range(len(a)):
    if i == 1:
        del a[i]
        
    print(a[i])