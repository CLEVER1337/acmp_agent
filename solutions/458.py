
def main():
    with open('INPUT.TXT', 'r', encoding='cp866') as f:
        H = int(f.readline().strip())
        order = list(map(int, f.readline().split()))
        encoded = f.readline().strip()
    
    n = len(encoded)
    cols = n // H
    if n % H != 0:
        cols += 1
    
    matrix = [[''] * cols for _ in range(H)]
    
    idx = 0
    for col in range(cols):
        for row in range(H):
            if idx < n:
                matrix[row][col] = encoded[idx]
                idx += 1
    
    original_order = sorted(range(1, H+1), key=lambda x: order.index(x))
    
    result = []
    for col in range(cols):
        for row_idx in original_order:
            char = matrix[row_idx-1][col]
            if char:
                result.append(char)
    
    with open('OUTPUT.TXT', 'w', encoding='cp866') as f:
        f.write(''.join(result))

if __name__ == '__main__':
    main()
