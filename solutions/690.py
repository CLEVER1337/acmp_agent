
def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    grid = []
    start = None
    for i in range(1, n + 1):
        row = data[i].strip()
        grid.append(list(row))
        if 'K' in row:
            start = (i - 1, row.index('K'))
    
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
             (1, -2), (1, 2), (2, -1), (2, 1)]
    
    result = [[0] * m for _ in range(n)]
    count = n * m
    
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m
    
    def dfs(x, y, step):
        if step == count:
            return True
        
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and result[nx][ny] == 0:
                result[nx][ny] = step + 1
                if dfs(nx, ny, step + 1):
                    return True
                result[nx][ny] = 0
        
        return False
    
    x0, y0 = start
    result[x0][y0] = 1
    dfs(x0, y0, 1)
    
    for i in range(n):
        print(' '.join(map(str, result[i])))

if __name__ == '__main__':
    main()
