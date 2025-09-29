
def main():
    with open('INPUT.TXT', 'r') as f:
        src = f.readline().strip()
        target = f.readline().strip()
    
    n = len(src)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(n - 1, -1, -1):
        for j in range(1, n - i + 1):
            if src[i] == target[n - j]:
                dp[i][j] = dp[i][j - 1] + dp[i + 1][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(dp[0][n]))

if __name__ == '__main__':
    main()
