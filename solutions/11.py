def rabbit_ways(K, N):
    dp = [0] * (N+1)
    dp[0] = 1
    
    for i in range(1, N+1):
        for j in range(1, K+1):
            if j > i: break
            dp[i] += dp[i-j]
            
    return dp[-1]

K, N = map(int, input().split())
print(rabbit_ways(K, N))
