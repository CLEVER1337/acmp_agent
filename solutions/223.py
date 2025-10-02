
def main():
    with open('INPUT.TXT', 'r') as f:
        src = f.readline().strip()
        dst = f.readline().strip()
    
    n = len(src)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[0][i] = 1
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[i][j] = dp[i][j - 1]
            if src[j - 1] == dst[i - 1]:
                dp[i][j] += dp[i - 1][j - 1]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(dp[n][n]))

if __name__ == '__main__':
    main()
