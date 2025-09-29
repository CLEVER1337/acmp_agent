
from collections import deque

def main():
    with open('INPUT.TXT', 'r') as f:
        n, m = map(int, f.readline().split())
        data = list(map(int, f.readline().split()))
        k = data[0]
        viruses = []
        for i in range(k):
            y = data[2*i + 1] - 1
            x = data[2*i + 2] - 1
            viruses.append((y, x))
    
    if k == 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('0')
        return
    
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    
    for y, x in viruses:
        visited[y][x] = True
        queue.append((y, x, 0))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_time = 0
    
    while queue:
        y, x, time = queue.popleft()
        max_time = max(max_time, time)
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx, time + 1))
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(max_time))

if __name__ == '__main__':
    main()
