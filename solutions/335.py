
MOD = 10**9 + 9

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return is_prime

def solve():
    n = int(input())
    
    if n == 3:
        print(143)
        return
    
    primes = sieve(1000)
    prime_3digit = [i for i in range(100, 1000) if primes[i]]
    
    graph = {}
    for p in prime_3digit:
        prefix = p // 10
        suffix = p % 100
        if prefix not in graph:
            graph[prefix] = []
        graph[prefix].append(suffix)
    
    dp_prev = {}
    for p in prime_3digit:
        suffix = p % 100
        dp_prev[suffix] = dp_prev.get(suffix, 0) + 1
    
    for i in range(4, n + 1):
        dp_curr = {}
        for suffix, count in dp_prev.items():
            if suffix in graph:
                for next_suffix in graph[suffix]:
                    dp_curr[next_suffix] = (dp_curr.get(next_suffix, 0) + count) % MOD
        dp_prev = dp_curr
    
    result = sum(dp_prev.values()) % MOD
    print(result)

solve()
