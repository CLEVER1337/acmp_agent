
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, m = map(int, data[0].split())
    grid = []
    start = None
    for i in range(1, n+1):
        line = list(data[i].strip())
        grid.append(line)
        if 'X' in line:
            start = (i-1, line.index('X'))
    
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    visited = [[set() for _ in range(m)] for _ in range(n)]
    
    def trace(r, c, dr, dc):
        while True:
            if not (0 <= r < n and 0 <= c < m):
                break
                
            if (dr, dc) in visited[r][c]:
                break
            visited[r][c].add((dr, dc))
            
            if grid[r][c] == '*':
                break
                
            if grid[r][c] == '.':
                if dr == -1 and dc == -1:
                    grid[r][c] = '/'
                elif dr == -1 and dc == 1:
                    grid[r][c] = '\\'
                elif dr == 1 and dc == -1:
                    grid[r][c] = '\\'
                elif dr == 1 and dc == 1:
                    grid[r][c] = '/'
            elif grid[r][c] == '/':
                if (dr, dc) == (-1, -1):
                    dr, dc = 1, 1
                elif (dr, dc) == (-1, 1):
                    dr, dc = 1, -1
                elif (dr, dc) == (1, -1):
                    dr, dc = -1, 1
                elif (dr, dc) == (1, 1):
                    dr, dc = -1, -1
            elif grid[r][c] == '\\':
                if (dr, dc) == (-1, -1):
                    dr, dc = -1, -1
                elif (dr, dc) == (-1, 1):
                    dr, dc = 1, 1
                elif (dr, dc) == (1, -1):
                    dr, dc = -1, -1
                elif (dr, dc) == (1, 1):
                    dr, dc = 1, 1
            elif grid[r][c] == 'X':
                pass
            
            r += dr
            c += dc
    
    for dr, dc in directions:
        trace(start[0], start[1], dr, dc)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'X':
                if len(visited[i][j]) > 1:
                    grid[i][j] = 'X'
                elif visited[i][j]:
                    if (-1, -1) in visited[i][j] or (1, 1) in visited[i][j]:
                        grid[i][j] = '/'
                    else:
                        grid[i][j] = '\\'
            elif grid[i][j] != '*' and grid[i][j] != '.':
                if len(visited[i][j]) > 1:
                    grid[i][j] = 'X'
    
    for i in range(n):
        print(''.join(grid[i]))

if __name__ == "__main__":
    main()
