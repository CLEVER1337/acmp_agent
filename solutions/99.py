
from collections import deque

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().splitlines()
    
    h, m, n = map(int, data[0].split())
    levels = []
    index = 1
    prince_pos = None
    princess_pos = None
    
    for level_idx in range(h):
        grid = []
        for i in range(m):
            line = data[index].strip()
            index += 1
            grid.append(list(line))
            
            if '1' in line:
                prince_pos = (level_idx, i, line.index('1'))
            if '2' in line:
                princess_pos = (level_idx, i, line.index('2'))
        
        levels.append(grid)
        if index < len(data) and data[index].strip() == '':
            index += 1
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    visited = [[[float('inf')] * n for _ in range(m)] for __ in range(h)]
    lvl, row, col = prince_pos
    visited[lvl][row][col] = 0
    
    queue = deque([(lvl, row, col)])
    
    while queue:
        lvl, row, col = queue.popleft()
        current_time = visited[lvl][row][col]
        
        if (lvl, row, col) == princess_pos:
            print(current_time)
            return
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < m and 0 <= new_col < n:
                if levels[lvl][new_row][new_col] != 'o':
                    if visited[lvl][new_row][new_col] > current_time + 5:
                        visited[lvl][new_row][new_col] = current_time + 5
                        queue.append((lvl, new_row, new_col))
        
        if lvl < h - 1 and levels[lvl][row][col] != 'o':
            if visited[lvl + 1][row][col] > current_time + 5:
                visited[lvl + 1][row][col] = current_time + 5
                queue.append((lvl + 1, row, col))
    
    print(visited[princess_pos[0]][princess_pos[1]][princess_pos[2]])

if __name__ == "__main__":
    main()
