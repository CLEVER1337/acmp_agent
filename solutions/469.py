
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    n = int(data[0])
    m = int(data[1])
    grid = []
    index = 2
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(data[index]))
            index += 1
        grid.append(row)
    
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = grid[0][0]
    
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(dp[n-1][m-1]))

if __name__ == "__main__":
    main()
