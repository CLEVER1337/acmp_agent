
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
        d = parts[2].strip()
        robots.append((x, y, d))
    
    directions = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    time = 0
    active = [True] * k
    
    while any(active):
        positions = {}
        lasers = {}
        
        for idx, (x, y, d) in enumerate(robots):
            if not active[idx]:
                continue
                
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < m and 0 <= ny < n and grid[ny][nx] != 'X':
                positions[idx] = (nx, ny, d)
            else:
                positions[idx] = (x, y, d)
                
            lx, ly = x, y
            while True:
                lx += dx
                ly += dy
                if not (0 <= lx < m and 0 <= ly < n) or grid[ly][lx] == 'X':
                    break
                lasers[(lx, ly)] = lasers.get((lx, ly), 0) + 1
        
        explosions = set()
        for idx in positions:
            x, y, d = positions[idx]
            if (x, y) in lasers:
                explosions.add(idx)
                
        pos_count = {}
        for idx in positions:
            if idx in explosions:
                continue
            x, y, d = positions[idx]
            pos_count[(x, y)] = pos_count.get((x, y), 0) + 1
            
        for pos, count in pos_count.items():
            if count > 1:
                for idx in positions:
                    if idx in explosions:
                        continue
                    x, y, d = positions[idx]
                    if (x, y) == pos:
                        explosions.add(idx)
                        
        for idx in explosions:
            active[idx] = False
            
        robots = []
        for idx in range(k):
            if active[idx]:
                x, y, d = positions[idx]
                robots.append((x, y, d))
            else:
                robots.append((0, 0, 'U'))
                
        time += 1
        
    print(time)

if __name__ == "__main__":
    main()
