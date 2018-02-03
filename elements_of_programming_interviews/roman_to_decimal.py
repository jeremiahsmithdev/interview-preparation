mappings = {}
mappings['I'] = 1
mappings['V'] = 5
mappings['X'] = 10
mappings['L'] = 50
mappings['C'] = 100
mappings['D'] = 500
mappings['M'] = 1000

a = 'LVIII'

sum = 0

for i in range(0, len(a) - 2):
    sum += mappings[a[i]]

print(sum)