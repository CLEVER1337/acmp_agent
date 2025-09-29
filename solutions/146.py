
def main():
    with open('INPUT.TXT', 'r') as f:
        A_str = f.read().strip()
    
    if A_str == '0':
        with open('OUTPUT.TXT', 'w') as f:
            f.write('0')
        return
    
    n = len(A_str)
    if n % 2 == 1:
        current = int(A_str[0])
        start_index = 1
    else:
        current = int(A_str[:2])
        start_index = 2
    
    root_digits = []
    remainder = 0
    
    if start_index == 1:
        x = 0
        while (x + 1) ** 2 <= current:
            x += 1
        root_digits.append(str(x))
        remainder = current - x * x
    else:
        x = 0
        while (x + 1) ** 2 <= current:
            x += 1
        root_digits.append(str(x))
        remainder = current - x * x
    
    for i in range(start_index, n, 2):
        if i + 1 < n:
            chunk = int(A_str[i:i+2])
        else:
            chunk = int(A_str[i]) * 10
        
        temp = remainder * 100 + chunk
        current_root = int(''.join(root_digits))
        
        x = 0
        while (20 * current_root + x) * x <= temp:
            x += 1
        x -= 1
        
        root_digits.append(str(x))
        remainder = temp - (20 * current_root + x) * x
        current_root = current_root * 10 + x
    
    result = ''.join(root_digits).lstrip('0')
    if not result:
        result = '0'
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
