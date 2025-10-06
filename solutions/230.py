
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, m = map(int, data[0].split())
    grid = []
    start = None
    for i in range(1, 1 + n):
        line = data[i].strip()
        grid.append(list(line))
        if 'X' in line:
            j = line.index('X')
            start = (i - 1, j)
    
    if start is None:
        for line in grid:
            print(''.join(line))
        return
        
    directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    visited = [[set() for _ in range(m)] for _ in range(n)]
    
    from collections import deque
    q = deque()
    for idx, (dx, dy) in enumerate(directions):
        q.append((start[0], start[1], idx))
        visited[start[0]][start[1]].add(idx)
    
    while q:
        x, y, d = q.popleft()
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
            
        if grid[nx][ny] == '*':
            continue
            
        if d in visited[nx][ny]:
            continue
            
        visited[nx][ny].add(d)
        
        if grid[nx][ny] == '.':
            if d == 0 or d == 2:
                grid[nx][ny] = '\\'
            else:
                grid[nx][ny] = '/'
        elif grid[nx][ny] == '/':
            if d == 0 or d == 2:
                grid[nx][ny] = 'X'
            else:
                pass
        elif grid[nx][ny] == '\\':
            if d == 1 or d == 3:
                grid[nx][ny] = 'X'
            else:
                pass
        elif grid[nx][ny] == 'X':
            pass
        
        if grid[nx][ny] == 'X':
            new_dirs = []
            if d == 0:
                new_dirs = [3]
            elif d == 1:
                new_dirs = [2]
            elif d == 2:
                new_dirs = [1]
            elif d == 3:
                new_dirs = [0]
            for nd in new_dirs:
                if nd not in visited[nx][ny]:
                    q.append((nx, ny, nd))
                    visited[nx][ny].add(nd)
        elif grid[nx][ny] == '/':
            new_dirs = []
            if d == 0:
                new_dirs = [1]
            elif d == 1:
                new_dirs = [0]
            elif d == 2:
                new_dirs = [3]
            elif d == 3:
                new_dirs = [2]
            for nd in new_dirs:
                if nd not in visited[nx][ny]:
                    q.append((nx, ny, nd))
                    visited[nx][ny].add(nd)
        elif grid[nx][ny] == '\\':
            new_dirs = []
            if d == 0:
                new_dirs = [3]
            elif d == 1:
                new_dirs = [2]
            elif d == 2:
                new_dirs = [1]
            elif d == 3:
                new_dirs = [0]
            for nd in new_dirs:
                if nd not in visited[nx][ny]:
                    q.append((nx, ny, nd))
                    visited[nx][ny].add(nd)
        else:
            q.append((nx, ny, d))
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'X' and (i, j) != start:
                if len(visited[i][j]) == 2:
                    grid[i][j] = 'X'
                elif len(visited[i][j]) == 1:
                    d = next(iter(visited[i][j]))
                    if d == 0 or d == 2:
                        grid[i][j] = '\\'
                    else:
                        grid[i][j] = '/'
    
    for line in grid:
        print(''.join(line))

if __name__ == "__main__":
    main()
