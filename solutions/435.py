
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
                ns = s + d
                if ns <= max_sum:
                    new_dp[ns] += dp[s]
        dp = new_dp

    total_numbers = (K + 1) ** N
    happy_count = 0
    for s in range(max_sum + 1):
        happy_count += dp[s] * dp[s]
    if total_sum % 2 == 0:
        happy_count -= dp[max_sum] * dp[max_sum]
        happy_count += dp[max_sum] * (dp[max_sum] + 1) // 2

    result = total_numbers - happy_count
    print(result)

if __name__ == "__main__":
    main()
