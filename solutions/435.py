
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    
    total_sum = N * K
    max_sum = total_sum // 2
    
    dp = [0] * (max_sum + 1)
    dp[0] = 1
    
    for _ in range(N):
        new_dp = [0] * (max_sum + 1)
        for s in range(max_sum + 1):
            if dp[s] == 0:
                continue
            for d in range(K + 1):
                new_s = s + d
                if new_s <= max_sum:
                    new_dp[new_s] += dp[s]
        dp = new_dp
    
    total_numbers = (K + 1) ** N
    lucky_count = 0
    for s in range(max_sum + 1):
        if 2 * s == total_sum:
            lucky_count += dp[s] * dp[s]
        else:
            lucky_count += 2 * dp[s] * dp[s]
    
    unlucky_count = total_numbers - lucky_count
    print(unlucky_count)

if __name__ == "__main__":
    main()
