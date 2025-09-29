
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        grid = [list(f.readline().strip()) for _ in range(n)]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * n for _ in range(n)]
    queue = [(0, 0)]
    visited[0][0] = True
    
    walls = set()
    
    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == '#':
                    walls.add((x, y, nx, ny))
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    total_area = 0
    for wall in walls:
        x1, y1, x2, y2 = wall
        if x1 == x2:
            total_area += 5
        else:
            total_area += 5
    
    print(total_area)

if __name__ == '__main__':
    main()
