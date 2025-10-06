
def main():
    x = int(input().strip())
    if x < 4:
        print(0)
        return
        
    sieve = [True] * (x + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(x**0.5) + 1):
        if sieve[i]:
            sieve[i*i:x+1:i] = [False] * len(sieve[i*i:x+1:i])
            
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    count = 0
    left = 0
    right = len(primes) - 1
    
    while left <= right:
        s = primes[left] + primes[right]
        if s == x:
            count += 1
            left += 1
            right -= 1
        elif s < x:
            left += 1
        else:
            right -= 1
            
    print(count)

if __name__ == "__main__":
    main()
