#ccti 1.2

def is_permutation(one, two):
    return False if len(one) != len(two) else sorted(one) == sorted(two)

a = "abc"
b = "cba"

print(is_permutation(a, b))