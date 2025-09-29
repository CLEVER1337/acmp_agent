
def main():
    with open('INPUT.TXT', 'r') as f:
        n, m = map(int, f.readline().split())
        grid = [list(line.strip()) for line in f.readlines()]
    
    # Находим все черные клетки
    black_cells = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                black_cells.append((i, j))
    
    if not black_cells:
        print("CIRCLE")
        return
    
    # Находим границы черной области
    min_i = min(c[0] for c in black_cells)
    max_i = max(c[0] for c in black_cells)
    min_j = min(c[1] for c in black_cells)
    max_j = max(c[1] for c in black_cells)
    
    # Проверяем, что черные клетки образуют прямоугольник с помехами
    # Проверяем наличие внутренней белой области
    has_inner_white = False
    for i in range(min_i + 1, max_i):
        for j in range(min_j + 1, max_j):
            if grid[i][j] == '.':
                has_inner_white = True
                break
        if has_inner_white:
            break
    
    # Если есть внутренняя белая область - это не квадрат
    if has_inner_white:
        print("CIRCLE")
        return
    
    # Проверяем границы на наличие помех
    # Должны быть черные клетки только на границе и рядом с границей
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                # Проверяем, находится ли клетка в допустимой области
                if not ((min_i <= i <= max_i and (j == min_j or j == max_j)) or 
                       (min_j <= j <= max_j and (i == min_i or i == max_i)) or
                       (i == min_i - 1 and min_j <= j <= max_j) or
                       (i == max_i + 1 and min_j <= j <= max_j) or
                       (j == min_j - 1 and min_i <= i <= max_i) or
                       (j == max_j + 1 and min_i <= i <= max_i)):
                    print("CIRCLE")
                    return
    
    print("SQUARE")

if __name__ == "__main__":
    main()
