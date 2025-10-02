
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
    
    length = 2**26 - 1
    pos = n
    char_code = 97
    
    while pos > 1:
        half = length // 2 + 1
        if pos == half:
            break
        elif pos < half:
            length = half - 1
        else:
            pos = length - pos + 1
            length = half - 1
        char_code += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(chr(char_code))

if __name__ == '__main__':
    main()
