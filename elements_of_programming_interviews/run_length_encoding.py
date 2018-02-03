a = "aaaabcca"
result = ""

temp_count = 1

for i in range(1, len(a) + 1):
    if i == len(a) or a[i] != a[i - 1]:
        result += str(temp_count) + a[i - 1]
        temp_count = 1
    else:
        temp_count += 1

print(result)