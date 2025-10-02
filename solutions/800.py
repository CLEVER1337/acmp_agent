
import sys
import math
from functools import lru_cache

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

def get_divisors(factors):
    divisors = [1]
    for p, exp in factors.items():
        new_divisors = []
        for d in divisors:
            for i in range(exp + 1):
                new_divisors.append(d * (p ** i))
        divisors = new_divisors
    return sorted(divisors)

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    
    factors = factorize(n)
    divisors = get_divisors(factors)
    
    @lru_cache(maxsize=None)
    def count_normal_sets(start_idx, remaining_k, gcd_val):
        if remaining_k == 0:
            return 1
        
        total = 0
        for i in range(start_idx, len(divisors)):
            d = divisors[i]
            if d == 1:
                continue
                
            if gcd_val == 0:
                new_gcd = d
            else:
                new_gcd = math.gcd(gcd_val, d)
                
            if new_gcd == 1:
                total += count_normal_sets(i + 1, remaining_k - 1, new_gcd)
        
        return total
    
    result = count_normal_sets(0, k, 0)
    print(result)

if __name__ == "__main__":
    solve()
