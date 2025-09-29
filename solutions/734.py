
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    
    MOD = 10**9 + 7
    
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] * K % MOD
    
    total = 0
    for i in range(1, N + 1):
        total = (total + dp[i]) % MOD
    
    count = dp[N]
    
    print(total)
    print(count)

if __name__ == "__main__":
    main()
