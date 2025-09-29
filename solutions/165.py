
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    grid = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        grid.append(row)
        index += m
        
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if dp[i][j] == 0:
                continue
            step = grid[i][j]
            if step == 0:
                continue
                
            if i + step < n:
                dp[i + step][j] += dp[i][j]
                
            if j + step < m:
                dp[i][j + step] += dp[i][j]
                
    print(dp[n-1][m-1])

if __name__ == "__main__":
    main()
