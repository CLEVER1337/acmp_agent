
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
    A = int(input().strip())
    if A == 1:
        print(1)
        return
        
    factors_A = factorize(A)
    result = 1
    
    for p, exp in factors_A.items():
        n = 0
        current_exp = 0
        while current_exp < exp:
            n += 1
            temp = n
            while temp % p == 0:
                current_exp += 1
                temp //= p
        result = max(result, n * p)
    
    print(result)

if __name__ == '__main__':
    main()
