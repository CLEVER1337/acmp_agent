
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, m = map(int, data[0].split())
    grid = [list(line.strip()) for line in data[1:1+n]]
    
    black_cells = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                black_cells.append((i, j))
                
    if not black_cells:
        for i in range(n):
            print('.' * m)
        return
        
    min_i = min(c[0] for c in black_cells)
    max_i = max(c[0] for c in black_cells)
    min_j = min(c[1] for c in black_cells)
    max_j = max(c[1] for c in black_cells)
    
    result = [['.' for _ in range(m)] for _ in range(n)]
    
    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            result[i][j] = '*'
            
    for row in result:
        print(''.join(row))

if __name__ == "__main__":
    main()
