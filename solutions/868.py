
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
                max_i = i
                max_j = j
                break
    
    matrix[0], matrix[max_i] = matrix[max_i], matrix[0]
    
    for j in range(m):
        col = [matrix[i][j] for i in range(n)]
        if j == 0:
            max_col_val = max(col)
            max_col_idx = j
        else:
            current_max = max(col)
            if current_max > max_col_val:
                max_col_val = current_max
                max_col_idx = j
    
    matrix = [list(row) for row in zip(*matrix)]
    matrix[0], matrix[max_col_idx] = matrix[max_col_idx], matrix[0]
    matrix = [list(row) for row in zip(*matrix)]
    
    print(matrix[n-1][m-1])

if __name__ == "__main__":
    main()
