
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        grid = [list(f.readline().strip()) for _ in range(n)]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * n for _ in range(n)]
    from collections import deque
    
    queue = deque([(0, 0)])
    visited[0][0] = True
    walls = set()
    
    while queue:
        i, j = queue.popleft()
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < n:
                if grid[ni][nj] == '#':
                    walls.add((i, j, ni, nj))
                elif not visited[ni][nj]:
                    visited[ni][nj] = True
                    queue.append((ni, nj))
    
    queue = deque([(n-1, n-1)])
    visited[n-1][n-1] = True
    while queue:
        i, j = queue.popleft()
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < n:
                if grid[ni][nj] == '#':
                    walls.add((i, j, ni, nj))
                elif not visited[ni][nj]:
                    visited[ni][nj] = True
                    queue.append((ni, nj))
    
    external_walls = set()
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '#' or not visited[i][j]:
                continue
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if ni < 0 or ni >= n or nj < 0 or nj >= n:
                    external_walls.add((i, j, ni, nj))
    
    all_walls = walls | external_walls
    area = len(all_walls) * 25
    print(area)

if __name__ == '__main__':
    main()
