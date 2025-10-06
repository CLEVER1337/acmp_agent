
def main():
    import sys
    m, n = map(int, sys.stdin.readline().split())
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    grid = [[False] * (n + 2) for _ in range(m + 2)]
    for i in range(m + 2):
        grid[i][0] = True
        grid[i][n + 1] = True
    for j in range(n + 2):
        grid[0][j] = True
        grid[m + 1][j] = True
        
    x, y = 1, 1
    dir_idx = 0
    commands = []
    steps = 0
    
    while True:
        dx, dy = directions[dir_idx]
        nx, ny = x + dx, y + dy
        if not grid[nx][ny]:
            grid[x][y] = True
            steps += 1
            x, y = nx, ny
        else:
            if steps > 0:
                commands.append(('f', steps))
                steps = 0
            dir_idx = (dir_idx + 1) % 4
            dx, dy = directions[dir_idx]
            nx, ny = x + dx, y + dy
            if grid[nx][ny]:
                break
            commands.append('r')
            
    if steps > 0:
        commands.append(('f', steps))
        
    print(len(commands))
    for cmd in commands:
        if isinstance(cmd, tuple):
            print(f"{cmd[0]} {cmd[1]}")
        else:
            print(cmd)

if __name__ == "__main__":
    main()
