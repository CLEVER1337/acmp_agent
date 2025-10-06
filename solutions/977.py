
def main():
    n = int(input().strip())
    if n == 2:
        print(1)
        return
        
    MOD = 123456789
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = 0
        for j in range(i):
            dp[i] = (dp[i] + dp[j] * dp[i - j - 1]) % MOD
            
    result = (dp[n] * n * (n - 1) // 2) % MOD
    print(result)

if __name__ == '__main__':
    main()
