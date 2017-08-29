MAXLEN = 15

m = [[0 for i in range(MAXLEN)] for i in range(MAXLEN)]

def match(a, b):
    return not a == b

def indel(a, i):
    #string = a[:i] + a[i + 1:]
    return 1

def row_init(i):
    m[0][i] = i

def col_init(i):
    m[i][0] = i

def string_compare(a, b):
    opt = [0,0,0]

    for i in range(MAXLEN):
        row_init(i)
        col_init(i)

    for i in range(1, len(a)):
        for j in range(1, len(b)):
            opt[0] = m[i-1][j-1] + match(a[i], b[j])
            opt[1] = m[i][j-1] + indel(b, j)
            opt[2] = m[i-1][j] + indel(a, i)

            m[i][j] = opt[0]

            for k in range(1,3):
                if opt[k] < m[i][j]:
                    m[i][j] = opt[k]

    print(m[i][j])
    return m

#print(m[0][0][0])

a = "you-should-not"
b = "thou-shalt-not"
for i in string_compare(a,b):
    for j in i:
        print(j,end="   ")
    print()