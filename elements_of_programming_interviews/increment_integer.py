a = [9, 9, 9]

i = len(a) - 1
a[i] += 1

while i > 0 and a[i] == 10:
	a[i] = 0
	a[i - 1] += 1
	i -= 1

if a[0] == 10:
	a[0] = 0
	a.insert(0, 1)

print(a)