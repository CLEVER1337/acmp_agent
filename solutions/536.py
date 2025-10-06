
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, C, K = map(int, data[0].split())
    s = data[1].strip()
    
    MOD = 10 ** K
    max_len = len(str(C))
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        total = 0
        j = i - 1
        num = 0
        base = 1
        max_j = max(0, i - max_len)
        
        for j in range(i - 1, max_j - 1, -1):
            digit = int(s[j])
            num += digit * base
            base *= 10
            
            if base > C:
                break
                
            if digit == 0 and j != i - 1:
                continue
                
            if num <= C:
                total = (total + dp[j]) % MOD
            else:
                break
                
        dp[i] = total % MOD
        
    print(str(dp[n] % MOD).zfill(K))

if __name__ == "__main__":
    main()
