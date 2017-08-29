def move_zeros(a):
    zero_ptr = -1
    i = 0
    while i < len(a):
        if a[i] == 0:
            if zero_ptr < 0:
                zero_ptr = i
        elif zero_ptr > 0:
            a[zero_ptr] = a[i]
            a[i] = 0
            zero_ptr = i
        print(a, zero_ptr)
        i += 1

# a = [1,2,0,4,0,0]
#
# move_zeros(a)
#
# print(a)

a = [1,0,0,4,0,5]

move_zeros(a)

print(a)