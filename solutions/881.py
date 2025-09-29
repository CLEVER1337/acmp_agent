
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
        parts = data[i].strip()[1:-1].split(',')
        x = int(parts[0]) - 1
        y = int(parts[1]) - 1
        direction = parts[2].strip()
        robots.append((x, y, direction))
    
    directions = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    
    time = 0
    active_robots = set(range(k))
    
    while active_robots:
        time += 1
        explosions = set()
        new_positions = {}
        
        for idx in active_robots:
            x, y, d = robots[idx]
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[ny][nx] == 'X':
                explosions.add(idx)
                continue
                
            new_positions[idx] = (nx, ny, d)
        
        for idx in active_robots:
            if idx in explosions:
                continue
                
            x, y, d = new_positions[idx]
            for other_idx in active_robots:
                if other_idx == idx or other_idx in explosions:
                    continue
                    
                ox, oy, od = new_positions[other_idx]
                if (x, y) == (ox, oy):
                    explosions.add(idx)
                    explosions.add(other_idx)
        
        lasers = {}
        for idx in active_robots:
            if idx in explosions:
                continue
                
            x, y, d = new_positions[idx]
            dx, dy = directions[d]
            lx, ly = x, y
            
            while True:
                lx += dx
                ly += dy
                if lx < 0 or lx >= m or ly < 0 or ly >= n or grid[ly][lx] == 'X':
                    break
                    
                lasers.setdefault((lx, ly), []).append(idx)
        
        for pos, robot_list in lasers.items():
            if len(robot_list) > 0:
                for idx in robot_list:
                    explosions.add(idx)
        
        for idx in explosions:
            active_robots.discard(idx)
            
        for idx in active_robots:
            robots[idx] = new_positions[idx]
    
    print(time)

if __name__ == "__main__":
    main()
