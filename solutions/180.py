
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        N = int(data[0])
        K = int(data[1])
    
    if K == 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('YES')
        return
    
    def digit_product(n):
        product = 1
        while n > 0:
            digit = n % 10
            if digit == 0:
                return 0
            product *= digit
            n //= 10
        return product
    
    for num in range(1, min(N + 1, 1000000)):
        if digit_product(num) == K:
            with open('OUTPUT.TXT', 'w') as f:
                f.write('YES')
            return
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('NO')

if __name__ == '__main__':
    main()
