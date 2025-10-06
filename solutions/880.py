
def main():
    m, n = map(int, input().split())
    pattern = []
    for _ in range(3):
        pattern.append(input().strip())
    
    grid = [[0]*9 for _ in range(9)]
    best = float('inf')
    
    coords = []
    for i in range(3):
        for j in range(3):
            if pattern[i][j] == 'X':
                coords.append((i, j))
    
    def dfs(x, y, count):
        nonlocal best
        if count >= best:
            return
        if x == m:
            best = min(best, count)
            return
        if y == n:
            dfs(x+1, 0, count)
            return
        if grid[x][y] > 0:
            dfs(x, y+1, count)
            return
        
        for dx, dy in coords:
            nx, ny = x - dx, y - dy
            if nx < 0 or ny < 0:
                continue
            valid = True
            for i, j in coords:
                cx, cy = nx + i, ny + j
                if cx >= m or cy >= n:
                    valid = False
                    break
                grid[cx][cy] += 1
                if grid[cx][cy] > 1:
                    valid = False
            
            if valid:
                dfs(x, y+1, count+1)
            
            for i, j in coords:
                cx, cy = nx + i, ny + j
                if cx < m and cy < n:
                    grid[cx][cy] -= 1
    
    dfs(0, 0, 0)
    print(best)

if __name__ == "__main__":
    main()
