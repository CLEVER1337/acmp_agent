
def main():
    s = input().strip()
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 1
        
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j]
            if s[i - 1] == '(':
                dp[i][j] += dp[i - 1][j - 1]
            else:
                if j < n:
                    dp[i][j] += dp[i - 1][j + 1]
                    
    print(dp[n][0] - 1)
    
if __name__ == "__main__":
    main()
