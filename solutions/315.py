
def main():
    S = input().strip()
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    max_char = max(S.upper())
    min_base = symbols.index(max_char) + 1
    
    if min_base < 2:
        min_base = 2
        
    for base in range(min_base, 37):
        valid = True
        for char in S.upper():
            digit = symbols.find(char)
            if digit == -1 or digit >= base:
                valid = False
                break
        if valid:
            print(base)
            return
            
    print(-1)

if __name__ == "__main__":
    main()
