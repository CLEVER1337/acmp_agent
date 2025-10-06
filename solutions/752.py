
def main():
    import sys
    data = sys.stdin.read().split()
    L = int(data[0])
    R_mod = int(data[1])
    
    if L == 1:
        print(1 % R_mod)
        return
        
    dp = [0] * (L + 1)
    dp[1] = 1
    
    for n in range(2, L + 1):
        total = 0
        for k in range(1, n):
            if 2 * k <= n:
                total = (total + dp[k] * dp[n - 2 * k]) % R_mod
            if 3 * k <= n:
                total = (total + dp[k] * dp[n - 3 * k]) % R_mod
        dp[n] = total % R_mod
        
    print(dp[L] % R_mod)

if __name__ == "__main__":
    main()
