
from collections import deque

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    K = int(data[0])
    N = int(data[1])
    M = int(data[2])
    grid = []
    index = 3
    start = None
    end = None
    
    for i in range(N):
        row = list(map(int, data[index:index+M]))
        index += M
        grid.append(row)
        for j in range(M):
            if row[j] == 2:
                start = (i, j)
            elif row[j] == 3:
                end = (i, j)
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = float('inf')
    dist = [[[[INF] * (K+1) for _ in range(4)] for _ in range(M)] for _ in range(N)]
    
    queue = deque()
    for d in range(4):
        dist[start[0]][start[1]][d][0] = 0
        queue.append((start[0], start[1], d, 0))
    
    while queue:
        x, y, dir_idx, turns = queue.popleft()
        current_dist = dist[x][y][dir_idx][turns]
        
        if (x, y) == end:
            continue
            
        dx, dy = directions[dir_idx]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != 1:
            if dist[nx][ny][dir_idx][turns] > current_dist + 1:
                dist[nx][ny][dir_idx][turns] = current_dist + 1
                queue.append((nx, ny, dir_idx, turns))
        
        for new_dir in range(4):
            if new_dir == dir_idx:
                continue
                
            turn_cost = 1
            if (dir_idx + 1) % 4 == new_dir:
                new_turns = turns + 1
            else:
                new_turns = turns
                
            if new_turns <= K:
                if dist[x][y][new_dir][new_turns] > current_dist + turn_cost:
                    dist[x][y][new_dir][new_turns] = current_dist + turn_cost
                    queue.append((x, y, new_dir, new_turns))
    
    result = INF
    for d in range(4):
        for t in range(K+1):
            result = min(result, dist[end[0]][end[1]][d][t])
    
    if result == INF:
        result = -1
        
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
