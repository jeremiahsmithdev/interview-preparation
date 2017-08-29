# from random import randrange, randint, random, uniform
#
# x = randrange(10.,50.)
#
# y = randint(1,5)
#
# z = uniform(10.,50.)
#
# print(x)
#
# print(y)
#
# print(z)


def parity(a):
    count = 0
    while a > 0:
        one = a & 1
        count += one
        a = a >> 1
    return count

a = 15
print(parity(a))

b = 1
print(bin(b << 5))

c = -1
print(bin(c >> 2))