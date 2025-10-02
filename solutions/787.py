
n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
dp[-1] = a[-1]
for i in range(n-2, -1, -1):
    dp[i] = min(a[i], dp[i+1]) if (n - 1 - i) % 2 == 1 else max(a[i], dp[i+1])
print(dp[0])
