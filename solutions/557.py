
import sys

def main():
    data = sys.stdin.read().splitlines()
    m_n = data[0].split()
    m = int(m_n[0])
    n = int(m_n[1])
    a_b = data[1].split()
    a = int(a_b[0]) - 1
    b = int(a_b[1]) - 1
    p = int(data[2])
    
    matrices = []
    index = 3
    for _ in range(m):
        while index < len(data) and data[index].strip() == '':
            index += 1
        matrix = []
        for i in range(n):
            row = list(map(int, data[index].split()))
            matrix.append(row)
            index += 1
        matrices.append(matrix)
    
    if m == 0:
        print(0)
        return
        
    result_row = [0] * n
    result_row[a] = 1
    
    for matrix in matrices:
        new_row = [0] * n
        for j in range(n):
            total = 0
            for k in range(n):
                total = (total + result_row[k] * matrix[k][j]) % p
            new_row[j] = total
        result_row = new_row
    
    print(result_row[b])

if __name__ == "__main__":
    main()
