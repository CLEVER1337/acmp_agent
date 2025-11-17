
import collections
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print("No")
        return
        
    n = int(data[0].strip())
    grid = []
    start = None
    end = None
    for i in range(1, 1+n):
        line = data[i].strip()
        grid.append(list(line))
        for j, char in enumerate(line):
            if char == '@':
                start = (i-1, j)
            elif char == 'X':
                end = (i-1, j)
                
    if start is None or end is None:
        print("No")
        return
        
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    visited = [[-1] * n for _ in range(n)]
    parent = [[None] * n for _ in range(n)]
    
    q = collections.deque()
    q.append(start)
    visited[start[0]][start[1]] = 0
    
    found = False
    while q:
        i, j = q.popleft()
        if (i, j) == end:
            found = True
            break
            
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < n:
                if visited[ni][nj] == -1:
                    if grid[ni][nj] == '.' or grid[ni][nj] == 'X':
                        visited[ni][nj] = visited[i][j] + 1
                        parent[ni][nj] = (i, j)
                        q.append((ni, nj))
    
    if not found:
        print("No")
        return
        
    print("Yes")
    path_set = set()
    cur = end
    while cur != start:
        i, j = cur
        if grid[i][j] == '.' or grid[i][j] == 'X':
            path_set.add(cur)
        cur = parent[i][j]
    
    for i in range(n):
        for j in range(n):
            if (i, j) in path_set:
                grid[i][j] = '+'
            elif grid[i][j] == 'X':
                grid[i][j] = '+'
                
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    main()
