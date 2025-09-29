
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    size = 2 * n - 1
    dp = [[0] * size for _ in range(size)]
    
    dp[0][0] = 1
    
    for i in range(size):
        for j in range(size):
            if dp[i][j] > 0:
                if i + 1 < size:
                    dp[i + 1][j] += dp[i][j]
                if i + 1 < size and j + 1 < size:
                    dp[i + 1][j + 1] += dp[i][j]
                if i - 1 >= 0 and j + 1 < size:
                    dp[i - 1][j + 1] += dp[i][j]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(dp[0][size - 1]))

if __name__ == '__main__':
    main()
