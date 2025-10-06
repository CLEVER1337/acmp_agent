
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(-1)
        return
        
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(data[i])
    
    start = (1, 1)
    end = (m-2, n-2)
    
    if grid[start[1]][start[0]] == '@' or grid[end[1]][end[0]] == '@':
        print(-1)
        return
        
    visited_count = [[0] * m for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_names = ['down', 'right', 'up', 'left']
    
    x, y = start
    visited_count[y][x] = 1
    steps = 0
    current_dir = 0
    
    while (x, y) != end:
        min_count = float('inf')
        candidates = []
        
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[ny][nx] != '@':
                count = visited_count[ny][nx]
                if count < min_count:
                    min_count = count
                    candidates = [i]
                elif count == min_count:
                    candidates.append(i)
        
        if not candidates:
            print(-1)
            return
            
        next_dir = current_dir
        if current_dir not in candidates:
            next_dir = candidates[0]
            for cand in candidates:
                if cand < next_dir:
                    next_dir = cand
        else:
            next_dir = current_dir
        
        dx, dy = directions[next_dir]
        nx, ny = x + dx, y + dy
        
        if grid[ny][nx] == '@':
            print(-1)
            return
            
        visited_count[ny][nx] += 1
        x, y = nx, ny
        current_dir = next_dir
        steps += 1
        
        if steps > 10**7:
            print(-1)
            return
            
    print(steps)

if __name__ == "__main__":
    main()
