
def main():
    with open('INPUT.TXT', 'r') as f:
        n, m = map(int, f.readline().split())
        grid = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
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
