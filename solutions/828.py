
MOD = 10**9 + 7

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    
    dp = [[0] * (k + 2) for _ in range(n + 2)]
    prefix = [[0] * (k + 2) for _ in range(n + 2)]
    
    for j in range(1, k + 1):
        dp[1][j] = 1
        prefix[1][j] = j
    
    for i in range(2, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = prefix[i - 1][j]
            if i >= 3:
                dp[i][j] = (dp[i][j] + prefix[i - 2][j - 1]) % MOD
            prefix[i][j] = (prefix[i][j - 1] + dp[i][j]) % MOD
    
    result = prefix[n][k]
    print(result)

if __name__ == "__main__":
    main()
