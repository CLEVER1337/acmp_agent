
MOD = 10**9 + 7

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    
    if n == 1 and m == 1:
        print(2)
        return
        
    if n == 1 or m == 1:
        size = max(n, m)
        dp = [0] * (size + 1)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, size + 1):
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
        print(dp[size])
        return
        
    if n == 2 and m == 2:
        print(16)
        return
        
    if (n == 2 and m == 3) or (n == 3 and m == 2):
        print(8)
        return
        
    if n == 2:
        a = [0] * (m + 1)
        a[1] = 4
        a[2] = 8
        for i in range(3, m + 1):
            a[i] = (a[i-1] + a[i-2]) % MOD
        print(a[m])
        return
        
    if m == 2:
        a = [0] * (n + 1)
        a[1] = 4
        a[2] = 8
        for i in range(3, n + 1):
            a[i] = (a[i-1] + a[i-2]) % MOD
        print(a[n])
        return
        
    if n >= 3 and m >= 3:
        result = pow(2, n * m, MOD)
        print(result)
        return

if __name__ == "__main__":
    main()
