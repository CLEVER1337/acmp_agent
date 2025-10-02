
import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print("IMPOSSIBLE")
        return
        
    n = int(data[0])
    size = 2 * n + 1
    grid = []
    for i in range(1, 1 + size):
        grid.append(list(data[i].strip()))
    
    start_pos = (n, n)
    start_dir = (n-1, n)
    
    enemy_ships = []
    islands = []
    for i in range(size):
        for j in range(size):
            if grid[i][j] == '@':
                enemy_ships.append((i, j))
            elif grid[i][j] == '#':
                islands.append((i, j))
    
    def get_direction(from_pos, to_pos):
        dx = to_pos[0] - from_pos[0]
        dy = to_pos[1] - from_pos[1]
        return (dx, dy)
    
    def normalize_direction(dx, dy):
        if dx == 0 and dy == 0:
            return (0, 0)
        if dx == 0:
            return (0, 1 if dy > 0 else -1)
        if dy == 0:
            return (1 if dx > 0 else -1, 0)
        return (1 if dx > 0 else -1, 1 if dy > 0 else -1)
    
    def get_perpendicular_directions(dx, dy):
        if dx == 0:
            return [(1, 0), (-1, 0)]
        if dy == 0:
            return [(0, 1), (0, -1)]
        return [(dy, -dx), (-dy, dx)]
    
    def is_valid_pos(x, y):
        return 0 <= x < size and 0 <= y < size
    
    def simulate_shot(grid_copy, pos, direction):
        x, y = pos
        dx, dy = direction
        perp_dirs = get_perpendicular_directions(dx, dy)
        destroyed = set()
        new_wrecks = []
        
        for pdx, pdy in perp_dirs:
            for dist in range(1, 4):
                tx, ty = x + pdx * dist, y + pdy * dist
                if not is_valid_pos(tx, ty):
                    break
                    
                cell = grid_copy[tx][ty]
                if cell == '@':
                    destroyed.add((tx, ty))
                    new_wrecks.append((tx, ty))
                    break
                elif cell == '#' or cell == '*':
                    break
        
        return destroyed, new_wrecks
    
    def move_enemy_ships(grid_copy, player_pos):
        new_enemies = []
        wrecks_created = []
        enemy_positions = {}
        
        for i in range(size):
            for j in range(size):
                if grid_copy[i][j] == '@':
                    px, py = player_pos
                    best_dist = float('inf')
                    best_move = None
                    
                    for dx, dy in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
                        nx, ny = i + dx, j + dy
                        if is_valid_pos(nx, ny):
                            dist = abs(px - nx) + abs(py - ny)
                            if dist < best_dist:
                                best_dist = dist
                                best_move = (nx, ny)
                    
                    if best_move:
                        nx, ny = best_move
                        if grid_copy[nx][ny] == '.':
                            enemy_positions[(nx, ny)] = enemy_positions.get((nx, ny), 0) + 1
                        elif grid_copy[nx][ny] == '+':
                            return None
                        elif grid_copy[nx][ny] == '#':
                            wrecks_created.append((nx, ny))
        
        for (x, y), count in enemy_positions.items():
            if count == 1:
                new_enemies.append((x, y))
            else:
                wrecks_created.append((x, y))
                
        return new_enemies, wrecks_created
    
    def state_hash(player_pos, player_dir, enemies_set, wrecks_set):
        return (player_pos, player_dir, frozenset(enemies_set), frozenset(wrecks_set))
    
    visited = set()
    queue = deque()
    initial_enemies = set(enemy_ships)
    initial_wrecks = set()
    
    initial_state = (start_pos, get_direction(start_dir, start_pos), initial_enemies, initial_wrecks)
    visited.add(state_hash(*initial_state))
    queue.append((initial_state, []))
    
    while queue:
        current_state, path = queue.popleft()
        player_pos, player_dir, enemies, wrecks = current_state
        
        if not enemies:
            print(len(path))
            for pos in path:
                print(f"{pos[0]} {pos[1]}")
            return
        
        grid_copy = [['.' for _ in range(size)] for _ in range(size)]
        grid_copy[player_pos[0]][player_pos[1]] = '+'
        
        for ex, ey in enemies:
            grid_copy[ex][ey] = '@'
        
        for wx, wy in wrecks:
            grid_copy[wx][wy] = '*'
        
        for ix, iy in islands:
            grid_copy[ix][iy] = '#'
        
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
            nx, ny = player_pos[0] + dx, player_pos[1] + dy
            if is_valid_pos(nx, ny) and grid_copy[nx][ny] == '.':
                new_dir = normalize_direction(dx, dy)
                new_pos = (nx, ny)
                new_enemies = set(enemies)
                new_wrecks = set(wrecks)
                
                enemy_result = move_enemy_ships(grid_copy, new_pos)
                if enemy_result is None:
                    continue
                    
                moved_enemies, new_wrecks_from_move = enemy_result
                new_enemies = set(moved_enemies)
                new_wrecks.update(new_wrecks_from_move)
                
                new_state = (new_pos, new_dir, new_enemies, new_wrecks)
                state_key = state_hash(*new_state)
                
                if state_key not in visited:
                    visited.add(state_key)
                    queue.append((new_state, path + [new_pos]))
        
        destroyed, new_wrecks_from_shot = simulate_shot(grid_copy, player_pos, player_dir)
        new_enemies = set(enemies) - destroyed
        new_wrecks = set(wrecks)
        new_wrecks.update(new_wrecks_from_shot)
        
        enemy_result = move_enemy_ships(grid_copy, player_pos)
        if enemy_result is None:
            continue
            
        moved_enemies, new_wrecks_from_move = enemy_result
        new_enemies = set(moved_enemies)
        new_wrecks.update(new_wrecks_from_move)
        
        new_state = (player_pos, player_dir, new_enemies, new_wrecks)
        state_key = state_hash(*new_state)
        
        if state_key not in visited:
            visited.add(state_key)
            queue.append((new_state, path))
    
    print("IMPOSSIBLE")

if __name__ == "__main__":
    main()
