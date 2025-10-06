
from collections import deque

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    viruses = []
    index = 3
    for i in range(k):
        y = int(data[index]) - 1
        x = int(data[index + 1]) - 1
        viruses.append((y, x))
        index += 2
    
    grid = [[-1] * m for _ in range(n)]
    queue = deque()
    
    for y, x in viruses:
        grid[y][x] = 0
        queue.append((y, x))
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    max_time = 0
    
    while queue:
        y, x = queue.popleft()
        current_time = grid[y][x]
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == -1:
                grid[ny][nx] = current_time + 1
                max_time = max(max_time, current_time + 1)
                queue.append((ny, nx))
    
    print(max_time)

if __name__ == "__main__":
    main()
