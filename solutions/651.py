
import math

def sieve(n):
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.isqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def factorize(n, primes):
    factors = {}
    temp = n
    for p in primes:
        if p * p > temp:
            break
        while temp % p == 0:
            factors[p] = factors.get(p, 0) + 1
            temp //= p
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    return factors

def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    N = int(data[0])
    M = int(data[1])
    
    if N == M:
        print(0)
        return
        
    if M % N != 0:
        print(-1)
        return
        
    ratio = M // N
    
    if ratio == 1:
        print(0)
        return
        
    primes = sieve(int(math.isqrt(ratio)) + 100)
    factors = factorize(ratio, primes)
    
    for p in factors:
        if p not in [2, 3]:
            print(-1)
            return
            
    count_2 = factors.get(2, 0)
    count_3 = factors.get(3, 0)
    
    print(count_2 + count_3)

if __name__ == "__main__":
    solve()
