
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
        with open('OUTPUT.TXT', 'w') as f:
            f.write('1')
        return
    
    factors_A = factorize(A)
    
    result = 1
    for p, exp in factors_A.items():
        n_candidate = p
        count = 0
        while count < exp:
            temp = n_candidate
            while temp % p == 0:
                count += 1
                temp //= p
                if count >= exp:
                    break
            if count < exp:
                n_candidate += p
        
        result = max(result, n_candidate)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

solve()
