#ccti 1.4

def is_permutation_of_palindrome(a):
    a = list(a.replace(' ', ''))
    a = sorted(a)
    a += " "
    #one letter can be odd, all others must be even
    print(a)
    temp = a[0]
    count = 1
    no_odd = 0
    for i in range(1, len(a)):
        if a[i] == temp:
            count += 1
        else:
            if count % 2 != 0:
                no_odd += 1
                if no_odd > 1:
                    return False
            temp = a[i]
            count = 1
    return True

a = "tact coat"
print(is_permutation_of_palindrome(a))