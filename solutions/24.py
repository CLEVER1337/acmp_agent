
def count_ways(n, m):
    if n < m or (n - m) % 2 != 0:
        return 0
    
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[0][0] = 1
    
    for i in range(1, n+1):
        for j in range(min(i//2+1, m+1)):
            if j == 0 or j == i:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]*2
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]*3 - dp[i-2][j-2]
    
    return dp[n][m] % (10**9+7)

with open('INPUT.TXT', 'r') as f:
    n, m = map(int, f.readline().split())

result = count_ways(n, m)

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
