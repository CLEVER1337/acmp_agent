
from collections import deque

def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print("N")
        return
        
    n = int(data[0])
    grid = []
    start = None
    end = None
    
    for i in range(n):
        line = data[1 + i].strip()
        grid.append(list(line))
        for j in range(n):
            if grid[i][j] == '@':
                start = (i, j)
            elif grid[i][j] == 'X':
                end = (i, j)
    
    if start is None or end is None:
        print("N")
        return
        
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
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
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and grid[nx][ny] != 'O':
                    visited[nx][ny] = True
                    parent[nx][ny] = (x, y)
                    queue.append((nx, ny))
    
    if not found:
        print("N")
        return
        
    print("Y")
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent[current[0]][current[1]]
    path.append(start)
    path.reverse()
    
    for x, y in path:
        if grid[x][y] == '.' or grid[x][y] == 'X':
            grid[x][y] = '+'
    
    grid[start[0]][start[1]] = '@'
    grid[end[0]][end[1]] = 'X'
    
    for i in range(n):
        print(''.join(grid[i]))

if __name__ == "__main__":
    main()
