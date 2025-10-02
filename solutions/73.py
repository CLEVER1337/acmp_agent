
def main():
    with open('INPUT.TXT', 'r') as f:
        encoded = f.readline().strip()
    
    base27_chars = '0123456789ABCDEFGHIJKLMNOPQ'
    char_to_num = {c: i for i, c in enumerate(base27_chars)}
    
    num_to_char = {}
    for i in range(1, 27):
        num_to_char[i] = chr(ord('a') + i - 1)
    num_to_char[27] = ' '
    
    decoded = []
    for i in range(len(encoded)):
        char_code = char_to_num[encoded[i]]
        original_num = (char_code - i) % 27
        if original_num == 0:
            original_num = 27
        decoded.append(num_to_char[original_num])
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(''.join(decoded))

if __name__ == '__main__':
    main()
