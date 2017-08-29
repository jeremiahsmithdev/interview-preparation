def mcnuggets(n):
    return _mcnuggets(n, [6, 9, 20], 0, {})

def _mcnuggets(n, options, index, memo):
    if n == 0:
        return True
    if index >= len(options):
        return False
    n_with_type = 0
    key = str(n) + "-" + str(index)
    if key in memo:
        print("found")
        return memo[key]
    while n_with_type <= n:
        remaining = n - n_with_type
        result = _mcnuggets(remaining, options, index + 1, memo)
        if result == True:
            return True
        n_with_type += options[index]
    memo[key] = result
    print("put")
    return False

n = 19
print(mcnuggets(n))