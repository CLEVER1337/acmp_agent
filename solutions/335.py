
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
    
    primes = sieve(1000)
    prime_3digit = [False] * 1000
    for i in range(100, 1000):
        prime_3digit[i] = primes[i]
    
    dp = [[[0] * 100 for _ in range(100)] for __ in range(2)]
    
    for i in range(100, 1000):
        if prime_3digit[i]:
            a, b, c = i // 100, (i // 10) % 10, i % 10
            dp[0][b][c] = (dp[0][b][c] + 1) % MOD
    
    current = 0
    for length in range(4, n + 1):
        next_dp = [[0] * 100 for _ in range(100)]
        for b in range(10):
            for c in range(10):
                if dp[current][b][c] == 0:
                    continue
                for d in range(10):
                    num = b * 100 + c * 10 + d
                    if prime_3digit[num]:
                        next_dp[c][d] = (next_dp[c][d] + dp[current][b][c]) % MOD
        dp[current] = next_dp
        if length == n:
            break
    
    result = 0
    for i in range(100):
        for j in range(100):
            result = (result + dp[current][i][j]) % MOD
    
    print(result)

solve()
