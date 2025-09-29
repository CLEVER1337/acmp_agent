
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    grid = []
    for i in range(1, n+1):
        grid.append(list(map(int, list(data[i]))))
    
    if n == 0:
        print(0)
        return
        
    dp = [[0] * n for _ in range(n)]
    max_side = 0
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                if dp[i][j] > max_side:
                    max_side = dp[i][j]
    
    print(max_side * max_side)

if __name__ == "__main__":
    main()
