
MOD = 10**6

def main():
    k = int(input().strip())
    if k % 2 != 0:
        print(0)
        return
        
    n = k // 2
    if n == 0:
        print(1)
        return
        
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2
    
    for i in range(2, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
        
    print(dp[n])

if __name__ == "__main__":
    main()
