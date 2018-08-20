def count_bits(x):
	n_bits = 0
	while x:
		n_bits += x & 1
		x = x >> 1
	return n_bits

n = 76
print(bin(n), count_bits(n))