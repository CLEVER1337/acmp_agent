
def main():
    n = int(input().strip())
    if n == 2:
        print(1)
        return
        
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    def lcm(a, b):
        from math import gcd
        return a * b // gcd(a, b)

    def get_cycle_lengths(n):
        if n == 1:
            return [1]
            
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
                
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for p in primes:
            for j in range(n, p - 1, -1):
                power = p
                while power <= j:
                    dp[j] = lcm(dp[j], lcm(dp[j - power], power))
                    power *= p
                    
        return dp[n]

    result = get_cycle_lengths(n)
    print(result)

if __name__ == "__main__":
    main()
