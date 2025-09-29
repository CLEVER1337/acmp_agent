
from collections import deque

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("Impossible")
        return
        
    idx = 0
    n = int(data[idx]); m = int(data[idx+1]); idx += 2
    xa = int(data[idx]); ya = int(data[idx+1]); idx += 2
    
    grid = []
    for i in range(n):
        row = list(map(int, data[idx:idx+m]))
        idx += m
        grid.append(row)
    
    h = int(data[idx]); idx += 1
    tunnels = {}
    for i in range(h):
        x1 = int(data[idx]); y1 = int(data[idx+1]); x2 = int(data[idx+2]); y2 = int(data[idx+3]); idx += 4
        tunnels[(x1-1, y1-1)] = (x2-1, y2-1)
    
    k = int(data[idx]); idx += 1
    exits = set()
    for i in range(k):
        x = int(data[idx]); y = int(data[idx+1]); idx += 2
        exits.add((x-1, y-1))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[-1] * m for _ in range(n)]
    queue = deque()
    
    start_x = xa - 1
    start_y = ya - 1
    visited[start_x][start_y] = 0
    queue.append((start_x, start_y))
    
    found = False
    result = -1
    
    while queue:
        x, y = queue.popleft()
        current_dist = visited[x][y]
        
        if (x, y) in exits:
            result = current_dist
            found = True
            break
            
        if (x, y) in tunnels:
            tx, ty = tunnels[(x, y)]
            if visited[tx][ty] == -1:
                visited[tx][ty] = current_dist + 1
                queue.append((tx, ty))
                
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = current_dist + 1
                    queue.append((nx, ny))
                    
    if found:
        print(result)
    else:
        print("Impossible")

if __name__ == "__main__":
    main()
