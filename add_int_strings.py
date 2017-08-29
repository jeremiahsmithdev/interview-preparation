def pad(a, b):
    diff = abs(len(a) - len(b))
    if diff == 0:
        return a, b
    pad = "0" * diff
    if len(a) < len(b):
        a = pad + a
    else:
        b = pad + b
    return a, b

def add(a, b):
    a, b = pad(a, b) #incase they are different lengths

    new_str = ""
    carry = 0
    #assume same length
    i = len(a) - 1
    while i >= 0:
        temp_sum = int(a[i]) + int(b[i]) + carry
        #check for carry
        carry = int(temp_sum / 10)
        temp_sum -= carry * 10
        new_str = str(temp_sum) + new_str
        i -= 1
    return new_str

a = "1163"
b = "456"

print(add(a, b))