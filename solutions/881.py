
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    m, n, k = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(data[i].strip())
    
    robots = []
    for i in range(1 + n, 1 + n + k):
        parts = data[i].strip().replace('(', '').replace(')', '').split(',')
        x = int(parts[0]) - 1
        y = int(parts[1]) - 1
        direction = parts[2].strip()
        robots.append((x, y, direction))
    
    directions = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    time = 0
    active_robots = set(range(k))
    
    while active_robots:
        time += 1
        positions = {}
        new_positions = {}
        lasers = {}
        
        for idx in active_robots:
            x, y, d = robots[idx]
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
            robots[idx] = (nx, ny, d)
            positions[idx] = (nx, ny)
            new_positions[(nx, ny)] = new_positions.get((nx, ny), []) + [idx]
            
            lx, ly = nx, ny
            while 0 <= lx < m and 0 <= ly < n and grid[ly][lx] != 'X':
                lx += dx
                ly += dy
            lasers[idx] = (lx - dx, ly - dy)
        
        to_explode = set()
        
        for idx in active_robots:
            x, y, d = robots[idx]
            if not (0 <= x < m and 0 <= y < n) or grid[y][x] == 'X':
                to_explode.add(idx)
                continue
                
            if len(new_positions.get((x, y), [])) > 1:
                to_explode.add(idx)
                continue
                
            lx, ly = lasers[idx]
            dx, dy = directions[d]
            cx, cy = x, y
            while (cx, cy) != (lx, ly):
                cx += dx
                cy += dy
                if (cx, cy) in positions.values():
                    for other_idx, pos in positions.items():
                        if pos == (cx, cy):
                            to_explode.add(other_idx)
                            to_explode.add(idx)
        
        active_robots -= to_explode
        
    print(time)

if __name__ == "__main__":
    main()
