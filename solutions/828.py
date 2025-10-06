
n, k = map(int, input().split())
MOD = 10**9 + 7

if n == 0:
    print(0)
    exit(0)

dp = [[0] * (k + 1) for _ in range(n + 1)]
prefix = [0] * (n + 1)

for j in range(1, k + 1):
    dp[1][j] = 1

for i in range(2, n + 1):
    total = 0
    for j in range(1, k + 1):
        total = (total + dp[i - 1][j]) % MOD
    
    for j in range(1, k + 1):
        dp[i][j] = total
        
        start = 2 * j
        while start <= i:
            dp[i][j] = (dp[i][j] - dp[i - start][j] + MOD) % MOD
            start += j
        
        prefix[i] = (prefix[i] + dp[i][j]) % MOD

result = 0
for j in range(1, k + 1):
    result = (result + dp[n][j]) % MOD

print(result)
