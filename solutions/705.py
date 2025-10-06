
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
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    
    if n == 0:
        print(0)
        return
        
    T = [[1, 1], [1, 0]]
    T_n = matrix_pow(T, n, m)
    
    s_n = T_n[0][1] % m
    print(s_n)
    
if __name__ == "__main__":
    main()
