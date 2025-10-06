
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1+n):
        grid.append(list(data[i].strip()))
    
    empty_cells = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                empty_cells.append((i, j))
    
    min_grid = [row[:] for row in grid]
    max_grid = [row[:] for row in grid]
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '?':
                if i == 0:
                    min_grid[i][j] = 'D'
                    max_grid[i][j] = 'D'
                elif i == n-1:
                    min_grid[i][j] = 'U'
                    max_grid[i][j] = 'U'
                elif j == 0:
                    min_grid[i][j] = 'R'
                    max_grid[i][j] = 'R'
                elif j == m-1:
                    min_grid[i][j] = 'L'
                    max_grid[i][j] = 'L'
                else:
                    min_grid[i][j] = 'R'
                    max_grid[i][j] = 'D'
    
    for row in min_grid:
        print(''.join(row))
    print()
    for row in max_grid:
        print(''.join(row))

if __name__ == "__main__":
    main()
