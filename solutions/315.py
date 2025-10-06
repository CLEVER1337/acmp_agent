
def main():
    s = input().strip()
    max_char = max(s) if s else '0'
    if max_char in '0123456789':
        min_base = int(max_char) + 1
    elif 'A' <= max_char <= 'Z':
        min_base = ord(max_char) - ord('A') + 11
    else:
        print(-1)
        return
        
    if min_base < 2:
        min_base = 2
        
    for base in range(min_base, 37):
        valid = True
        for char in s:
            if char in '0123456789':
                digit = int(char)
            elif 'A' <= char <= 'Z':
                digit = ord(char) - ord('A') + 10
            else:
                valid = False
                break
                
            if digit >= base:
                valid = False
                break
                
        if valid:
            print(base)
            return
            
    print(-1)

if __name__ == "__main__":
    main()
