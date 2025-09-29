
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    grid = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        index += n
        grid.append(row)
    
    if k == 1:
        print(grid[0][0])
        return
        
    dp_prev = [[-10**9] * n for _ in range(n)]
    dp_prev[0][0] = grid[0][0]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for step in range(1, k):
        dp_curr = [[-10**9] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                best = -10**9
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        best = max(best, dp_prev[ni][nj])
                if best != -10**9:
                    dp_curr[i][j] = best + grid[i][j]
        dp_prev = dp_curr
    
    result = max(max(row) for row in dp_prev)
    print(result)

if __name__ == "__main__":
    main()
