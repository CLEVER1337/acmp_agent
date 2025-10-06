
def main():
    s = input().strip()
    n = len(s)
    base = 27
    num_to_char = {0: ' '}
    for i in range(1, 27):
        num_to_char[i] = chr(ord('a') + i - 1)
    
    prev = 0
    res = []
    for i, char in enumerate(s):
        if '0' <= char <= '9':
            num_val = int(char)
        else:
            num_val = 10 + (ord(char) - ord('A'))
        
        original_val = (num_val - prev) % base
        if original_val < 0:
            original_val += base
        res.append(num_to_char[original_val])
        prev = num_val
    
    print(''.join(res))

if __name__ == '__main__':
    main()
