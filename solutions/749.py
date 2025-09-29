
def main():
    n = int(input().strip())
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    
    if len(factors) != 2:
        exit()
    
    k = list(factors.values())[0]
    if k != list(factors.values())[1]:
        exit()
    
    total_factors = 2 * k
    result = (1 << total_factors) - total_factors - 1
    print(result)

if __name__ == "__main__":
    main()
