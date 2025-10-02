
from collections import deque

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("Impossible")
        return
        
    index = 0
    n = int(data[index]); m = int(data[index+1]); index += 2
    xa = int(data[index]); ya = int(data[index+1]); index += 2
    
    grid = []
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        index += m
        grid.append(row)
        
    h = int(data[index]); index += 1
    tunnels = {}
    for i in range(h):
        x1 = int(data[index]); y1 = int(data[index+1]); x2 = int(data[index+2]); y2 = int(data[index+3]); index += 4
        tunnels[(x1-1, y1-1)] = (x2-1, y2-1)
        
    k = int(data[index]); index += 1
    exits = set()
    for i in range(k):
        x = int(data[index]); y = int(data[index+1]); index += 2
        exits.add((x-1, y-1))
        
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    visited = [[-1] * m for _ in range(n)]
    queue = deque()
    start_x, start_y = xa-1, ya-1
    visited[start_x][start_y] = 0
    queue.append((start_x, start_y))
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) in exits:
            print(visited[x][y])
            return
            
        if (x, y) in tunnels:
            nx, ny = tunnels[(x, y)]
            if visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y]:
                visited[nx][ny] = visited[x][y]
                queue.appendleft((nx, ny))
                
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                    
    print("Impossible")

if __name__ == "__main__":
    main()
