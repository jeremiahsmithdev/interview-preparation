def parity(x):
	res = 0
	while x:
		res = res ^ (x & 1)
		x = x >> 1
	return not res

n = 67
print(bin(n), parity(n))