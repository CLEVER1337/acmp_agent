
def product_of_digits(n):
    product = 1
    for digit in str(n):
        if digit == '0':
            return 0
        product *= int(digit)
    return product

def main():
    with open('INPUT.TXT', 'r') as f:
        L, R = map(int, f.readline().split())
    
    count = 0
    for num in range(L, R + 1):
        if num == 0:
            continue
        product = product_of_digits(num)
        if product != 0 and num % product == 0:
            count += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(count))

if __name__ == '__main__':
    main()
