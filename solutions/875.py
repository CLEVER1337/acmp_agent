
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, m, k = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(list(data[i].strip()))
    
    for _ in range(k):
        new_grid = [['.' for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                live_neighbors = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni = (i + di) % n
                        nj = (j + dj) % m
                        if grid[ni][nj] == '*':
                            live_neighbors += 1
                
                if grid[i][j] == '*':
                    if live_neighbors == 2 or live_neighbors == 3:
                        new_grid[i][j] = '*'
                    else:
                        new_grid[i][j] = '.'
                else:
                    if live_neighbors == 3:
                        new_grid[i][j] = '*'
                    else:
                        new_grid[i][j] = '.'
        grid = new_grid
    
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    main()
