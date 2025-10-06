
n = int(input().strip())

if n == 0:
    print(0)
else:
    dp = [0] * (n + 1)
    dp[1] = 0
    for i in range(2, n + 1):
        k = (i + 1) // 2
        dp[i] = dp[k] + dp[i - k] + 1
    print(dp[n])
