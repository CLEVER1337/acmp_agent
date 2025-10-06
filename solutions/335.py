
MOD = 10**9 + 9

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return is_prime

def main():
    n = int(input().strip())
    if n == 3:
        print(143)
        return
        
    primes = sieve(1000)
    prime_set = set()
    for num in range(100, 1000):
        if primes[num]:
            prime_set.add(str(num))
            
    graph = {}
    for p in prime_set:
        suffix = p[1:]
        graph.setdefault(suffix, []).append(p)
        
    dp_prev = {}
    for p in prime_set:
        suffix = p[1:]
        dp_prev[suffix] = dp_prev.get(suffix, 0) + 1
        
    for i in range(4, n + 1):
        dp_curr = {}
        for suffix, count in dp_prev.items():
            for next_digit in '0123456789':
                candidate = suffix + next_digit
                if candidate in prime_set:
                    new_suffix = candidate[1:]
                    dp_curr[new_suffix] = (dp_curr.get(new_suffix, 0) + count) % MOD
        dp_prev = dp_curr
        
    total = sum(dp_prev.values()) % MOD
    print(total)

if __name__ == '__main__':
    main()
