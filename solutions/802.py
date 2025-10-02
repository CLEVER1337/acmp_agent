
def generate_magic_square(n):
    if n % 2 == 1:
        return generate_odd_magic_square(n)
    elif n % 4 == 0:
        return generate_doubly_even_magic_square(n)
    else:
        return generate_singly_even_magic_square(n)

def generate_odd_magic_square(n):
    square = [[0] * n for _ in range(n)]
    i, j = 0, n // 2
    
    for num in range(1, n * n + 1):
        square[i][j] = num
        next_i = (i - 1) % n
        next_j = (j + 1) % n
        
        if square[next_i][next_j] == 0:
            i, j = next_i, next_j
        else:
            i = (i + 1) % n
    
    return square

def generate_doubly_even_magic_square(n):
    square = [[0] * n for _ in range(n)]
    num = 1
    
    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i % 4) + (j % 4) == 3):
                square[i][j] = num
            else:
                square[i][j] = n * n - num + 1
            num += 1
    
    return square

def generate_singly_even_magic_square(n):
    k = n // 2
    A = generate_odd_magic_square(k)
    
    square = [[0] * n for _ in range(n)]
    
    for i in range(k):
        for j in range(k):
            square[i][j] = A[i][j]
            square[i][j + k] = A[i][j] + 2 * k * k
            square[i + k][j] = A[i][j] + 3 * k * k
            square[i + k][j + k] = A[i][j] + k * k
    
    m = k // 2
    for i in range(k):
        for j in range(m):
            if i != m or (j != 0 and j != m - 1):
                square[i][j], square[i + k][j] = square[i + k][j], square[i][j]
        
        for j in range(n - m + 1, n):
            square[i][j], square[i + k][j] = square[i + k][j], square[i][j]
    
    square[m][m], square[m + k][m] = square[m + k][m], square[m][m]
    square[m][0], square[m + k][0] = square[m + k][0], square[m][0]
    
    return square

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
    
    if n == 2:
        with open('OUTPUT.TXT', 'w') as f:
            f.write("Impossible")
    else:
        magic_square = generate_magic_square(n)
        with open('OUTPUT.TXT', 'w') as f:
            for row in magic_square:
                f.write(' '.join(map(str, row)) + '\n')

if __name__ == "__main__":
    main()
