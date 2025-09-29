
MOD = 10**18

def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    N, C, K = map(int, data[0].split())
    s = data[1].strip()
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    max_len = len(str(C))
    
    for i in range(1, n + 1):
        total = 0
        for l in range(1, min(i, max_len) + 1):
            start = i - l
            if s[start] == '0' and l > 1:
                continue
                
            num_str = s[start:i]
            num = int(num_str)
            if num <= C:
                total = (total + dp[start]) % MOD
                
        dp[i] = total % MOD
    
    result = dp[n] % (10**K)
    print(str(result).zfill(K))

if __name__ == "__main__":
    main()
