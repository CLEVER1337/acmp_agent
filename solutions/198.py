
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0].strip())
    matrix = []
    for i in range(1, n + 1):
        row = list(map(int, data[i].split()))
        matrix.append(row)
    
    A = []
    B = []
    for row in matrix:
        A.append(row[:-1])
        B.append(row[-1])
    
    for col in range(n):
        pivot_row = col
        for r in range(col + 1, n):
            if abs(A[r][col]) > abs(A[pivot_row][col]):
                pivot_row = r
        
        A[col], A[pivot_row] = A[pivot_row], A[col]
        B[col], B[pivot_row] = B[pivot_row], B[col]
        
        pivot_val = A[col][col]
        for j in range(col, n):
            A[col][j] /= pivot_val
        B[col] /= pivot_val
        
        for i in range(n):
            if i == col:
                continue
            factor = A[i][col]
            for j in range(col, n):
                A[i][j] -= factor * A[col][j]
            B[i] -= factor * B[col]
    
    x = [0] * n
    for i in range(n):
        x[i] = round(B[i])
    
    print(' '.join(map(str, x)))

if __name__ == "__main__":
    main()
