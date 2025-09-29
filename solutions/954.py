
MOD = 10**6

def main():
    k = int(input().strip())
    if k % 2 != 0:
        print(0)
        return
        
    n = k // 2
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        if i >= 2:
            dp[i] = (dp[i] + dp[i - 2]) % MOD
        if i >= 3:
            dp[i] = (dp[i] + dp[i - 3]) % MOD
            
    print(dp[n] % MOD)

if __name__ == "__main__":
    main()
