
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(-1)
        return
        
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(list(data[i]))
    
    start = (1, 1)
    end = (m - 2, n - 2)
    
    if grid[start[1]][start[0]] == '@' or grid[end[1]][end[0]] == '@':
        print(-1)
        return
        
    visit_count = [[0] * m for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_names = ['right', 'down', 'left', 'up']
    
    x, y = start
    visit_count[y][x] = 1
    steps = 0
    current_dir = 0
    
    while (x, y) != end:
        if steps > 10000000:
            print(-1)
            return
            
        dx, dy = directions[current_dir]
        nx, ny = x + dx, y + dy
        
        if grid[ny][nx] != '@':
            x, y = nx, ny
            visit_count[y][x] += 1
            steps += 1
            continue
            
        possible_dirs = []
        min_visits = float('inf')
        
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if grid[ny][nx] != '@':
                if visit_count[ny][nx] < min_visits:
                    min_visits = visit_count[ny][nx]
                    possible_dirs = [i]
                elif visit_count[ny][nx] == min_visits:
                    possible_dirs.append(i)
        
        if not possible_dirs:
            print(-1)
            return
            
        if current_dir in possible_dirs:
            new_dir = current_dir
        else:
            new_dir = min(possible_dirs)
        
        dx, dy = directions[new_dir]
        x += dx
        y += dy
        visit_count[y][x] += 1
        steps += 1
        current_dir = new_dir
    
    print(steps)

if __name__ == "__main__":
    main()
