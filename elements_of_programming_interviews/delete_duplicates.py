a = [2,3,5,5,7,11,11,11,13]

unique_start = 1
for i in range(1, len(a)):
	if a[i] != a[unique_start - 1]:
		a[unique_start] = a[i]
		unique_start += 1
	i += 1

print(a[:unique_start])