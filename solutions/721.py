
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1+n):
        grid.append(list(data[i]))
    
    directions = ['R', 'L', 'U', 'D']
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    def get_neighbors(x, y):
        neighbors = []
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '.':
                neighbors.append((nx, ny, d))
        return neighbors
    
    def find_cycle_count(arrangement):
        visited = [[False] * m for _ in range(n)]
        cycles = 0
        
        def dfs(x, y):
            stack = [(x, y)]
            while stack:
                cx, cy = stack.pop()
                if visited[cx][cy]:
                    continue
                visited[cx][cy] = True
                d = directions.index(arrangement[cx][cy])
                nx, ny = cx + dx[d], cy + dy[d]
                if 0 <= nx < n and 0 <= ny < m and arrangement[nx][ny] != '.':
                    stack.append((nx, ny))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] != '.' and not visited[i][j]:
                    cycles += 1
                    dfs(i, j)
        return cycles
    
    min_grid = [row[:] for row in grid]
    max_grid = [row[:] for row in grid]
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '?':
                neighbors = get_neighbors(i, j)
                if neighbors:
                    _, _, d = neighbors[0]
                    min_grid[i][j] = directions[d]
                    max_grid[i][j] = directions[d]
    
    print('\n'.join(''.join(row) for row in min_grid))
    print()
    print('\n'.join(''.join(row) for row in max_grid))

if __name__ == '__main__':
    main()
