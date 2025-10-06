
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    A = int(data[1])
    
    dp = [0] * (N + 1)
    dp[0] = 1
    
    for i in range(1, A + 1):
        for j in range(i, N + 1):
            dp[j] += dp[j - i]
            
    print(dp[N])

if __name__ == "__main__":
    main()
