
def main():
    n = int(input().strip())
    
    factors = {}
    temp = n
    f = 2
    while f * f <= temp:
        if temp % f == 0:
            count = 0
            while temp % f == 0:
                count += 1
                temp //= f
            factors[f] = count
        f += 1
    if temp > 1:
        factors[temp] = 1
        
    if len(factors) != 2:
        print(0)
        return
        
    primes = list(factors.keys())
    if factors[primes[0]] != factors[primes[1]]:
        print(0)
        return
        
    k = factors[primes[0]]
    result = (2 * k - 1) * (2 * k - 1)
    print(result)

if __name__ == "__main__":
    main()
