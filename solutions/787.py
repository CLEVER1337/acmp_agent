
n = int(input().strip())
a = list(map(int, input().split()))
dp = [0] * n
dp[-1] = a[-1]
for i in range(n-2, -1, -1):
    if i % 2 == (n-1) % 2:
        dp[i] = max(a[i], dp[i+1])
    else:
        dp[i] = min(a[i], dp[i+1])
print(dp[0])
