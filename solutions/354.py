
def factorize(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

with open('INPUT.TXT', 'r') as f:
    n = int(f.read().strip())
    
factors = factorize(n)
result = '*'.join(map(str, factors))

with open('OUTPUT.TXT', 'w') as f:
    f.write(result)
