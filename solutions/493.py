
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(list(data[i].strip()))
    
    count = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                valid = True
                # Проверяем соседние клетки
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m:
                        if grid[ni][nj] == '*':
                            valid = False
                            break
                if valid:
                    count += 1
    
    print(count)

if __name__ == "__main__":
    main()
