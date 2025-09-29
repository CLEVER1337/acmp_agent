
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

def count_factor_in_factorial(n, p):
    count = 0
    power = p
    while power <= n:
        count += n // power
        power *= p
    return count

def find_max_k(n):
    if n == 1:
        return 0
    
    n_factors = factorize(n)
    max_k = float('inf')
    
    for p, exp in n_factors.items():
        count_in_factorial = count_factor_in_factorial(n, p)
        k_for_prime = count_in_factorial // exp
        max_k = min(max_k, k_for_prime)
    
    return max_k

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    result = find_max_k(n)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
