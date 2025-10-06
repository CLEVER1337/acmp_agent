
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(-1)
        return
        
    n, m, k = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(list(map(int, data[i].split())))
    
    tiles = []
    for i in range(1 + n, 1 + n + k):
        parts = data[i].split()
        shape = int(parts[0])
        cost = int(parts[1])
        colors = list(map(int, parts[2:]))
        tiles.append((shape, cost, colors))
    
    total_cells = n * m
    fixed = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                fixed += 1
                
    def get_tile_rotations(shape, colors):
        if shape == 1:
            return [colors]
        elif shape == 2:
            base = colors
            rot1 = [base[0], base[1]]
            rot2 = [base[1], base[0]]
            return [rot1, rot2]
        elif shape == 3:
            base = colors
            rot1 = [base[0], base[1], base[2]]
            rot2 = [base[2], base[0], base[1]]
            rot3 = [base[1], base[2], base[0]]
            return [rot1, rot2, rot3]
        elif shape == 4:
            base = colors
            rot1 = [base[0], base[1], base[2], base[3]]
            rot2 = [base[3], base[0], base[1], base[2]]
            rot3 = [base[2], base[3], base[0], base[1]]
            rot4 = [base[1], base[2], base[3], base[0]]
            return [rot1, rot2, rot3, rot4]
        return []
    
    all_tiles = []
    for shape, cost, colors in tiles:
        rotations = get_tile_rotations(shape, colors)
        for rot in rotations:
            all_tiles.append((shape, cost, rot))
    
    def get_cells(shape, x, y):
        if shape == 1:
            return [(x, y)]
        elif shape == 2:
            return [(x, y), (x, y+1)]
        elif shape == 3:
            return [(x, y), (x+1, y), (x, y+1)]
        elif shape == 4:
            return [(x, y), (x, y+1), (x+1, y), (x+1, y+1)]
        return []
    
    def can_place(shape, x, y, rot):
        cells = get_cells(shape, x, y)
        for idx, (i, j) in enumerate(cells):
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            if grid[i][j] != 2 and grid[i][j] != rot[idx]:
                return False
        return True
    
    def place(shape, x, y, rot):
        cells = get_cells(shape, x, y)
        changes = []
        for idx, (i, j) in enumerate(cells):
            if grid[i][j] != 2:
                changes.append((i, j, grid[i][j]))
                grid[i][j] = 2
        return changes
    
    def unplace(changes):
        for i, j, val in changes:
            grid[i][j] = val
    
    memo = {}
    def dfs(x, y):
        if y == m:
            y = 0
            x += 1
        if x == n:
            return 0
            
        if grid[x][y] == 2:
            return dfs(x, y+1)
            
        key = tuple(tuple(row) for row in grid)
        if key in memo:
            return memo[key]
            
        best = float('inf')
        for shape, cost, rot in all_tiles:
            if can_place(shape, x, y, rot):
                changes = place(shape, x, y, rot)
                res = dfs(x, y+1)
                if res != float('inf'):
                    best = min(best, cost + res)
                unplace(changes)
                
        memo[key] = best
        return best
        
    result = dfs(0, 0)
    if result == float('inf'):
        print(-1)
    else:
        print(result)

if __name__ == "__main__":
    main()
