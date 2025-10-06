
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    
    if (K - N) % 2 != 0 or K < N:
        print(0)
        return
        
    steps_to_reach = (K - N) // 2
    total_steps = K
    
    dp = [[0] * (total_steps + 2) for _ in range(total_steps + 2)]
    dp[0][0] = 1
    
    for step in range(1, total_steps + 1):
        for pos in range(0, total_steps + 1):
            if pos > 0:
                dp[step][pos] += dp[step - 1][pos - 1]
            if pos + 1 <= total_steps:
                dp[step][pos] += dp[step - 1][pos + 1]
                
    print(dp[total_steps][N])

if __name__ == "__main__":
    main()
