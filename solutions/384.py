
MOD = 10**9

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def fib_gcd(i, j):
    return fib(gcd(i, j)) % MOD

def fib(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % MOD
    return b

with open('INPUT.TXT', 'r') as f:
    i, j = map(int, f.read().split())

result = fib_gcd(i, j)

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
