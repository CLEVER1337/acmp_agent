
def main():
    n = int(input().strip())
    if n == 1:
        print(1)
        return
    if n == 2:
        print("Impossible")
        return
        
    grid = [[0] * n for _ in range(n)]
    
    if n % 2 == 1:
        i, j = 0, n // 2
        num = 1
        while num <= n * n:
            grid[i][j] = num
            num += 1
            ni, nj = (i - 1) % n, (j + 1) % n
            if grid[ni][nj] != 0:
                ni, nj = (i + 1) % n, j
            i, j = ni, nj
    else:
        if n % 4 == 0:
            for i in range(n):
                for j in range(n):
                    if (i % 4 == 0 or i % 4 == 3) and (j % 4 == 0 or j % 4 == 3):
                        grid[i][j] = i * n + j + 1
                    elif (i % 4 == 1 or i % 4 == 2) and (j % 4 == 1 or j % 4 == 2):
                        grid[i][j] = i * n + j + 1
                    else:
                        grid[i][j] = n * n - (i * n + j)
        else:
            k = n // 2
            subgrid = [[0] * k for _ in range(k)]
            i, j = 0, k // 2
            num = 1
            while num <= k * k:
                subgrid[i][j] = num
                num += 1
                ni, nj = (i - 1) % k, (j + 1) % k
                if subgrid[ni][nj] != 0:
                    ni, nj = (i + 1) % k, j
                i, j = ni, nj
            
            for i in range(k):
                for j in range(k):
                    val = subgrid[i][j]
                    grid[i][j] = val
                    grid[i + k][j + k] = val + k * k
                    grid[i][j + k] = val + 2 * k * k
                    grid[i + k][j] = val + 3 * k * k
            
            m = k // 2
            for i in range(k):
                for j in range(m):
                    if i != m:
                        grid[i][j], grid[i + k][j] = grid[i + k][j], grid[i][j]
                    else:
                        grid[i][j + m], grid[i + k][j + m] = grid[i + k][j + m], grid[i][j + m]
            
            for i in range(k):
                for j in range(k - m + 1, k):
                    grid[i][j], grid[i + k][j] = grid[i + k][j], grid[i][j]
    
    for row in grid:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    main()
