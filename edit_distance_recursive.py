
def match(a, b):
    return not a == b #or can call lower etc

def indel(a, i):
    string = a[:i] + a[i + 1:]
    #print(string,a,i)
    return 1

def string_compare(a, b, i, j):
    k = 0
    lowest_cost = 1
    opt = [0 for i in range(3)]

   #print(i,j)

    if i == 0:
        return j
    if j == 0:
        return i

    opt[0] = string_compare(a, b, i-1,j-1) + match(a[i], b[j])
    opt[1] = string_compare(a, b, i,j-1) + indel(b, j)
    opt[2] = string_compare(a, b, i-1,j) + indel(a, i)

    lowest_cost = opt[0]
    for i in range(1,3):
        if opt[i] < lowest_cost:
            lowest_cost = opt[i]

    return lowest_cost

a = "hellooooooooo"
b = "helloooooooooo"
print(string_compare(a,b,len(a)-1,len(b)-1))

