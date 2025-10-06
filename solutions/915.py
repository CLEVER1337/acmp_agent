
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    grid = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        index += m
        grid.append(row)
    
    if n == 0 or m == 0:
        print(0)
        return
        
    dp = [[-10**18] * m for _ in range(n)]
    dp[0][0] = grid[0][0] * 6
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
                
            from_top = -10**18
            from_left = -10**18
            
            if i > 0:
                from_top = dp[i-1][j] + grid[i][j] * (6 if i % 2 == 0 else 2)
            if j > 0:
                from_left = dp[i][j-1] + grid[i][j] * (6 if j % 2 == 0 else 2)
                
            dp[i][j] = max(from_top, from_left)
    
    print(dp[n-1][m-1])

if __name__ == "__main__":
    main()
