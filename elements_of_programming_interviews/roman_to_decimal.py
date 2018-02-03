mappings = {}
mappings['I'] = 1
mappings['V'] = 5
mappings['X'] = 10
mappings['L'] = 50
mappings['C'] = 100
mappings['D'] = 500
mappings['M'] = 1000

a = 'LIX'

sum = mappings[a[-1]]

for i in reversed(range(len(a) - 1)):
    if mappings[a[i]] < mappings[a[i + 1]]:
        sum -= mappings[a[i]]
    else:
        sum += mappings[a[i]]

print(sum)