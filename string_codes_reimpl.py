
def decode(a):
    dp = [0 for i in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        if i > 1 and int(a[i - 2]) <= 2 and int(a[i - 1]) <= 6:
            dp[i] = dp[i - 2] + dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]

    return dp

a = "1126"
print(decode(a))