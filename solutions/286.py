
def compare_numbers():
    with open('INPUT.TXT', 'r') as f:
        num1 = f.readline().strip()
        num2 = f.readline().strip()
    
    def parse_number(s):
        if '.' not in s:
            return s, '0'
        parts = s.split('.')
        integer = parts[0]
        fractional = parts[1] if len(parts) > 1 else '0'
        return integer, fractional
    
    int1, frac1 = parse_number(num1)
    int2, frac2 = parse_number(num2)
    
    # Compare integer parts
    if len(int1) != len(int2):
        if len(int1) > len(int2):
            return '>'
        else:
            return '<'
    
    # Compare integer digits
    for i in range(len(int1)):
        if int1[i] != int2[i]:
            if int1[i] > int2[i]:
                return '>'
            else:
                return '<'
    
    # Compare fractional parts
    max_len = max(len(frac1), len(frac2))
    frac1_padded = frac1.ljust(max_len, '0')
    frac2_padded = frac2.ljust(max_len, '0')
    
    for i in range(max_len):
        if frac1_padded[i] != frac2_padded[i]:
            if frac1_padded[i] > frac2_padded[i]:
                return '>'
            else:
                return '<'
    
    return '='

result = compare_numbers()
with open('OUTPUT.TXT', 'w') as f:
    f.write(result)
