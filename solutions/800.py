
import math

def factorize(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def main():
    n, k = map(int, input().split())
    factors = factorize(n)
    primes = list(factors.keys())
    exponents = list(factors.values())
    m = len(primes)
    
    dp = [[0] * (k + 1) for _ in range(m + 1)]
    dp[0][0] = 1
    
    for i in range(1, m + 1):
        exp = exponents[i - 1]
        for j in range(k + 1):
            dp[i][j] = dp[i - 1][j] * (exp + 1)
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1] * exp
    
    print(dp[m][k])

if __name__ == "__main__":
    main()
