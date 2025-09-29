
from collections import deque

def main():
    import sys
    data = sys.stdin.read().splitlines()
    
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(data[i].strip())
    
    qx, qy, L = map(int, data[1 + n].split())
    qx -= 1
    qy -= 1
    
    musketeers = []
    for i in range(2 + n, 6 + n):
        parts = data[i].split()
        x = int(parts[0]) - 1
        y = int(parts[1]) - 1
        p = int(parts[2])
        musketeers.append((x, y, p))
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def bfs(start_x, start_y):
        if grid[start_x][start_y] == '1':
            return float('inf')
            
        visited = [[-1] * m for _ in range(n)]
        queue = deque()
        queue.append((start_x, start_y))
        visited[start_x][start_y] = 0
        
        while queue:
            x, y = queue.popleft()
            
            if x == qx and y == qy:
                return visited[x][y]
                
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == '0' and visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
        
        return float('inf')
    
    total_pendants = 0
    for x, y, p in musketeers:
        time = bfs(x, y)
        if time <= L:
            total_pendants += p
            
    print(total_pendants)

if __name__ == "__main__":
    main()
