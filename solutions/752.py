
def main():
    import sys
    data = sys.stdin.read().split()
    L = int(data[0])
    R_val = int(data[1])
    
    dp = [0] * (L + 1)
    dp[1] = 1
    
    for n in range(2, L + 1):
        total = 0
        for i in range(1, n):
            j = n - i
            total = (total + dp[i] * dp[j]) % R_val
        
        for i in range(1, n):
            for j in range(1, n - i):
                k = n - i - j
                total = (total + dp[i] * dp[j] * dp[k]) % R_val
        
        dp[n] = total % R_val
    
    print(dp[L] % R_val)

if __name__ == "__main__":
    main()
