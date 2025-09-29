
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
    
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    visited = set()
    
    def trace(r, c, dr, dc):
        while 0 <= r < n and 0 <= c < m:
            if (r, c, dr, dc) in visited:
                break
            visited.add((r, c, dr, dc))
            
            if grid[r][c] == '*':
                break
                
            if grid[r][c] == '.':
                if dr == dc:
                    grid[r][c] = '\\'
                else:
                    grid[r][c] = '/'
            elif grid[r][c] == '/':
                if dr == dc:
                    grid[r][c] = 'X'
                else:
                    pass
            elif grid[r][c] == '\\':
                if dr != dc:
                    grid[r][c] = 'X'
                else:
                    pass
            elif grid[r][c] == 'X':
                pass
            
            if grid[r][c] == '*':
                break
                
            next_r = r + dr
            next_c = c + dc
            
            if not (0 <= next_r < n and 0 <= next_c < m):
                break
                
            if grid[next_r][next_c] == '*':
                dr, dc = -dr, -dc
            else:
                r, c = next_r, next_c
    
    for dr, dc in directions:
        trace(start[0], start[1], dr, dc)
    
    grid[start[0]][start[1]] = 'X'
    
    for i in range(n):
        print(''.join(grid[i]))

if __name__ == "__main__":
    main()
