
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    max_sum = N * K
    total_numbers = (K + 1) ** N
    
    dp = [0] * (max_sum + 1)
    dp[0] = 1
    
    for _ in range(N):
        new_dp = [0] * (max_sum + 1)
        for s in range(len(dp)):
            if dp[s] == 0:
                continue
            for d in range(K + 1):
                new_sum = s + d
                if new_sum <= max_sum:
                    new_dp[new_sum] += dp[s]
        dp = new_dp
    
    happy_count = 0
    for s in range(max_sum + 1):
        if s % 2 == 0:
            half = s // 2
            if half <= max_sum:
                happy_count += dp[half] * dp[half]
    
    result = total_numbers - happy_count
    print(result)

if __name__ == "__main__":
    main()
