#ccti 8.1
#leverage coin change problem
#can memoize from here...

def jump(n, options, index):
    if index >= len(options) or n < 0:
        return 0
    if n == 0:
        return 1
    height_with_option = 0
    ways = 0
    while height_with_option <= n:
        remaining = n - height_with_option
        ways += jump(remaining, options, index + 1)
        height_with_option += options[index]
    return ways

options = [1, 2, 3]
n = 10
print(jump(n, options, 0))