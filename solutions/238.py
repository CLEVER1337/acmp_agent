
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
        
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    start_x = xa - 1
    start_y = ya - 1
    dist[start_x][start_y] = 0
    q.append((start_x, start_y))
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while q:
        x, y = q.popleft()
        if (x, y) in exits:
            print(dist[x][y])
            return
            
        if (x, y) in tunnels:
            nx, ny = tunnels[(x, y)]
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
                
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
                
    print("Impossible")

if __name__ == "__main__":
    main()
