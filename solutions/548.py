
def main():
    with open('INPUT.TXT', 'r') as f:
        a = f.readline().strip()
        b = f.readline().strip()
    
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp[i][j] = dp[i][j-1] * 10 + int(b[j-1])
            elif j == 0:
                dp[i][j] = dp[i-1][j] * 10 + int(a[i-1])
            else:
                option1 = dp[i-1][j] * 10 + int(a[i-1])
                option2 = dp[i][j-1] * 10 + int(b[j-1])
                dp[i][j] = min(option1, option2)
    
    result = str(dp[n][m])
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
