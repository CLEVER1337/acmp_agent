
MOD = 10**9 + 7

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    prefix = [[0] * (k + 1) for _ in range(n + 1)]
    
    for j in range(1, k + 1):
        dp[1][j] = 1
        prefix[1][j] = j
    
    for i in range(2, n + 1):
        for j in range(1, k + 1):
            divisors = []
            for d in range(1, int(j**0.5) + 1):
                if j % d == 0:
                    divisors.append(d)
                    if d != j // d:
                        divisors.append(j // d)
            
            total = prefix[i - 1][k]
            for d in divisors:
                if d != j:
                    total = (total - dp[i - 1][d] + MOD) % MOD
            dp[i][j] = total
            prefix[i][j] = (prefix[i][j - 1] + total) % MOD
    
    result = prefix[n][k]
    print(result)

if __name__ == "__main__":
    main()
