
def main():
    s = input().strip()
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][i] = 0
        if i < n:
            dp[i][i + 1] = 1
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length
            dp[i][j] = float('inf')
            if (s[i] == '(' and s[j - 1] == ')') or (s[i] == '[' and s[j - 1] == ']') or (s[i] == '{' and s[j - 1] == '}'):
                dp[i][j] = dp[i + 1][j - 1]
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    
    print(dp[0][n])

if __name__ == "__main__":
    main()
