
def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
    
    if not s:
        print(-1)
        return
        
    max_char = max(s)
    if max_char.isdigit():
        min_base = int(max_char) + 1
    elif max_char.isalpha():
        min_base = ord(max_char.upper()) - ord('A') + 11
    else:
        print(-1)
        return
        
    if min_base < 2:
        min_base = 2
        
    for base in range(min_base, 37):
        try:
            int(s, base)
            print(base)
            return
        except ValueError:
            continue
            
    print(-1)

if __name__ == '__main__':
    main()
