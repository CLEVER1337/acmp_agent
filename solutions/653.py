
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    grid = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        index += m
        grid.append(row)
    
    operations = []
    
    target = [[(i)*m + j + 1 for j in range(m)] for i in range(n)]
    
    for col in range(m):
        correct_col = col
        found = False
        for check_col in range(col, m):
            for row in range(n):
                if grid[row][check_col] == target[0][col]:
                    found = True
                    break
            if found:
                if check_col != col:
                    operations.append(('C', col+1, check_col+1))
                    for r in range(n):
                        grid[r][col], grid[r][check_col] = grid[r][check_col], grid[r][col]
                break
    
    for row in range(n):
        correct_row = row
        found = False
        for check_row in range(row, n):
            if grid[check_row][0] == target[row][0]:
                found = True
                if check_row != row:
                    operations.append(('R', row+1, check_row+1))
                    grid[row], grid[check_row] = grid[check_row], grid[row]
                break
    
    print(len(operations))
    for op in operations:
        print(f"{op[0]} {op[1]} {op[2]}")

if __name__ == "__main__":
    main()
