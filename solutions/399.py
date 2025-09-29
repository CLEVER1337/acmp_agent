
def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    data = sys.stdin.read().splitlines()
    if not data:
        print(-1)
        return
        
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(data[i].rstrip('\n'))
    
    start = (1, 1)
    end = (m - 2, n - 2)
    
    if grid[start[1]][start[0]] == '@' or grid[end[1]][end[0]] == '@':
        print(-1)
        return
        
    visited_count = [[0] * m for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_names = ['down', 'right', 'up', 'left']
    priority_order = [0, 1, 2, 3]
    
    x, y = start
    current_dir = 0
    steps = 0
    max_steps = 10000000
    
    visited_count[y][x] = 1
    
    while (x, y) != end and steps < max_steps:
        counts = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[ny][nx] != '@':
                counts.append(visited_count[ny][nx])
            else:
                counts.append(float('inf'))
                
        min_count = min(counts)
        candidates = [i for i in range(4) if counts[i] == min_count]
        
        if current_dir in candidates:
            new_dir = current_dir
        else:
            for candidate in priority_order:
                if candidate in candidates:
                    new_dir = candidate
                    break
            else:
                new_dir = current_dir
                
        dx, dy = directions[new_dir]
        nx, ny = x + dx, y + dy
        
        if grid[ny][nx] == '@':
            print(-1)
            return
            
        x, y = nx, ny
        current_dir = new_dir
        visited_count[y][x] += 1
        steps += 1
        
    if (x, y) == end:
        print(steps)
    else:
        print(-1)

if __name__ == "__main__":
    main()
