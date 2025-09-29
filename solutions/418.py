
def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.read().strip()
    
    max_len = 0
    cur_len = 0
    clipboard = []
    stack = []
    
    i = 0
    n = len(s)
    
    while i < n:
        if s[i] == '\\':
            cur_len = 0
            i += 1
        elif s[i] == '<':
            if i + 1 < n and s[i + 1] == 'c':
                if i + 2 < n and s[i + 2] == 'o':
                    if i + 3 < n and s[i + 3] == 'p':
                        if i + 4 < n and s[i + 4] == 'y':
                            stack.append((cur_len, clipboard[:]))
                            clipboard = []
                            i += 5
                        else:
                            cur_len += 1
                            max_len = max(max_len, cur_len)
                            i += 1
                    else:
                        cur_len += 1
                        max_len = max(max_len, cur_len)
                        i += 1
                else:
                    cur_len += 1
                    max_len = max(max_len, cur_len)
                    i += 1
            elif i + 1 < n and s[i + 1] == 'p':
                if i + 2 < n and s[i + 2] == 'a':
                    if i + 3 < n and s[i + 3] == 's':
                        if i + 4 < n and s[i + 4] == 't':
                            if i + 5 < n and s[i + 5] == 'e':
                                if stack:
                                    cur_len, prev_clipboard = stack.pop()
                                    clipboard = prev_clipboard[:]
                                    for char in clipboard:
                                        cur_len += 1
                                        max_len = max(max_len, cur_len)
                                i += 6
                            else:
                                cur_len += 1
                                max_len = max(max_len, cur_len)
                                i += 1
                        else:
                            cur_len += 1
                            max_len = max(max_len, cur_len)
                            i += 1
                    else:
                        cur_len += 1
                        max_len = max(max_len, cur_len)
                        i += 1
                else:
                    cur_len += 1
                    max_len = max(max_len, cur_len)
                    i += 1
            elif i + 1 < n and s[i + 1] == 'u':
                if i + 2 < n and s[i + 2] == 'n':
                    if i + 3 < n and s[i + 3] == 'd':
                        if i + 4 < n and s[i + 4] == 'o':
                            if stack:
                                cur_len, prev_clipboard = stack.pop()
                                clipboard = prev_clipboard[:]
                            i += 5
                        else:
                            cur_len += 1
                            max_len = max(max_len, cur_len)
                            i += 1
                    else:
                        cur_len += 1
                        max_len = max(max_len, cur_len)
                        i += 1
                else:
                    cur_len += 1
                    max_len = max(max_len, cur_len)
                    i += 1
            else:
                cur_len += 1
                max_len = max(max_len, cur_len)
                i += 1
        elif s[i] == '^':
            if i + 1 < n and s[i + 1] == 'C':
                clipboard = []
                i += 2
            elif i + 1 < n and s[i + 1] == 'V':
                for char in clipboard:
                    cur_len += 1
                    max_len = max(max_len, cur_len)
                i += 2
            elif i + 1 < n and s[i + 1] == 'X':
                clipboard = []
                cur_len = 0
                max_len = max(max_len, cur_len)
                i += 2
            else:
                cur_len += 1
                max_len = max(max_len, cur_len)
                i += 1
        else:
            if s[i] != '\n' and s[i] != '\r':
                clipboard.append(s[i])
                cur_len += 1
                max_len = max(max_len, cur_len)
            i += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(max_len))

if __name__ == '__main__':
    main()
