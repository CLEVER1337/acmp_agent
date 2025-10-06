
def main():
    s = input().strip()
    n = len(s)
    max_len = 0
    current_len = 0
    stack = []
    
    i = 0
    while i < n:
        if s[i] == '\\':
            if i + 1 < n:
                if s[i+1] == 'b':
                    if current_len > 0:
                        current_len -= 1
                    i += 2
                elif s[i+1] == 'i':
                    i += 2
                elif s[i+1] == 's':
                    stack.append(current_len)
                    current_len = 0
                    i += 2
                else:
                    current_len += 1
                    i += 1
            else:
                current_len += 1
                i += 1
        else:
            current_len += 1
            i += 1
        
        if current_len > max_len:
            max_len = current_len
            
    print(max_len)

if __name__ == "__main__":
    main()
