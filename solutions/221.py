
from collections import deque

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    K = int(data[0])
    N = int(data[1])
    M = int(data[2])
    
    grid = []
    index = 3
    for i in range(N):
        row = list(map(int, data[index:index+M]))
        index += M
        grid.append(row)
    
    start = None
    end = None
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 2:
                start = (i, j)
            elif grid[i][j] == 3:
                end = (i, j)
    
    if not start or not end:
        print(-1)
        return
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[[[False] * (K+1) for _ in range(4)] for _ in range(M)] for _ in range(N)]
    
    queue = deque()
    start_x, start_y = start
    for d in range(4):
        queue.append((start_x, start_y, d, 0, 0))
        visited[start_x][start_y][d][0] = True
    
    while queue:
        x, y, direction, turns, time = queue.popleft()
        
        if (x, y) == end:
            print(time)
            return
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            new_direction = directions.index((dx, dy))
            new_turns = turns
            
            if new_direction != direction:
                if (new_direction - direction) % 4 == 1:
                    new_turns += 1
                elif (new_direction - direction) % 4 == 3:
                    new_turns += 1
            
            if new_turns > K:
                continue
            
            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] != 1 and not visited[nx][ny][new_direction][new_turns]:
                    visited[nx][ny][new_direction][new_turns] = True
                    queue.append((nx, ny, new_direction, new_turns, time + 1))
    
    print(-1)

if __name__ == "__main__":
    main()
