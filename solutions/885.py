
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
    start_dir = (-1, 0)
    
    enemy_ships = []
    islands = []
    for y in range(size):
        for x in range(size):
            if grid[y][x] == '+':
                start_x, start_y = x, y
            elif grid[y][x] == '!':
                enemy_ships.append((x, y))
            elif grid[y][x] == '@':
                islands.append((x, y))
    
    directions = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1),           (0, 1),
                 (1, -1),  (1, 0),  (1, 1)]
    
    def is_valid(x, y):
        return 0 <= x < size and 0 <= y < size
    
    def can_move_to(x, y, obstacles):
        if not is_valid(x, y):
            return False
        for ox, oy in obstacles:
            if x == ox and y == oy:
                return False
        return True
    
    def get_shoot_targets(ship_x, ship_y, dir_x, dir_y, obstacles):
        targets = []
        perp_dirs = []
        if dir_x == 0:
            perp_dirs = [(1, 0), (-1, 0)]
        elif dir_y == 0:
            perp_dirs = [(0, 1), (0, -1)]
        else:
            perp_dirs = [(1, -1), (-1, 1)]
        
        for dx, dy in perp_dirs:
            for dist in range(1, 4):
                tx, ty = ship_x + dx * dist, ship_y + dy * dist
                if not is_valid(tx, ty):
                    break
                hit = False
                for ex, ey in enemy_ships:
                    if tx == ex and ty == ey:
                        targets.append((tx, ty))
                        hit = True
                        break
                if hit:
                    break
                for ox, oy in obstacles:
                    if tx == ox and ty == oy:
                        break
        return targets
    
    def move_enemy_ships(player_x, player_y, obstacles):
        new_enemies = []
        destroyed = set()
        for ex, ey in enemy_ships:
            best_dist = float('inf')
            best_move = None
            for dx, dy in directions:
                nx, ny = ex + dx, ey + dy
                if not is_valid(nx, ny):
                    continue
                dist = abs(player_x - nx) + abs(player_y - ny)
                if dist < best_dist:
                    best_dist = dist
                    best_move = (nx, ny)
            
            if best_move:
                mx, my = best_move
                collision = False
                for ox, oy in obstacles:
                    if mx == ox and my == oy:
                        collision = True
                        break
                if collision:
                    destroyed.add((ex, ey))
                else:
                    new_enemies.append((mx, my))
        
        return new_enemies, destroyed
    
    visited = set()
    queue = deque()
    initial_state = (start_x, start_y, start_dir[0], start_dir[1], tuple(enemy_ships), tuple(islands))
    queue.append((initial_state, []))
    visited.add(initial_state)
    
    solution = None
    
    while queue:
        state, path = queue.popleft()
        x, y, dir_x, dir_y, enemies, obst = state
        
        if not enemies:
            solution = (len(path), path)
            break
        
        enemies_list = list(enemies)
        obstacles_list = list(obst)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if can_move_to(nx, ny, obstacles_list + enemies_list):
                new_dir = (dx, dy)
                new_enemies, destroyed = move_enemy_ships(nx, ny, obstacles_list)
                
                player_collision = False
                for ex, ey in new_enemies:
                    if ex == nx and ey == ny:
                        player_collision = True
                        break
                
                if player_collision:
                    continue
                
                new_obstacles = obstacles_list + list(destroyed)
                new_enemies_set = set(new_enemies)
                final_enemies = []
                seen_positions = set()
                collisions = set()
                
                for enemy in new_enemies:
                    if enemy in seen_positions:
                        collisions.add(enemy)
                    else:
                        seen_positions.add(enemy)
                
                for enemy in new_enemies:
                    if enemy not in collisions:
                        final_enemies.append(enemy)
                
                new_obstacles.extend(collisions)
                
                new_state = (nx, ny, new_dir[0], new_dir[1], tuple(final_enemies), tuple(new_obstacles))
                if new_state not in visited:
                    visited.add(new_state)
                    new_path = path + [(nx, ny)]
                    queue.append((new_state, new_path))
        
        shoot_targets = get_shoot_targets(x, y, dir_x, dir_y, obstacles_list)
        if shoot_targets:
            new_enemies_set = set(enemies_list)
            new_obstacles = obstacles_list.copy()
            
            for tx, ty in shoot_targets:
                if (tx, ty) in new_enemies_set:
                    new_enemies_set.remove((tx, ty))
                    new_obstacles.append((tx, ty))
            
            new_enemies, destroyed = move_enemy_ships(x, y, new_obstacles)
            
            player_collision = False
            for ex, ey in new_enemies:
                if ex == x and ey == y:
                    player_collision = True
                    break
            
            if player_collision:
                continue
            
            new_enemies_set = set(new_enemies)
            seen_positions = set()
            collisions = set()
            
            for enemy in new_enemies:
                if enemy in seen_positions:
                    collisions.add(enemy)
                else:
                    seen_positions.add(enemy)
            
            final_enemies = []
            for enemy in new_enemies:
                if enemy not in collisions:
                    final_enemies.append(enemy)
            
            new_obstacles.extend(collisions)
            
            new_state = (x, y, dir_x, dir_y, tuple(final_enemies), tuple(new_obstacles))
            if new_state not in visited:
                visited.add(new_state)
                new_path = path + [(x, y)]
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
