
def main():
    with open('INPUT.TXT', 'r') as f:
        n, m = map(int, f.readline().split())
        grid = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            grid.append(row)
    
    visited = [[False] * m for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def dfs(i, j):
        stack = [(i, j)]
        visited[i][j] = True
        
        while stack:
            x, y = stack.pop()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and grid[nx][ny] == 0:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
    
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0 and not visited[i][j]:
                dfs(i, j)
                count += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(count))

if __name__ == '__main__':
    main()
