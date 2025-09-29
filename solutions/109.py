
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.readline().strip()
    
    if '/' not in data:
        with open('OUTPUT.TXT', 'w') as f:
            f.write(data)
        return
    
    a, b = map(int, data.split('/'))
    
    if b == 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('')
        return
    
    if a == 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('0')
        return
    
    negative = False
    if a < 0 and b > 0:
        negative = True
        a = -a
    elif a > 0 and b < 0:
        negative = True
        b = -b
    elif a < 0 and b < 0:
        a = -a
        b = -b
    
    integer_part = a // b
    remainder = a % b
    
    if remainder == 0:
        result = str(integer_part)
        if negative:
            result = '-' + result
        with open('OUTPUT.TXT', 'w') as f:
            f.write(result)
        return
    
    result = []
    if negative:
        result.append('-')
    if integer_part != 0:
        result.append(str(integer_part))
    
    remainder *= 10
    fractional_part = []
    remainders = {}
    repeating_start = -1
    
    while remainder != 0:
        if remainder in remainders:
            repeating_start = remainders[remainder]
            break
        
        remainders[remainder] = len(fractional_part)
        digit = remainder // b
        fractional_part.append(str(digit))
        remainder = (remainder % b) * 10
    
    if repeating_start == -1:
        if integer_part == 0:
            result.append('0.')
        else:
            result.append('.')
        result.extend(fractional_part)
    else:
        if integer_part == 0:
            result.append('0.')
        else:
            result.append('.')
        
        non_repeating = fractional_part[:repeating_start]
        repeating = fractional_part[repeating_start:]
        
        result.extend(non_repeating)
        if repeating_start > 0 or non_repeating:
            result.append('(')
            result.extend(repeating)
            result.append(')')
        else:
            result.append('(')
            result.extend(repeating)
            result.append(')')
    
    output = ''.join(result)
    with open('OUTPUT.TXT', 'w') as f:
        f.write(output)

if __name__ == '__main__':
    main()
