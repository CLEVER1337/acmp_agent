
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    nk = data[0].split()
    n = int(nk[0])
    k = int(nk[1])
    
    grid = []
    for i in range(1, 1 + n):
        grid.append(data[i].strip())
    
    if grid[0][0] == '1' or grid[n-1][n-1] == '1':
        print(0)
        return
        
    dp_prev = [[0] * n for _ in range(n)]
    dp_prev[0][0] = 1
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for step in range(k):
        dp_next = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '1':
                    continue
                if dp_prev[i][j] == 0:
                    continue
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == '0':
                        dp_next[ni][nj] += dp_prev[i][j]
        dp_prev = dp_next
        
    print(dp_prev[n-1][n-1])

if __name__ == "__main__":
    main()
