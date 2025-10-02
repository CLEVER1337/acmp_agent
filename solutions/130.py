
from collections import deque

def knight_moves(pos):
    x, y = ord(pos[0]) - ord('a'), int(pos[1]) - 1
    moves = []
    for dx, dy in [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8:
            moves.append((nx, ny))
    return moves

def solve():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        red_pos, green_pos = data[0], data[1]
    
    if red_pos == green_pos:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('0')
        return
    
    red_start = (ord(red_pos[0]) - ord('a'), int(red_pos[1]) - 1)
    green_start = (ord(green_pos[0]) - ord('a'), int(green_pos[1]) - 1)
    
    red_visited = {}
    green_visited = {}
    
    red_queue = deque([(red_start[0], red_start[1], 0)])
    green_queue = deque([(green_start[0], green_start[1], 0)])
    
    red_visited[(red_start[0], red_start[1])] = 0
    green_visited[(green_start[0], green_start[1])] = 0
    
    while red_queue and green_queue:
        red_x, red_y, red_steps = red_queue.popleft()
        green_x, green_y, green_steps = green_queue.popleft()
        
        if (red_x, red_y) in green_visited:
            if abs(green_visited[(red_x, red_y)] - red_steps) % 2 == 0:
                total_steps = max(green_visited[(red_x, red_y)], red_steps)
                with open('OUTPUT.TXT', 'w') as f:
                    f.write(str(total_steps))
                return
        
        if (green_x, green_y) in red_visited:
            if abs(red_visited[(green_x, green_y)] - green_steps) % 2 == 0:
                total_steps = max(red_visited[(green_x, green_y)], green_steps)
                with open('OUTPUT.TXT', 'w') as f:
                    f.write(str(total_steps))
                return
        
        for nx, ny in knight_moves(chr(red_x + ord('a')) + str(red_y + 1)):
            if (nx, ny) not in red_visited:
                red_visited[(nx, ny)] = red_steps + 1
                red_queue.append((nx, ny, red_steps + 1))
        
        for nx, ny in knight_moves(chr(green_x + ord('a')) + str(green_y + 1)):
            if (nx, ny) not in green_visited:
                green_visited[(nx, ny)] = green_steps + 1
                green_queue.append((nx, ny, green_steps + 1))
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('-1')

solve()
