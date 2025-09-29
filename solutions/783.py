
def main():
    with open('INPUT.TXT', 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    
    correct_pattern1 = []
    correct_pattern2 = []
    
    for i in range(8):
        row1 = []
        row2 = []
        for j in range(8):
            if (i + j) % 2 == 0:
                row1.append('W')
                row2.append('B')
            else:
                row1.append('B')
                row2.append('W')
        correct_pattern1.append(row1)
        correct_pattern2.append(row2)
    
    errors1 = 0
    errors2 = 0
    
    for i in range(8):
        for j in range(8):
            if grid[i][j] != correct_pattern1[i][j]:
                errors1 += 1
            if grid[i][j] != correct_pattern2[i][j]:
                errors2 += 1
    
    min_errors = min(errors1, errors2)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(min_errors))

if __name__ == '__main__':
    main()
