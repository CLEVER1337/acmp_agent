
def count_stairs(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n+1):
        for j in range(n, i-1, -1):
            dp[j] += dp[j-i]
    return dp[-1]-1  # вычитаем единицу для того, чтобы не учитывать случай, когда все кубики лежат на одном уровне.

n = int(input())
print(count_stairs(n))
