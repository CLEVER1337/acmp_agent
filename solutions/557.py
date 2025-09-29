
import sys

def main():
    data = sys.stdin.read().splitlines()
    m, n = map(int, data[0].split())
    a, b = map(int, data[1].split())
    p = int(data[2])
    
    matrices = []
    index = 3
    for _ in range(m):
        matrix = []
        for i in range(n):
            row = list(map(int, data[index].split()))
            matrix.append(row)
            index += 1
        matrices.append(matrix)
        index += 1
    
    result_vector = [0] * n
    result_vector[b - 1] = 1
    
    for i in range(m - 1, -1, -1):
        current_matrix = matrices[i]
        new_vector = [0] * n
        for col in range(n):
            total = 0
            for row in range(n):
                total = (total + result_vector[row] * current_matrix[row][col]) % p
            new_vector[col] = total
        result_vector = new_vector
    
    print(result_vector[a - 1])

if __name__ == "__main__":
    main()
