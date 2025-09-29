
import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    w, h = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + h):
        grid.append(data[i].strip())
    
    queries = []
    for i in range(1 + h, len(data)):
        parts = data[i].split()
        if len(parts) < 4:
            continue
        if parts[0] == '0':
            break
        x1, y1, x2, y2 = map(int, parts)
        queries.append((x1, y1, x2, y2))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for query in queries:
        x1, y1, x2, y2 = query
        if x1 == x2 and y1 == y2:
            print(0)
            continue
            
        start_x, start_y = x1 - 1, y1 - 1
        end_x, end_y = x2 - 1, y2 - 1
        
        if grid[start_y][start_x] != 'X' or grid[end_y][end_x] != 'X':
            print(0)
            continue
            
        rows, cols = h + 2, w + 2
        dist = [[-1] * cols for _ in range(rows)]
        
        queue = deque()
        dist[start_y + 1][start_x + 1] = 0
        queue.append((start_x + 1, start_y + 1))
        
        found = False
        while queue:
            x, y = queue.popleft()
            if x == end_x + 1 and y == end_y + 1:
                found = True
                break
                
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < cols and 0 <= ny < rows:
                    if dist[ny][nx] == -1:
                        if nx == 0 or nx == cols - 1 or ny == 0 or ny == rows - 1:
                            dist[ny][nx] = dist[y][x] + 1
                            queue.append((nx, ny))
                        else:
                            if grid[ny - 1][nx - 1] != 'X' or (nx - 1 == end_x and ny - 1 == end_y):
                                dist[ny][nx] = dist[y][x] + 1
                                queue.append((nx, ny))
        
        if found:
            print(dist[end_y + 1][end_x + 1])
        else:
            print(0)

if __name__ == "__main__":
    main()
