
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

def solve():
    with open('INPUT.TXT', 'r') as f:
        A = int(f.read().strip())
    
    if A == 1:
        result = 1
    else:
        factors_A = factorize(A)
        result = 1
        
        for p, exp in factors_A.items():
            n_candidate = 0
            temp_exp = 0
            while temp_exp < exp:
                n_candidate += 1
                temp_exp += n_candidate
                count = n_candidate
                temp = n_candidate
                while temp % p == 0:
                    temp_exp += count
                    temp //= p
            
            result = max(result, n_candidate * p)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

solve()
