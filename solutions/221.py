
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
    
    if not start or not end:
        print(-1)
        return
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[[[False] * (K + 1) for _ in range(4)] for _ in range(M)] for _ in range(N)]
    
    queue = deque()
    queue.append((start[0], start[1], 0, 0, 0))
    visited[start[0]][start[1]][0][0] = True
    
    while queue:
        x, y, dir_idx, turns, time = queue.popleft()
        
        if (x, y) == end:
            print(time)
            return
        
        for i in range(4):
            dx, dy = directions[i]
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != 1:
                new_turns = turns
                if i != dir_idx:
                    diff = (i - dir_idx) % 4
                    if diff == 1:
                        new_turns += 1
                    elif diff == 3:
                        continue
                
                if new_turns <= K and not visited[nx][ny][i][new_turns]:
                    visited[nx][ny][i][new_turns] = True
                    queue.append((nx, ny, i, new_turns, time + 1))
    
    print(-1)

if __name__ == "__main__":
    main()
