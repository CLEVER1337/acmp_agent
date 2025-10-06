
def main():
    with open('INPUT.TXT', 'r') as f:
        path = f.readline().strip()
    
    directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
    reverse_dir = {(0, 1): 'N', (0, -1): 'S', (1, 0): 'E', (-1, 0): 'W'}
    priority = ['N', 'E', 'S', 'W']
    
    x, y = 0, 0
    visited = set()
    visited.add((x, y))
    
    for move in path:
        dx, dy = directions[move]
        x += dx
        y += dy
        visited.add((x, y))
    
    start = (x, y)
    end = (0, 0)
    
    queue = [(start, [])]
    visited_path = {start: []}
    
    while queue:
        current, path_so_far = queue.pop(0)
        if current == end:
            break
            
        for dir_char in priority:
            dx, dy = directions[dir_char]
            nx, ny = current[0] + dx, current[1] + dy
            next_pos = (nx, ny)
            
            if next_pos in visited and next_pos not in visited_path:
                new_path = path_so_far + [dir_char]
                visited_path[next_pos] = new_path
                queue.append((next_pos, new_path))
    
    result = ''.join(visited_path[end])
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()
