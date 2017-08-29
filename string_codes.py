

def decode(a):
    dp = [0 for i in range(len(a)+1)]

    for i in range(1,len(a)+1):
        if i > 1 and int(a[i - 2]) <= 2 and int(a[i - 1]) <= 6:#if valid
            dp[i] = dp[i - 1] + dp[i - 2] + 1
        else:
            dp[i] = dp[i - 1]

    print(dp)
    return dp[len(a)] + 1

a = "1123"

print(decode(a))