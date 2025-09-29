
def main():
    n = int(input().strip())
    if n == 1:
        print(1)
        return
        
    MOD = 10**9 + 7
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1]
        for j in range(1, i):
            dp[i] = (dp[i] + dp[j] * dp[i - j - 1]) % MOD
    
    print(dp[n] % MOD)

if __name__ == "__main__":
    main()
