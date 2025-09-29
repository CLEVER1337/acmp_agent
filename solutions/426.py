
from collections import deque

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        grid = []
        start = None
        end = None
        
        for i in range(n):
            line = f.readline().strip()
            grid.append(list(line))
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j] == 'X':
                    end = (i, j)
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * n for _ in range(n)]
    parent = [[None] * n for _ in range(n)]
    
    queue = deque([start])
    visited[start[0]][start[1]] = True
    
    found = False
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == end:
            found = True
            break
            
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if grid[nx][ny] == '.' or grid[nx][ny] == 'X':
                    visited[nx][ny] = True
                    parent[nx][ny] = (x, y)
                    queue.append((nx, ny))
    
    with open('OUTPUT.TXT', 'w') as f:
        if not found:
            f.write('N\n')
        else:
            f.write('Y\n')
            
            path = []
            current = end
            while current != start:
                path.append(current)
                current = parent[current[0]][current[1]]
            
            for x, y in path:
                if grid[x][y] == '.' or grid[x][y] == 'X':
                    grid[x][y] = '+'
            
            if grid[start[0]][start[1]] == '@':
                grid[start[0]][start[1]] = '+'
            
            for row in grid:
                f.write(''.join(row) + '\n')

if __name__ == '__main__':
    main()
