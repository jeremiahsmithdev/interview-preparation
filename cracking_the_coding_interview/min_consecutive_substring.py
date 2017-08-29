#https://www.careercup.com/question?id=4855286160424960
from math import inf

def contains(string, chars):
    for ch in chars:
        if ch not in string:
            return False
    return True

def min_consecutive_substring(string, chars):
    n = len(chars)
    i = 0
    j = n
    min = float(inf)
    best_substring = ""
    while j <= len(string):
        substring = string[i:j]
        if not contains(substring, chars):
            j += 1
        else:
            if len(substring) < min:
                min = len(substring)
                best_substring = substring
            i += 1
    return min, best_substring

a = "adobecodebanc"
b = "abc"
print(min_consecutive_substring(a, b))