
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def s(n):
    return sum(int(d) for d in str(n))

def pck(n):
    if is_prime(n):
        return n
    if n < 10:
        return 0
    return pck(s(n))

with open('INPUT.TXT', 'r') as f:
    n = int(f.read().strip())
    
result = pck(n)

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
