
def compare_numbers():
    with open('INPUT.TXT', 'r') as f:
        num1 = f.readline().strip()
        num2 = f.readline().strip()
    
    def parse_number(s):
        if '.' not in s:
            return int(s), 0
        parts = s.split('.')
        integer = int(parts[0]) if parts[0] else 0
        fractional = parts[1] if len(parts) > 1 else ''
        return integer, fractional
    
    int1, frac1 = parse_number(num1)
    int2, frac2 = parse_number(num2)
    
    if int1 != int2:
        print('<' if int1 < int2 else '>', end='')
        return
    
    max_len = max(len(frac1), len(frac2))
    frac1_padded = frac1.ljust(max_len, '0')
    frac2_padded = frac2.ljust(max_len, '0')
    
    if frac1_padded == frac2_padded:
        print('=', end='')
    else:
        print('<' if frac1_padded < frac2_padded else '>', end='')

compare_numbers()
