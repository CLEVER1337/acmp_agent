
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
    
    start_x, start_y = n, n
    initial_dir = (-1, 0)
    
    enemy_ships = []
    islands = []
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 'E':
                enemy_ships.append((i, j))
            elif grid[i][j] == '#':
                islands.append((i, j))
    
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    
    def is_valid(x, y):
        return 0 <= x < size and 0 <= y < size
    
    def get_next_enemy_move(ex, ey, px, py):
        min_dist = float('inf')
        best_move = None
        for dx, dy in directions:
            nx, ny = ex + dx, ey + dy
            if is_valid(nx, ny):
                dist = abs(px - nx) + abs(py - ny)
                if dist < min_dist:
                    min_dist = dist
                    best_move = (nx, ny)
        return best_move
    
    def simulate_enemy_move(player_x, player_y, current_enemies, current_obstacles):
        new_enemies = set()
        collisions = set()
        enemy_positions = {}
        
        for ex, ey in current_enemies:
            move = get_next_enemy_move(ex, ey, player_x, player_y)
            if move:
                mx, my = move
                if (mx, my) in current_obstacles:
                    continue
                if (mx, my) == (player_x, player_y):
                    return None
                
                if (mx, my) not in enemy_positions:
                    enemy_positions[(mx, my)] = []
                enemy_positions[(mx, my)].append((ex, ey))
        
        for pos, enemies in enemy_positions.items():
            if len(enemies) == 1:
                new_enemies.add(pos)
            else:
                collisions.add(pos)
        
        return new_enemies, collisions
    
    def can_shoot(player_x, player_y, dir_dx, dir_dy, enemies, obstacles):
        destroyed = set()
        left_dir = (-dir_dy, dir_dx)
        right_dir = (dir_dy, -dir_dx)
        
        for side_dir in [left_dir, right_dir]:
            for dist in range(1, 4):
                tx, ty = player_x + side_dir[0] * dist, player_y + side_dir[1] * dist
                if not is_valid(tx, ty):
                    break
                    
                if (tx, ty) in obstacles:
                    break
                    
                if (tx, ty) in enemies:
                    destroyed.add((tx, ty))
                    break
        
        return destroyed
    
    visited = set()
    queue = deque()
    initial_state = (start_x, start_y, initial_dir[0], initial_dir[1], frozenset(enemy_ships), frozenset(islands))
    visited.add(initial_state)
    queue.append((initial_state, []))
    
    solution = None
    
    while queue:
        state, path = queue.popleft()
        px, py, dir_dx, dir_dy, enemies, obstacles = state
        
        if len(enemies) == 0:
            solution = (len(path), path)
            break
        
        for dx, dy in directions:
            nx, ny = px + dx, py + dy
            if not is_valid(nx, ny):
                continue
                
            if (nx, ny) in obstacles:
                continue
                
            new_dir = (dx, dy)
            new_enemies = set(enemies)
            new_obstacles = set(obstacles)
            
            enemy_result = simulate_enemy_move(nx, ny, new_enemies, new_obstacles)
            if enemy_result is None:
                continue
                
            next_enemies, new_collisions = enemy_result
            new_obstacles.update(new_collisions)
            
            new_state = (nx, ny, new_dir[0], new_dir[1], frozenset(next_enemies), frozenset(new_obstacles))
            if new_state not in visited:
                visited.add(new_state)
                new_path = path + [(nx, ny)]
                queue.append((new_state, new_path))
        
        destroyed = can_shoot(px, py, dir_dx, dir_dy, enemies, obstacles)
        if destroyed:
            new_enemies = set(enemies) - destroyed
            new_obstacles = set(obstacles) | destroyed
            
            enemy_result = simulate_enemy_move(px, py, new_enemies, new_obstacles)
            if enemy_result is None:
                continue
                
            next_enemies, new_collisions = enemy_result
            new_obstacles.update(new_collisions)
            
            new_state = (px, py, dir_dx, dir_dy, frozenset(next_enemies), frozenset(new_obstacles))
            if new_state not in visited:
                visited.add(new_state)
                new_path = path + [(px, py)]
                queue.append((new_state, new_path))
    
    if solution:
        moves_count, path = solution
        print(moves_count)
        for x, y in path:
            print(f"{x} {y}")
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()
