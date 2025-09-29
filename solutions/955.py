
from collections import deque

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    immune = set()
    index = 3
    for i in range(k):
        y = int(data[index]) - 1
        x = int(data[index + 1]) - 1
        immune.add((y, x))
        index += 2
        
    grid = [[0] * m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if (y, x) in immune:
                grid[y][x] = -1
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def bfs(start_y, start_x, visited):
        queue = deque([(start_y, start_x)])
        visited[start_y][start_x] = True
        while queue:
            y, x = queue.popleft()
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m:
                    if not visited[ny][nx] and grid[ny][nx] != -1:
                        visited[ny][nx] = True
                        queue.append((ny, nx))
    
    visited = [[False] * m for _ in range(n)]
    components = 0
    
    for y in range(n):
        for x in range(m):
            if grid[y][x] != -1 and not visited[y][x]:
                bfs(y, x, visited)
                components += 1
                
    print(components)

if __name__ == "__main__":
    main()
