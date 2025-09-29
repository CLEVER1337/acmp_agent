
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    grid = []
    for i in range(1, n + 1):
        grid.append(list(map(int, list(data[i]))))
    
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = grid[0][0]
    
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    
    path = [['.'] * n for _ in range(n)]
    i, j = n - 1, n - 1
    path[i][j] = '#'
    
    while i > 0 or j > 0:
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            if dp[i - 1][j] < dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        path[i][j] = '#'
    
    for row in path:
        print(''.join(row))

if __name__ == "__main__":
    main()
