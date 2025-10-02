
from collections import deque

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().splitlines()
    
    h, m, n = map(int, data[0].split())
    levels = []
    index = 1
    
    for i in range(h):
        level = []
        for j in range(m):
            level.append(data[index].strip())
            index += 1
        levels.append(level)
        if i < h - 1:
            index += 1
    
    start_level = 0
    start_i = 0
    start_j = 0
    end_level = h - 1
    end_i = 0
    end_j = 0
    
    for level_idx in range(h):
        for i in range(m):
            for j in range(n):
                if levels[level_idx][i][j] == '1':
                    start_level = level_idx
                    start_i = i
                    start_j = j
                elif levels[level_idx][i][j] == '2':
                    end_level = level_idx
                    end_i = i
                    end_j = j
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    visited = [[[-1] * n for _ in range(m)] for __ in range(h)]
    queue = deque()
    queue.append((start_level, start_i, start_j))
    visited[start_level][start_i][start_j] = 0
    
    while queue:
        level, i, j = queue.popleft()
        current_time = visited[level][i][j]
        
        if level == end_level and i == end_i and j == end_j:
            print(current_time)
            return
            
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < m and 0 <= nj < n and levels[level][ni][nj] != 'o':
                if visited[level][ni][nj] == -1:
                    visited[level][ni][nj] = current_time + 5
                    queue.append((level, ni, nj))
        
        if level < h - 1 and levels[level + 1][i][j] != 'o':
            if visited[level + 1][i][j] == -1:
                visited[level + 1][i][j] = current_time + 5
                queue.append((level + 1, i, j))
    
    print(visited[end_level][end_i][end_j])

if __name__ == "__main__":
    main()
