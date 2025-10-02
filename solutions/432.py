
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
    
    count = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def dfs(i, j):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != '#':
            return
        grid[i][j] = '.'
        for dx, dy in directions:
            dfs(i + dx, j + dy)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                count += 1
                dfs(i, j)
                
    print(count)

if __name__ == "__main__":
    main()
