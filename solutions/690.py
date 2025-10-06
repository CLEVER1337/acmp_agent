
def main():
    import sys
    sys.setrecursionlimit(1000000)
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    grid = []
    start = None
    for i in range(1, 1 + n):
        line = data[i].strip()
        grid.append(list(line))
        if 'K' in line:
            j = line.index('K')
            start = (i - 1, j)
    
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    total_cells = n * m
    result = [[0] * m for _ in range(n)]
    step = 1
    
    def dfs(x, y):
        nonlocal step
        if step == total_cells:
            return True
            
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and result[nx][ny] == 0:
                result[nx][ny] = step + 1
                step += 1
                if dfs(nx, ny):
                    return True
                step -= 1
                result[nx][ny] = 0
                
        return False
        
    x0, y0 = start
    result[x0][y0] = 1
    dfs(x0, y0)
    
    for i in range(n):
        print(' '.join(map(str, result[i])))
        
if __name__ == '__main__':
    main()
