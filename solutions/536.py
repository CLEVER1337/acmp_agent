
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, C, k = map(int, data[0].split())
    s = data[1].strip()
    
    MOD = 10**k
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        total = 0
        j = i - 1
        num = 0
        base = 1
        
        while j >= 0:
            digit = int(s[j])
            num += digit * base
            if base > C:
                break
            if digit == 0 and j != i - 1:
                j -= 1
                base *= 10
                continue
                
            if num > C:
                break
                
            total = (total + dp[j]) % MOD
            j -= 1
            base *= 10
            
        dp[i] = total % MOD
        
    print(str(dp[n] % MOD).zfill(k))

if __name__ == "__main__":
    main()
