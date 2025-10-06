
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    grid = []
    for i in range(1, n+1):
        grid.append(data[i].strip())
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * n for _ in range(n)]
    from collections import deque
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    walls = set()
    
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == '#':
                    walls.add((x, y, nx, ny))
                else:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
    
    q2 = deque()
    q2.append((n-1, n-1))
    visited2 = [[False] * n for _ in range(n)]
    visited2[n-1][n-1] = True
    
    while q2:
        x, y = q2.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == '#':
                    walls.add((x, y, nx, ny))
                else:
                    if not visited2[nx][ny]:
                        visited2[nx][ny] = True
                        q2.append((nx, ny))
    
    total_area = 0
    for wall in walls:
        x1, y1, x2, y2 = wall
        if x1 == x2:
            total_area += 5
        else:
            total_area += 5
    
    outer_walls = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                if i == 0:
                    outer_walls += 5
                if i == n-1:
                    outer_walls += 5
                if j == 0:
                    outer_walls += 5
                if j == n-1:
                    outer_walls += 5
                    
    for i in range(n):
        for j in range(n):
            if visited2[i][j]:
                if i == 0:
                    outer_walls += 5
                if i == n-1:
                    outer_walls += 5
                if j == 0:
                    outer_walls += 5
                if j == n-1:
                    outer_walls += 5
    
    total_area -= outer_walls
    print(total_area)

if __name__ == "__main__":
    main()
