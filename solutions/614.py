
def main():
    with open("INPUT.TXT", "r") as f:
        s = f.readline().strip()
    
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j]
            if s[i - 1] == '(':
                if j > 0:
                    dp[i][j] += dp[i - 1][j - 1]
            else:
                if j < n:
                    dp[i][j] += dp[i - 1][j + 1]
    
    result = 0
    for j in range(n + 1):
        result += dp[n][j]
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
