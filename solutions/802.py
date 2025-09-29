
def generate_magic_square(n):
    if n % 2 == 1:
        return generate_odd_magic_square(n)
    elif n % 4 == 0:
        return generate_doubly_even_magic_square(n)
    else:
        return generate_singly_even_magic_square(n)

def generate_odd_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]
    i, j = 0, n // 2
    
    for num in range(1, n * n + 1):
        magic_square[i][j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n
        
        if magic_square[new_i][new_j] != 0:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j
            
    return magic_square

def generate_doubly_even_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]
    num = 1
    
    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i % 4) + (j % 4) == 3):
                magic_square[i][j] = num
            else:
                magic_square[i][j] = n * n - num + 1
            num += 1
            
    return magic_square

def generate_singly_even_magic_square(n):
    k = n // 2
    quarter = generate_odd_magic_square(k)
    
    magic_square = [[0] * n for _ in range(n)]
    
    for i in range(k):
        for j in range(k):
            magic_square[i][j] = quarter[i][j]
            magic_square[i + k][j + k] = quarter[i][j] + k * k
            magic_square[i][j + k] = quarter[i][j] + 2 * k * k
            magic_square[i + k][j] = quarter[i][j] + 3 * k * k
            
    swap_count = k // 2
    for i in range(k):
        for j in range(swap_count):
            if i == k // 2 and j == 0:
                continue
            magic_square[i][j], magic_square[i + k][j] = magic_square[i + k][j], magic_square[i][j]
            
    for i in range(k):
        for j in range(n - swap_count + 1, n):
            magic_square[i][j], magic_square[i + k][j] = magic_square[i + k][j], magic_square[i][j]
            
    magic_square[k // 2][swap_count], magic_square[k // 2 + k][swap_count] = (
        magic_square[k // 2 + k][swap_count], magic_square[k // 2][swap_count]
    )
    
    return magic_square

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    if n <= 0 or n > 1000:
        with open('OUTPUT.TXT', 'w') as f:
            f.write("Impossible")
        return
    
    if n == 2:
        with open('OUTPUT.TXT', 'w') as f:
            f.write("Impossible")
        return
    
    magic_square = generate_magic_square(n)
    
    with open('OUTPUT.TXT', 'w') as f:
        for row in magic_square:
            f.write(' '.join(map(str, row)) + '\n')

if __name__ == "__main__":
    main()
