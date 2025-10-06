
def main():
    n = int(input().strip())
    size = 2 * n - 1
    dp = [[0] * size for _ in range(size)]
    
    dp[0][0] = 1
    
    for i in range(size):
        for j in range(size):
            if dp[i][j] == 0:
                continue
            if i + 1 < size:
                dp[i+1][j] += dp[i][j]
            if i + 1 < size and j + 1 < size:
                dp[i+1][j+1] += dp[i][j]
            if j + 1 < size:
                dp[i][j+1] += dp[i][j]
                
    print(dp[size-1][size-1])

if __name__ == '__main__':
    main()
