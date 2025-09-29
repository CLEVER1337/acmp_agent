
def main():
    with open('INPUT.TXT', 'r') as f:
        encrypted = f.readline().strip()
        word = f.readline().strip()
    
    n = len(encrypted)
    m = len(word)
    
    if m > n:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('IMPOSSIBLE')
        return
    
    for shift in range(26):
        decrypted = []
        for char in encrypted:
            new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted.append(new_char)
        decrypted_str = ''.join(decrypted)
        
        if word in decrypted_str:
            with open('OUTPUT.TXT', 'w') as f:
                f.write(decrypted_str)
            return
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('IMPOSSIBLE')

if __name__ == '__main__':
    main()
