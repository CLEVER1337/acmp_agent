
from collections import deque

def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, m = map(int, data[0].split())
    grid = []
    tiger_pos = None
    for i in range(1, n + 1):
        line = data[i].strip()
        grid.append(line)
        if 'T' in line:
            tiger_pos = (i - 1, line.index('T'))
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def bfs(start):
        dist = [[-1] * m for _ in range(n)]
        q = deque()
        q.append(start)
        dist[start[0]][start[1]] = 0
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#' and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        return dist
    
    exit_pos = (n - 1, m - 1)
    slave_dist = bfs((0, 0))
    tiger_dist = bfs(tiger_pos)
    
    shortest_path = slave_dist[n - 1][m - 1]
    
    if shortest_path == -1:
        print(-1)
        print("No")
        return
    
    safe = True
    q = deque()
    visited = [[False] * m for _ in range(n)]
    q.append((0, 0))
    visited[0][0] = True
    
    while q:
        x, y = q.popleft()
        if (x, y) == exit_pos:
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#' and not visited[nx][ny]:
                if slave_dist[nx][ny] < tiger_dist[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif slave_dist[nx][ny] == tiger_dist[nx][ny] and (nx, ny) == exit_pos:
                    safe = False
    
    print(shortest_path)
    print("Yes" if safe else "No")

if __name__ == "__main__":
    main()
