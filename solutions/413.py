
def main():
    with open('INPUT.TXT', 'r') as f:
        n, m = map(int, f.readline().split())
        grid = [list(f.readline().strip()) for _ in range(n)]
    
    buildings = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                buildings += 1
                
                # Находим правый нижний угол текущего здания
                right = j
                while right < m and grid[i][right] == '#':
                    right += 1
                right -= 1
                
                bottom = i
                while bottom < n and grid[bottom][j] == '#':
                    bottom += 1
                bottom -= 1
                
                # Очищаем весь прямоугольник здания
                for x in range(i, bottom + 1):
                    for y in range(j, right + 1):
                        grid[x][y] = '.'
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(buildings))

if __name__ == '__main__':
    main()
