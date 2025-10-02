
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    n = int(data[0])
    m = int(data[1])
    grid = []
    index = 2
    
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        grid.append(row)
        index += m
    
    total_length = 0.0
    
    # Проверяем соседей по горизонтали
    for i in range(n):
        for j in range(m - 1):
            if grid[i][j] != grid[i][j + 1]:
                total_length += 1
    
    # Проверяем соседей по вертикали
    for i in range(n - 1):
        for j in range(m):
            if grid[i][j] != grid[i + 1][j]:
                total_length += 1
    
    wall_thickness = 0.2  # 20 см
    wall_height = 3.0     # 3 метра
    
    volume = total_length * wall_thickness * wall_height
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("{:.3f}".format(volume))

if __name__ == "__main__":
    main()
