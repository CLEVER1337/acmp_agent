
def main():
    with open('INPUT.TXT', 'r') as f:
        a, b = map(int, f.readline().strip().split(':'))
    
    if a < b:
        a, b = b, a
    
    if a <= 25:
        n = a + b - 1
        k = b
        result = comb(n, k)
    else:
        if a - b != 2:
            result = 0
        else:
            result = comb(48, 24) * pow(2, b - 24)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

def comb(n, k):
    if k < 0 or k > n:
        return 0
    res = 1
    for i in range(1, k + 1):
        res = res * (n - k + i) // i
    return res

if __name__ == '__main__':
    main()
