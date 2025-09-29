
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
    with open("INPUT.TXT", "r") as f:
        x = int(f.read().strip())
    
    if x <= 2 or x % 2 != 0:
        with open("OUTPUT.TXT", "w") as f:
            f.write("0")
        return
    
    count = 0
    primes = []
    for i in range(2, x):
        if is_prime(i):
            primes.append(i)
    
    seen = set()
    for prime in primes:
        complement = x - prime
        if complement >= prime and complement in primes:
            count += 1
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(count))

if __name__ == "__main__":
    main()
