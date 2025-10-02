
def count_numbers(N, K):
    if K < 0:
        return 0
        
    s = bin(N)[2:]
    n = len(s)
    
    dp = [[[0] * (K + 2) for _ in range(2)] for __ in range(n + 1)]
    dp[0][0][0] = 1
    
    for i in range(n):
        for tight in range(2):
            for zeros in range(K + 1):
                if dp[i][tight][zeros] == 0:
                    continue
                    
                limit = int(s[i]) if tight else 1
                for d in range(limit + 1):
                    new_tight = tight and (d == limit)
                    new_zeros = zeros + (1 if d == 0 else 0)
                    if new_zeros <= K:
                        dp[i + 1][new_tight][new_zeros] += dp[i][tight][zeros]
    
    return dp[n][0][K] + dp[n][1][K] - (1 if K == 0 else 0)

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        N = int(data[0])
        K = int(data[1])
    
    result = count_numbers(N, K)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
