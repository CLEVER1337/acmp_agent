
def main():
    import sys
    sys.setrecursionlimit(10000)
    
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    grid = []
    for i in range(1, 1 + n):
        grid.append(list(data[i]))
    
    cities = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'C':
                cities.append((i, j))
    
    total_cities = len(cities)
    cities_per_state = total_cities // 2
    
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'C':
                result[i][j] = 1
            else:
                result[i][j] = 1
    
    count_state1 = total_cities
    
    def dfs(x, y, target_state):
        stack = [(x, y)]
        visited = set()
        visited.add((x, y))
        changed = []
        
        while stack:
            cx, cy = stack.pop()
            changed.append((cx, cy))
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if (nx, ny) not in visited and result[nx][ny] != target_state:
                        visited.add((nx, ny))
                        stack.append((nx, ny))
        
        return changed
    
    for i in range(n):
        for j in range(n):
            if count_state1 == cities_per_state:
                break
            if result[i][j] == 1 and grid[i][j] != 'C':
                changed_cells = dfs(i, j, 2)
                count_state1 -= sum(1 for x, y in changed_cells if grid[x][y] == 'C')
                for x, y in changed_cells:
                    result[x][y] = 2
        if count_state1 == cities_per_state:
            break
    
    for i in range(n):
        print(''.join(str(result[i][j]) for j in range(n)))

if __name__ == '__main__':
    main()
