
def main():
    with open('INPUT.TXT', 'r') as f:
        lines = f.readlines()
        I, J = map(int, lines[0].split())
        num_str = lines[1].strip()
    
    if num_str == '0':
        with open('OUTPUT.TXT', 'w') as f:
            f.write('0')
        return
    
    n = 0
    for char in num_str:
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
        else:
            digit = ord(char) - ord('A') + 10
        n = n * I + digit
    
    if n == 0:
        result = '0'
    else:
        digits = []
        while n > 0:
            remainder = n % J
            if remainder < 10:
                digits.append(chr(ord('0') + remainder))
            else:
                digits.append(chr(ord('A') + remainder - 10))
            n //= J
        result = ''.join(reversed(digits))
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
