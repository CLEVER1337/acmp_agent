
def main():
    import sys
    from itertools import product
    
    data = sys.stdin.read().splitlines()
    m, n = map(int, data[0].split())
    tile_pattern = []
    for i in range(1, 4):
        tile_pattern.append(data[i].strip())
    
    tile_cells = []
    for i in range(3):
        for j in range(3):
            if tile_pattern[i][j] == 'X':
                tile_cells.append((i, j))
    
    def get_offsets():
        offsets = []
        for dx in range(-2, m + 2):
            for dy in range(-2, n + 2):
                offsets.append((dx, dy))
        return offsets
    
    def is_valid(x, y):
        return 0 <= x < m and 0 <= y < n
    
    def cover_grid(offsets):
        grid = [[0] * n for _ in range(m)]
        count = 0
        for dx, dy in offsets:
            covered = False
            for i, j in tile_cells:
                x, y = dx + i, dy + j
                if is_valid(x, y):
                    grid[x][y] += 1
                    covered = True
            if covered:
                count += 1
        return grid, count
    
    def is_full_coverage(grid):
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    return False
        return True
    
    min_tiles = float('inf')
    offsets_list = get_offsets()
    
    from itertools import combinations
    for k in range(1, (m * n) // 6 + 3):
        for combo in combinations(offsets_list, k):
            grid, count = cover_grid(combo)
            if is_full_coverage(grid):
                min_tiles = min(min_tiles, count)
                if min_tiles == count:
                    break
        if min_tiles != float('inf'):
            break
            
    print(min_tiles)

if __name__ == "__main__":
    main()
