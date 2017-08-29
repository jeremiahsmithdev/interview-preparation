#ccti 1.1

def is_unique(string):
    return len(set(string)) == len(string)

def is_unique_no_ds(string):
    string_sorted = sorted(string)
    ch = -1
    for i in range(len(string_sorted)):
        if string_sorted[i] == ch:
            return False
        ch = string_sorted[i]
    return True

a = "abc"
b = "abca"

print(is_unique_no_ds(a))
print(is_unique_no_ds(b))