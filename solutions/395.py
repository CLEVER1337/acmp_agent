
def product_digits(n):
    product = 1
    for digit in str(n):
        if digit == '0':
            return 0
        product *= int(digit)
    return product

def solve():
    with open('INPUT.TXT', 'r') as f:
        L, R = map(int, f.readline().split())
    
    count = 0
    for num in range(L, R + 1):
        if num == 0:
            continue
        prod = product_digits(num)
        if prod != 0 and num % prod == 0:
            count += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(count))

solve()
