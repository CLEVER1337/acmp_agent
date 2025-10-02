
def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.read().strip()
    
    max_len = 0
    current_len = 0
    i = 0
    n = len(s)
    
    while i < n:
        if s[i] == '\\':
            current_len = 0
            i += 1
        elif s[i] == '^':
            if i + 1 < n:
                if s[i+1] == 's':
                    max_len = max(max_len, current_len)
                    i += 2
                elif s[i+1] == 'S':
                    max_len = max(max_len, current_len)
                    current_len = 0
                    i += 2
                elif s[i+1] == '^':
                    current_len += 1
                    max_len = max(max_len, current_len)
                    i += 2
                else:
                    i += 1
            else:
                i += 1
        else:
            current_len += 1
            max_len = max(max_len, current_len)
            i += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(max_len))

if __name__ == '__main__':
    main()
