
def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    grid = []
    start_i, start_j = -1, -1
    
    for i in range(1, 1 + n):
        row = list(data[i].strip())
        grid.append(row)
        if 'K' in row:
            start_i = i - 1
            start_j = row.index('K')
    
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
             (1, -2), (1, 2), (2, -1), (2, 1)]
    
    result = [[0] * m for _ in range(n)]
    count = n * m
    
    def is_valid(i, j):
        return 0 <= i < n and 0 <= j < m
    
    def dfs(i, j, step):
        if step == count:
            return True
            
        next_moves = []
        for dx, dy in moves:
            ni, nj = i + dx, j + dy
            if is_valid(ni, nj) and result[ni][nj] == 0:
                degree = 0
                for dx2, dy2 in moves:
                    ni2, nj2 = ni + dx2, nj + dy2
                    if is_valid(ni2, nj2) and result[ni2][nj2] == 0:
                        degree += 1
                next_moves.append((degree, ni, nj))
        
        next_moves.sort()
        
        for _, ni, nj in next_moves:
            result[ni][nj] = step + 1
            if dfs(ni, nj, step + 1):
                return True
            result[ni][nj] = 0
            
        return False
    
    result[start_i][start_j] = 1
    dfs(start_i, start_j, 1)
    
    with open('OUTPUT.TXT', 'w') as f:
        for i in range(n):
            f.write(' '.join(map(str, result[i])) + '\n')

if __name__ == '__main__':
    main()
