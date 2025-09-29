
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(-1)
        return
        
    n, m, k = map(int, data[0].split())
    grid = []
    for i in range(1, 1+n):
        grid.append(list(map(int, data[i].split())))
    
    tiles = []
    for i in range(1+n, 1+n+k):
        parts = data[i].split()
        shape = int(parts[0])
        cost = int(parts[1])
        colors = list(map(int, parts[2:]))
        tiles.append((shape, cost, colors))
    
    total_cells = n * m
    covered = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                covered += 1
    
    uncovered = total_cells - covered
    if uncovered == 0:
        print(0)
        return
    
    min_cost = [float('inf')]
    
    def backtrack(i, j, cost_so_far):
        if cost_so_far >= min_cost[0]:
            return
        
        if i == n:
            min_cost[0] = min(min_cost[0], cost_so_far)
            return
        
        if j == m:
            backtrack(i+1, 0, cost_so_far)
            return
        
        if grid[i][j] == 2:
            backtrack(i, j+1, cost_so_far)
            return
        
        for shape, cost, colors in tiles:
            if shape == 1:
                if j < m and grid[i][j] in [colors[0], 2]:
                    original = grid[i][j]
                    grid[i][j] = 2
                    backtrack(i, j+1, cost_so_far + cost)
                    grid[i][j] = original
            
            elif shape == 2:
                if j+1 < m and grid[i][j] in [colors[0], 2] and grid[i][j+1] in [colors[1], 2]:
                    orig1 = grid[i][j]
                    orig2 = grid[i][j+1]
                    grid[i][j] = 2
                    grid[i][j+1] = 2
                    backtrack(i, j+2, cost_so_far + cost)
                    grid[i][j] = orig1
                    grid[i][j+1] = orig2
            
            elif shape == 3:
                if i+1 < n and grid[i][j] in [colors[0], 2] and grid[i+1][j] in [colors[1], 2]:
                    orig1 = grid[i][j]
                    orig2 = grid[i+1][j]
                    grid[i][j] = 2
                    grid[i+1][j] = 2
                    backtrack(i, j+1, cost_so_far + cost)
                    grid[i][j] = orig1
                    grid[i+1][j] = orig2
            
            elif shape == 4:
                if i+1 < n and j+1 < m:
                    valid = True
                    origs = []
                    positions = [(i, j), (i, j+1), (i+1, j)]
                    for idx, (x, y) in enumerate(positions):
                        if grid[x][y] not in [colors[idx], 2]:
                            valid = False
                        origs.append(grid[x][y])
                    
                    if valid:
                        for x, y in positions:
                            grid[x][y] = 2
                        backtrack(i, j+2, cost_so_far + cost)
                        for idx, (x, y) in enumerate(positions):
                            grid[x][y] = origs[idx]
        
        if grid[i][j] != 2:
            return
    
    backtrack(0, 0, 0)
    
    if min_cost[0] == float('inf'):
        print(-1)
    else:
        print(min_cost[0])

if __name__ == "__main__":
    main()
