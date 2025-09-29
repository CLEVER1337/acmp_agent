
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

def get_divisors_count(factors):
    count = 1
    for exp in factors.values():
        count *= (exp + 1)
    return count

def solve():
    with open('INPUT.TXT', 'r') as f:
        D = int(f.read().strip())
    
    if D == 1:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('1')
        return
    
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    max_primes = len(primes)
    
    def backtrack(idx, current_num, divisors_left, last_exp):
        if divisors_left == 1:
            return current_num
        
        if idx >= max_primes:
            return float('inf')
        
        best = float('inf')
        p = primes[idx]
        
        for exp in range(1, last_exp + 1):
            if divisors_left % (exp + 1) != 0:
                continue
                
            next_num = current_num * (p ** exp)
            if next_num > 10**15 + 1:
                break
                
            next_divisors = divisors_left // (exp + 1)
            candidate = backtrack(idx + 1, next_num, next_divisors, exp)
            if candidate < best:
                best = candidate
        
        candidate = backtrack(idx + 1, current_num, divisors_left, last_exp)
        if candidate < best:
            best = candidate
            
        return best
    
    result = backtrack(0, 1, D, 100)
    
    if result > 10**15 + 1:
        result = 0
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

solve()
