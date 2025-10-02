
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    first_line = data[0].split()
    m = int(first_line[0])
    n_size = int(first_line[1])
    
    second_line = data[1].split()
    a = int(second_line[0]) - 1
    b = int(second_line[1]) - 1
    
    p = int(data[2])
    
    matrices = []
    line_index = 3
    
    for _ in range(m):
        while line_index < len(data) and data[line_index].strip() == '':
            line_index += 1
        
        matrix = []
        for i in range(n_size):
            if line_index >= len(data):
                break
            row = list(map(int, data[line_index].split()))
            matrix.append(row)
            line_index += 1
        
        if matrix:
            matrices.append(matrix)
    
    if not matrices:
        print(0)
        return
    
    result_vector = [0] * n_size
    result_vector[a] = 1
    
    for matrix in matrices:
        new_vector = [0] * n_size
        for j in range(n_size):
            total = 0
            for i in range(n_size):
                total = (total + result_vector[i] * matrix[i][j]) % p
            new_vector[j] = total
        result_vector = new_vector
    
    print(result_vector[b])

if __name__ == "__main__":
    main()
