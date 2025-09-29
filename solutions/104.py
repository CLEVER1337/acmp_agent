
def main():
    with open("INPUT.TXT", "r") as f:
        pattern = f.readline().strip()
        word = f.readline().strip()
    
    n = len(pattern)
    m = len(word)
    
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[i - 1] == word[j - 1] or pattern[i - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            else:
                dp[i][j] = False
    
    with open("OUTPUT.TXT", "w") as f:
        f.write("YES" if dp[n][m] else "NO")

if __name__ == "__main__":
    main()
