
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        N = int(data[0])
        K = int(data[1])
    
    if K == 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('YES')
        return
    
    def product_of_digits(n):
        product = 1
        for digit in str(n):
            if digit == '0':
                return 0
            product *= int(digit)
        return product
    
    max_pages_to_check = min(N, 1000000)
    
    for page in range(1, max_pages_to_check + 1):
        if product_of_digits(page) == K:
            with open('OUTPUT.TXT', 'w') as f:
                f.write('YES')
            return
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('NO')

if __name__ == '__main__':
    main()
