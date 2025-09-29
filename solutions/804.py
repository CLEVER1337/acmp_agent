
from collections import deque

def main():
    import sys
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    grid = []
    tiger_pos = None
    
    for i in range(1, n + 1):
        row = data[i].strip()
        grid.append(row)
        if 'T' in row:
            tiger_pos = (i - 1, row.index('T'))
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def bfs(start):
        dist = [[-1] * m for _ in range(n)]
        q = deque([start])
        dist[start[0]][start[1]] = 0
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#' and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        return dist
    
    slave_dist = bfs((0, 0))
    tiger_dist = bfs(tiger_pos)
    
    exit_dist = slave_dist[n-1][m-1]
    
    can_escape = True
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '#' and slave_dist[i][j] != -1:
                if tiger_dist[i][j] <= slave_dist[i][j]:
                    can_escape = False
                    break
        if not can_escape:
            break
    
    print(exit_dist)
    print("Yes" if can_escape else "No")

if __name__ == "__main__":
    main()
