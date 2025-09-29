
from collections import deque

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    grid = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        grid.append(row)
        index += m
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    result = [[-1] * m for _ in range(n)]
    queue = deque()
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                result[i][j] = 0
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and result[nx][ny] == -1:
                result[nx][ny] = result[x][y] + 1
                queue.append((nx, ny))
    
    for i in range(n):
        print(' '.join(map(str, result[i])))

if __name__ == "__main__":
    main()
