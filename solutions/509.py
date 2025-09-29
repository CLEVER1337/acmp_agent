
from collections import deque

def main():
    with open('INPUT.TXT', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    
    start = lines[0] + lines[1]
    target = lines[2] + lines[3]
    
    def get_neighbors(state):
        pos = state.index('#')
        neighbors = []
        row, col = pos // 4, pos % 4
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 2 and 0 <= new_col < 4:
                new_pos = new_row * 4 + new_col
                state_list = list(state)
                state_list[pos], state_list[new_pos] = state_list[new_pos], state_list[pos]
                neighbors.append(''.join(state_list))
        return neighbors
    
    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)
    
    while queue:
        current, moves = queue.popleft()
        
        if current == target:
            with open('OUTPUT.TXT', 'w') as f:
                f.write(str(moves))
            return
        
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, moves + 1))
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('-1')

if __name__ == '__main__':
    main()
