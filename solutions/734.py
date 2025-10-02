
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
        if i >= 2:
            dp[i] = (dp[i] + dp[i - 2] * K * (K - 1)) % MOD
    
    total_strings = dp[N]
    
    count_sets = 1
    for i in range(1, N + 1):
        count_sets = count_sets * (total_strings - dp[i - 1]) % MOD
    
    print(total_strings)
    print(count_sets)

if __name__ == "__main__":
    main()
