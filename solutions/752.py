
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
        for i in range(1, n):
            j = n - 1 - 2 * i
            if j < 0:
                break
            total = (total + dp[i] * dp[j]) % R_mod
            
        for i in range(1, n):
            j = n - 1 - i
            if j < i:
                break
            if i != j:
                total = (total + dp[i] * dp[j]) % R_mod
            else:
                total = (total + dp[i] * (dp[i] + 1) // 2) % R_mod
                
        dp[n] = total % R_mod
        
    print(dp[L] % R_mod)

if __name__ == "__main__":
    main()
