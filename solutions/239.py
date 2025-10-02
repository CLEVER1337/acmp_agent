
def main():
    import sys
    from itertools import product
    
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    idx = 0
    N = int(data[idx]); M = int(data[idx+1]); K = int(data[idx+2]); idx += 3
    
    grid = []
    for i in range(N):
        row = list(map(int, data[idx:idx+M]))
        idx += M
        grid.append(row)
    
    tiles = []
    for i in range(K):
        form = int(data[idx]); cost = int(data[idx+1]); idx += 2
        colors = list(map(int, data[idx:idx+form]))
        idx += form
        tiles.append((form, cost, colors))
    
    total_cells = N * M
    covered = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 2:
                covered += 1
    
    remaining = total_cells - covered
    if remaining == 0:
        print(0)
        return
    
    rotations = {
        1: [[(0,0)]],
        2: [[(0,0), (0,1)], [(0,0), (1,0)]],
        3: [[(0,0), (0,1), (1,0)], [(0,0), (0,1), (1,1)], [(0,0), (1,0), (1,1)], [(0,1), (1,0), (1,1)]],
        4: [[(0,0), (0,1), (1,0), (1,1)]]
    }
    
    def get_all_rotations(form, colors):
        base = rotations[form]
        all_rots = []
        for pattern in base:
            for rot in range(4):
                rotated_pattern = []
                for dx, dy in pattern:
                    if rot == 0:
                        new_dx, new_dy = dx, dy
                    elif rot == 1:
                        new_dx, new_dy = -dy, dx
                    elif rot == 2:
                        new_dx, new_dy = -dx, -dy
                    else:
                        new_dx, new_dy = dy, -dx
                    rotated_pattern.append((new_dx, new_dy))
                
                min_x = min(dx for dx, dy in rotated_pattern)
                min_y = min(dy for dx, dy in rotated_pattern)
                normalized = [(dx - min_x, dy - min_y) for dx, dy in rotated_pattern]
                all_rots.append((normalized, colors))
        return all_rots
    
    all_tile_variants = []
    for form, cost, colors in tiles:
        variants = get_all_rotations(form, colors)
        for pattern, col in variants:
            all_tile_variants.append((pattern, cost, col))
    
    INF = 10**9
    dp = [INF] * (1 << total_cells)
    dp[0] = 0
    
    def get_mask_index(i, j):
        return i * M + j
    
    def can_place(pattern, i, j, state_mask):
        for dx, dy in pattern:
            ni, nj = i + dx, j + dy
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                return False
            if grid[ni][nj] == 2:
                return False
            idx = get_mask_index(ni, nj)
            if state_mask & (1 << idx):
                return False
        return True
    
    def get_new_mask(pattern, i, j, state_mask):
        new_mask = state_mask
        for dx, dy in pattern:
            ni, nj = i + dx, j + dy
            idx = get_mask_index(ni, nj)
            new_mask |= (1 << idx)
        return new_mask
    
    def check_colors(pattern, colors, i, j):
        for (dx, dy), color in zip(pattern, colors):
            ni, nj = i + dx, j + dy
            if grid[ni][nj] not in [2, color]:
                return False
        return True
    
    for mask in range(1 << total_cells):
        if dp[mask] == INF:
            continue
            
        found = False
        for i in range(N):
            for j in range(M):
                idx_pos = get_mask_index(i, j)
                if mask & (1 << idx_pos):
                    continue
                if grid[i][j] == 2:
                    continue
                    
                found = True
                for pattern, cost, colors in all_tile_variants:
                    if can_place(pattern, i, j, mask) and check_colors(pattern, colors, i, j):
                        new_mask = get_new_mask(pattern, i, j, mask)
                        new_cost = dp[mask] + cost
                        if new_cost < dp[new_mask]:
                            dp[new_mask] = new_cost
                break
            if found:
                break
    
    full_mask = (1 << total_cells) - 1
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 2:
                idx_pos = get_mask_index(i, j)
                full_mask &= ~(1 << idx_pos)
                
    result = dp[full_mask]
    if result == INF:
        print(-1)
    else:
        print(result)

if __name__ == "__main__":
    main()
