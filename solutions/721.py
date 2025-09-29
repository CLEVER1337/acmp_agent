
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1+n):
        grid.append(list(data[i]))
    
    directions = ['R', 'L', 'U', 'D']
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    def get_neighbors(i, j):
        neighbors = []
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != '.':
                neighbors.append((ni, nj, d))
        return neighbors
    
    def find_cycle_min(i, j, visited, path):
        if (i, j) in visited:
            return
        visited.add((i, j))
        path.append((i, j))
        
        neighbors = get_neighbors(i, j)
        if not neighbors:
            return
        
        ni, nj, d = neighbors[0]
        grid[i][j] = directions[d]
        find_cycle_min(ni, nj, visited, path)
    
    def find_cycle_max(i, j, visited, path):
        if (i, j) in visited:
            return
        visited.add((i, j))
        path.append((i, j))
        
        neighbors = get_neighbors(i, j)
        if not neighbors:
            return
        
        for ni, nj, d in neighbors:
            if (ni, nj) not in visited:
                grid[i][j] = directions[d]
                find_cycle_max(ni, nj, visited, path)
                break
        else:
            ni, nj, d = neighbors[0]
            grid[i][j] = directions[d]
    
    grid_min = [row[:] for row in grid]
    visited_min = set()
    for i in range(n):
        for j in range(m):
            if grid_min[i][j] == '?' and (i, j) not in visited_min:
                path = []
                find_cycle_min(i, j, visited_min, path)
    
    grid_max = [row[:] for row in grid]
    visited_max = set()
    for i in range(n):
        for j in range(m):
            if grid_max[i][j] == '?' and (i, j) not in visited_max:
                path = []
                find_cycle_max(i, j, visited_max, path)
    
    for row in grid_min:
        print(''.join(row))
    print()
    for row in grid_max:
        print(''.join(row))

if __name__ == "__main__":
    main()
