
def matrix_mult(a, b, mod):
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % mod,
         (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % mod],
        [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % mod,
         (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % mod]
    ]

def matrix_pow(matrix, power, mod):
    result = [[1, 0], [0, 1]]
    base = matrix
    
    while power:
        if power & 1:
            result = matrix_mult(result, base, mod)
        base = matrix_mult(base, base, mod)
        power //= 2
    
    return result

def main():
    with open('INPUT.TXT', 'r') as f:
        n, m = map(int, f.read().split())
    
    if n == 0:
        result = 0
    elif n == 1:
        result = 1 % m
    else:
        transform = [[1, 1], [1, 0]]
        powered = matrix_pow(transform, n - 1, m)
        result = powered[0][0]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
