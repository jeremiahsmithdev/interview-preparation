#ccti 1.3

def urlify(a, length):
    a = list(a)
    n_spaces = 0
    for i in range(length):
        if a[i] == ' ':
            n_spaces += 1
    #iterate backwards through string, copying everything n_spaces * 2 forward
    shift = n_spaces * 2
    #this is awkward: simply change the upper and lower bounds of the loop
    for i in reversed(range(0, length)):
        if a[i] != ' ':
            a[i + shift] = a[i]
        else:
            shift = shift - 2
            a[i + shift] = "%"
            a[i + shift + 1] = "2"
            a[i + shift + 2] = "0"
    return str(a)

a = "Mr John Smith Test"
len_a = len(a)
a += " " * 2 * sum(1 if x == " " else 0 for x in a) #add space to end of string
print(urlify(a, len_a))