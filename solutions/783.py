
def main():
    with open('INPUT.TXT', 'r') as f:
        grid = [line.strip() for line in f.readlines()]
    
    correct_colors = []
    for i in range(8):
        row = []
        for j in range(8):
            if (i + j) % 2 == 0:
                row.append('W')
            else:
                row.append('B')
        correct_colors.append(row)
    
    errors = 0
    for i in range(8):
        for j in range(8):
            if grid[i][j] != correct_colors[i][j]:
                errors += 1
    
    print(min(errors, 64 - errors))

if __name__ == '__main__':
    main()
