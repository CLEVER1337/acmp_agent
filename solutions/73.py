
def main():
    with open('INPUT.TXT', 'r') as f:
        encoded = f.readline().strip()
    
    base27_digits = "0123456789ABCDEFGHIJKLMNOPQ"
    char_to_num = {d: i for i, d in enumerate(base27_digits)}
    
    decoded_chars = []
    for i, char in enumerate(encoded):
        num_val = char_to_num[char]
        original_num = (num_val - i) % 27
        if original_num == 26:
            decoded_chars.append(' ')
        else:
            decoded_chars.append(chr(original_num + 97))
    
    result = ''.join(decoded_chars)
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()
