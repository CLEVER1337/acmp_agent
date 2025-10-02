
def matrix_mult(A, B, mod):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % mod,
         (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % mod],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % mod,
         (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % mod]
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
        data = f.read().split()
        if len(data) < 2:
            return
        N = int(data[0])
        M = int(data[1])
    
    if N == 0:
        result = 0
    elif N == 1:
        result = 1 % M
    else:
        T = [[1, 1], [1, 0]]
        T_pow = matrix_pow(T, N - 1, M)
        result = T_pow[0][0] % M
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
