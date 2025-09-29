
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    matrix = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        index += m
        matrix.append(row)
    
    row_mins = [min(row) for row in matrix]
    
    col_maxes = []
    for j in range(m):
        col_max = -float('inf')
        for i in range(n):
            if matrix[i][j] > col_max:
                col_max = matrix[i][j]
        col_maxes.append(col_max)
    
    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == row_mins[i] and matrix[i][j] == col_maxes[j]:
                count += 1
                
    print(count)

if __name__ == "__main__":
    main()
