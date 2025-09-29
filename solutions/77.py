
def count_numbers_with_k_zeros(N, K):
    if K < 0:
        return 0
        
    def count_up_to(n, k):
        if k < 0:
            return 0
            
        s = bin(n)[2:]
        length = len(s)
        
        if k > length - 1:
            return 0
            
        dp = [[[0] * (k + 1) for _ in range(2)] for __ in range(length + 1)]
        dp[0][1][0] = 1
        
        for i in range(length):
            for tight in range(2):
                for zeros in range(k + 1):
                    if dp[i][tight][zeros] == 0:
                        continue
                    limit = int(s[i]) if tight else 1
                    for d in range(limit + 1):
                        new_tight = 1 if (tight and d == limit) else 0
                        new_zeros = zeros
                        if d == 0 and i > 0:
                            new_zeros += 1
                        if new_zeros <= k:
                            dp[i + 1][new_tight][new_zeros] += dp[i][tight][zeros]
        
        return dp[length][0][k] + dp[length][1][k]
    
    return count_up_to(N, K)

def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    result = count_numbers_with_k_zeros(N, K)
    print(result)

if __name__ == "__main__":
    main()
