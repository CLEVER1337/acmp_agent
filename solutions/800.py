
import sys

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
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    
    factors = factorize(n)
    primes = list(factors.keys())
    exponents = [factors[p] for p in primes]
    m = len(primes)
    
    dp = [0] * (k + 1)
    dp[0] = 1
    
    for exp in exponents:
        new_dp = [0] * (k + 1)
        for i in range(k + 1):
            if dp[i] == 0:
                continue
            for j in range(min(k - i, exp + 1)):
                new_dp[i + j] += dp[i]
        dp = new_dp
    
    print(dp[k])

if __name__ == "__main__":
    main()
