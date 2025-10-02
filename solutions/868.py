
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    matrix = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        index += m
        matrix.append(row)
    
    max_row = max(matrix)
    max_val = max(max_row)
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == max_val:
                target_row = i
                target_col = j
                break
    
    row_sorted = sorted(range(n), key=lambda i: matrix[i][target_col], reverse=True)
    col_sorted = sorted(range(m), key=lambda j: matrix[target_row][j], reverse=True)
    
    sorted_matrix = []
    for i in row_sorted:
        new_row = []
        for j in col_sorted:
            new_row.append(matrix[i][j])
        sorted_matrix.append(new_row)
    
    print(sorted_matrix[-1][-1])

if __name__ == "__main__":
    main()
