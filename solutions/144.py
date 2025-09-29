
def main():
    with open('INPUT.TXT', 'r') as f:
        a_str = f.readline().strip()
        b = int(f.readline().strip())
    
    result = []
    carry = 0
    
    for digit in reversed(a_str):
        digit_int = int(digit)
        product = digit_int * b + carry
        result.append(str(product % 10))
        carry = product // 10
    
    if carry > 0:
        result.append(str(carry))
    
    product_str = ''.join(reversed(result)).lstrip('0')
    
    if not product_str:
        product_str = '0'
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(product_str)

if __name__ == '__main__':
    main()
