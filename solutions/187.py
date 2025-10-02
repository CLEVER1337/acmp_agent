
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    dp = [[0] * (2 * n) for _ in range(2 * n)]
    dp[0][0] = 1
    
    for i in range(2 * n):
        for j in range(2 * n):
            if dp[i][j] == 0:
                continue
            if i + 1 < 2 * n:
                dp[i + 1][j] += dp[i][j]
            if i + 1 < 2 * n and j + 1 < 2 * n:
                dp[i + 1][j + 1] += dp[i][j]
            if i - 1 >= 0 and j + 1 < 2 * n:
                dp[i - 1][j + 1] += dp[i][j]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(dp[0][2 * n - 2]))

if __name__ == '__main__':
    main()
