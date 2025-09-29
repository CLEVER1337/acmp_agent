
from collections import deque

def knight_moves(pos):
    x, y = pos
    moves = []
    for dx, dy in [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8:
            moves.append((nx, ny))
    return moves

def solve():
    with open('input.txt', 'r') as f:
        data = f.read().split()
        red_pos = data[0]
        green_pos = data[1]
    
    def pos_to_coords(pos):
        col = ord(pos[0]) - ord('a')
        row = int(pos[1]) - 1
        return (col, row)
    
    red_start = pos_to_coords(red_pos)
    green_start = pos_to_coords(green_pos)
    
    if red_start == green_start:
        return 0
    
    red_visited = {red_start: 0}
    green_visited = {green_start: 0}
    
    red_queue = deque([red_start])
    green_queue = deque([green_start])
    
    while red_queue and green_queue:
        red_current = red_queue.popleft()
        green_current = green_queue.popleft()
        
        red_moves = knight_moves(red_current)
        green_moves = knight_moves(green_current)
        
        for red_next in red_moves:
            if red_next not in red_visited:
                red_visited[red_next] = red_visited[red_current] + 1
                red_queue.append(red_next)
                
                if red_next in green_visited:
                    return max(red_visited[red_next], green_visited[red_next])
        
        for green_next in green_moves:
            if green_next not in green_visited:
                green_visited[green_next] = green_visited[green_current] + 1
                green_queue.append(green_next)
                
                if green_next in red_visited:
                    return max(red_visited[green_next], green_visited[green_next])
    
    return -1

result = solve()
with open('output.txt', 'w') as f:
    f.write(str(result))
