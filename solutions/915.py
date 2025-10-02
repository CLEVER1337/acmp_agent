
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    grid = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        index += m
        grid.append(row)
    
    if n * m == 0:
        print(0)
        return
        
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 6 * grid[0][0]
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
                
            candidates = []
            if i >= 1:
                candidates.append(dp[i-1][j] + 6 * grid[i][j])
                candidates.append(dp[i-1][j] + 2 * grid[i][j])
            if j >= 1:
                candidates.append(dp[i][j-1] + 6 * grid[i][j])
                candidates.append(dp[i][j-1] + 2 * grid[i][j])
            
            if candidates:
                dp[i][j] = max(candidates)
            else:
                dp[i][j] = -10**18
                
    print(dp[n-1][m-1])

if __name__ == "__main__":
    main()
