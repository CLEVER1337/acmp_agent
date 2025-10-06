
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
    
    row_max = [max(row) for row in matrix]
    max_val = max(row_max)
    max_row_index = row_max.index(max_val)
    
    max_col_index = matrix[max_row_index].index(max_val)
    
    candidate_rows = []
    for i in range(n):
        if matrix[i][max_col_index] == max_val:
            candidate_rows.append(i)
    
    best_row = candidate_rows[0]
    for i in range(1, len(candidate_rows)):
        current_row = candidate_rows[i]
        for j in range(m):
            if matrix[current_row][j] > matrix[best_row][j]:
                best_row = current_row
                break
            elif matrix[current_row][j] < matrix[best_row][j]:
                break
    
    candidate_cols = []
    for j in range(m):
        if matrix[best_row][j] == max_val:
            candidate_cols.append(j)
    
    best_col = candidate_cols[0]
    for j in range(1, len(candidate_cols)):
        current_col = candidate_cols[j]
        for i in range(n):
            if matrix[i][current_col] > matrix[i][best_col]:
                best_col = current_col
                break
            elif matrix[i][current_col] < matrix[i][best_col]:
                break
    
    print(matrix[best_row][best_col])

if __name__ == "__main__":
    main()
