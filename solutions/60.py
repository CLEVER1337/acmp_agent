
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    k = int(input().strip())
    
    primes = []
    super_primes = []
    n = 2
    
    while len(super_primes) < k:
        if is_prime(n):
            primes.append(n)
            if len(primes) in primes:
                super_primes.append(n)
        n += 1
    
    print(super_primes[k-1])

if __name__ == "__main__":
    main()
