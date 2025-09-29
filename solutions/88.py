
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        size = n * n
        grid = []
        for _ in range(size):
            row = list(map(int, f.readline().split()))
            grid.append(row)
    
    # Проверяем все строки
    for i in range(size):
        if sorted(grid[i]) != list(range(1, size + 1)):
            with open('OUTPUT.TXT', 'w') as f:
                f.write('Incorrect')
            return
    
    # Проверяем все столбцы
    for j in range(size):
        column = [grid[i][j] for i in range(size)]
        if sorted(column) != list(range(1, size + 1)):
            with open('OUTPUT.TXT', 'w') as f:
                f.write('Incorrect')
            return
    
    # Проверяем все средние квадраты
    for box_row in range(n):
        for box_col in range(n):
            box_numbers = []
            start_row = box_row * n
            start_col = box_col * n
            for i in range(start_row, start_row + n):
                for j in range(start_col, start_col + n):
                    box_numbers.append(grid[i][j])
            if sorted(box_numbers) != list(range(1, size + 1)):
                with open('OUTPUT.TXT', 'w') as f:
                    f.write('Incorrect')
                return
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('Correct')

if __name__ == '__main__':
    main()
