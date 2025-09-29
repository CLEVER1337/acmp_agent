
def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

with open('INPUT.TXT', 'r') as f:
    n = int(f.read().strip())
    
result = phi(n)

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
