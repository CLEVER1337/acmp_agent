
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
                    if start is None:
                        start = (i, j)
                    else:
                        end = (i, j)
    
    if start is None or end is None:
        print("Impossible")
        return
    
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
             (1, -2), (1, 2), (2, -1), (2, 1)]
    
    prev = {}
    visited = set()
    queue = deque([start])
    visited.add(start)
    found = False
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            found = True
            break
            
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] != '#' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    prev[(nx, ny)] = (x, y)
                    queue.append((nx, ny))
    
    if not found:
        print("Impossible")
        return
    
    path = []
    current = end
    while current != start:
        path.append(current)
        current = prev[current]
    
    for x, y in path:
        if grid[x][y] != '@':
            grid[x][y] = '@'
    
    with open('OUTPUT.TXT', 'w') as f:
        for row in grid:
            f.write(''.join(row) + '\n')

if __name__ == "__main__":
    main()
