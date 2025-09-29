
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

def count_trailing_zeros(n, k):
    k_factors = factorize(k)
    result = float('inf')
    
    for prime, exp in k_factors.items():
        count = 0
        temp = n
        while temp:
            temp //= prime
            count += temp
        result = min(result, count // exp)
    
    return result

with open("INPUT.TXT", "r") as f:
    data = f.read().split()
    N = int(data[0])
    K = int(data[1])

result = count_trailing_zeros(N, K)

with open("OUTPUT.TXT", "w") as f:
    f.write(str(result))
