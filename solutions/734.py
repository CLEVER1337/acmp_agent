
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    
    MOD = 10**9 + 7
    
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        dp[i] = dp[i-1] * K % MOD
        
    total = sum(dp) % MOD
    
    ans_count = total
    ans_sets = 1
    
    for i in range(1, N + 1):
        if i * 2 <= N:
            continue
        cnt = dp[i]
        sets = pow(K, i, MOD)
        if cnt > ans_count:
            ans_count = cnt
            ans_sets = sets
        elif cnt == ans_count:
            ans_sets = (ans_sets + sets) % MOD
            
    print(ans_count)
    print(ans_sets % MOD)

if __name__ == "__main__":
    main()
