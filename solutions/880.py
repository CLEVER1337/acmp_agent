
def main():
    import sys
    data = sys.stdin.read().splitlines()
    m, n = map(int, data[0].split())
    tile = []
    for i in range(1, 4):
        tile.append(data[i].strip())
    
    xs = []
    ys = []
    for i in range(3):
        for j in range(3):
            if tile[i][j] == 'X':
                xs.append(i)
                ys.append(j)
    
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    
    pattern = []
    for i in range(min_x, max_x + 1):
        row = []
        for j in range(min_y, max_y + 1):
            if tile[i][j] == 'X':
                row.append(1)
            else:
                row.append(0)
        pattern.append(row)
    
    def can_place(grid, x, y):
        for i in range(len(pattern)):
            for j in range(len(pattern[0])):
                if pattern[i][j]:
                    nx, ny = x + i, y + j
                    if nx < 0 or ny < 0 or nx >= m or ny >= n:
                        return False
                    if grid[nx][ny] >= 1:
                        return False
        return True
    
    def place_tile(grid, x, y, val):
        for i in range(len(pattern)):
            for j in range(len(pattern[0])):
                if pattern[i][j]:
                    nx, ny = x + i, y + j
                    grid[nx][ny] += val
    
    def dfs(grid, x, y, count, best):
        if count >= best[0]:
            return best[0]
        
        if x == m:
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 0:
                        return best[0]
            best[0] = min(best[0], count)
            return best[0]
        
        nx, ny = x, y + 1
        if ny == n:
            nx, ny = x + 1, 0
        
        if grid[x][y] >= 1:
            return dfs(grid, nx, ny, count, best)
        
        res = best[0]
        if can_place(grid, x, y):
            place_tile(grid, x, y, 1)
            res = min(res, dfs(grid, nx, ny, count + 1, best))
            place_tile(grid, x, y, -1)
        
        res = min(res, dfs(grid, nx, ny, count, best))
        return res
    
    grid = [[0] * n for _ in range(m)]
    best = [float('inf')]
    result = dfs(grid, 0, 0, 0, best)
    print(result)

if __name__ == '__main__':
    main()
