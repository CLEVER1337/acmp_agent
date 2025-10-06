
def main():
    with open('INPUT.TXT', 'r') as f:
        lines = f.read().splitlines()
    
    if len(lines) < 2:
        print('=')
        return
        
    num1 = lines[0].strip()
    num2 = lines[1].strip()
    
    if num1 == num2:
        print('=')
        return
        
    sign1 = 1
    sign2 = 1
    
    if num1.startswith('-'):
        sign1 = -1
        num1 = num1[1:]
    if num2.startswith('-'):
        sign2 = -1
        num2 = num2[1:]
    
    if sign1 != sign2:
        if sign1 < sign2:
            print('<')
        else:
            print('>')
        return
            
    parts1 = num1.split('.', 1)
    parts2 = num2.split('.', 1)
    
    int_part1 = parts1[0]
    int_part2 = parts2[0]
    
    dec_part1 = parts1[1] if len(parts1) > 1 else ''
    dec_part2 = parts2[1] if len(parts2) > 1 else ''
    
    if len(int_part1) != len(int_part2):
        if len(int_part1) > len(int_part2):
            result = '>' if sign1 == 1 else '<'
        else:
            result = '<' if sign1 == 1 else '>'
        print(result)
        return
            
    for i in range(len(int_part1)):
        if int_part1[i] != int_part2[i]:
            if int(int_part1[i]) > int(int_part2[i]):
                result = '>' if sign1 == 1 else '<'
            else:
                result = '<' if sign1 == 1 else '>'
            print(result)
            return
            
    max_dec_len = max(len(dec_part1), len(dec_part2))
    dec_part1 = dec_part1.ljust(max_dec_len, '0')
    dec_part2 = dec_part2.ljust(max_dec_len, '0')
    
    for i in range(max_dec_len):
        if dec_part1[i] != dec_part2[i]:
            if int(dec_part1[i]) > int(dec_part2[i]):
                result = '>' if sign1 == 1 else '<'
            else:
                result = '<' if sign1 == 1 else '>'
            print(result)
            return
            
    print('=')

if __name__ == '__main__':
    main()
