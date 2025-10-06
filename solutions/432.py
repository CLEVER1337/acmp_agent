
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
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                count += 1
                stack = [(i, j)]
                grid[i][j] = '.'
                
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '#':
                            grid[nx][ny] = '.'
                            stack.append((nx, ny))
                            
    print(count)

if __name__ == "__main__":
    main()
