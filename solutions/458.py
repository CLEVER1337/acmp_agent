
import sys

def main():
    with open('INPUT.TXT', 'r', encoding='cp866') as f:
        lines = f.readlines()
    
    H = int(lines[0].strip())
    order = list(map(int, lines[1].strip().split()))
    encoded = lines[2].strip()
    
    n = len(encoded)
    cols = n // H
    if n % H != 0:
        cols += 1
    
    matrix = [[''] * cols for _ in range(H)]
    
    idx = 0
    for row_num in order:
        row_idx = row_num - 1
        for col in range(cols):
            if idx < n:
                matrix[row_idx][col] = encoded[idx]
                idx += 1
    
    result = []
    for col in range(cols):
        for row in range(H):
            if matrix[row][col]:
                result.append(matrix[row][col])
    
    with open('OUTPUT.TXT', 'w', encoding='cp866') as f:
        f.write(''.join(result))

if __name__ == '__main__':
    main()
