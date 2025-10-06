
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    
    dp = [[0] * (n + 2) for _ in range(2 * n + 1)]
    dp[0][0] = 1
    
    for i in range(1, 2 * n + 1):
        for j in range(n + 1):
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]
            if j < n:
                dp[i][j] += dp[i - 1][j + 1]
                
    result = dp[2 * n][0]
    
    if k < n:
        dp2 = [[0] * (n + 2) for _ in range(2 * n + 1)]
        dp2[0][0] = 1
        
        for i in range(1, 2 * n + 1):
            for j in range(n + 1):
                if j > 0:
                    dp2[i][j] += dp2[i - 1][j - 1]
                if j < n and j < k:
                    dp2[i][j] += dp2[i - 1][j + 1]
                    
        result -= dp2[2 * n][0]
        
    print(result)

if __name__ == "__main__":
    main()
