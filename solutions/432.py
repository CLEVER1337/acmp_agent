
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(list(data[i].strip()))
    
    def dfs(i, j):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != '#':
            return
        grid[i][j] = '.'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                count += 1
                dfs(i, j)
                
    print(count)

if __name__ == "__main__":
    main()
