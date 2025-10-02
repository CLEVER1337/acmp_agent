
from collections import deque

def main():
    with open('INPUT.TXT', 'r') as f:
        n, m = map(int, f.readline().split())
        k_data = list(map(int, f.readline().split()))
        k = k_data[0]
        viruses = []
        for i in range(1, len(k_data), 2):
            viruses.append((k_data[i] - 1, k_data[i + 1] - 1))
    
    grid = [[-1] * m for _ in range(n)]
    queue = deque()
    
    for y, x in viruses:
        grid[y][x] = 0
        queue.append((y, x))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_time = 0
    
    while queue:
        y, x = queue.popleft()
        current_time = grid[y][x]
        max_time = max(max_time, current_time)
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == -1:
                grid[ny][nx] = current_time + 1
                queue.append((ny, nx))
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(max_time))

if __name__ == "__main__":
    main()
