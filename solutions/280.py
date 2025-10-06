
def main():
    x = int(input().strip())
    if x == 1:
        print(1)
        return
        
    factors = {}
    temp = x
    p = 2
    while p * p <= temp:
        while temp % p == 0:
            factors[p] = factors.get(p, 0) + 1
            temp //= p
        p += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
        
    primes = list(factors.keys())
    count = 1
    for p in primes:
        count *= (factors[p] + 1)
        
    print(count)

if __name__ == '__main__':
    main()
