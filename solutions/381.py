
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
                    grid[i][j] = '.'
                elif grid[i][j] == 'X':
                    end = (i, j)
                    grid[i][j] = '.'
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * n for _ in range(n)]
    parent = [[None] * n for _ in range(n)]
    
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    
    found = False
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            found = True
            break
            
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == '.':
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)
                queue.append((nx, ny))
    
    with open('OUTPUT.TXT', 'w') as f:
        if not found:
            f.write("No\n")
            return
        
        f.write("Yes\n")
        path = set()
        current = end
        while current != start:
            path.add(current)
            current = parent[current[0]][current[1]]
        
        for i in range(n):
            for j in range(n):
                if (i, j) == start:
                    f.write('@')
                elif (i, j) == end:
                    f.write('X')
                elif (i, j) in path:
                    f.write('+')
                elif grid[i][j] == 'O':
                    f.write('O')
                else:
                    f.write(grid[i][j])
            f.write('\n')

if __name__ == "__main__":
    main()
