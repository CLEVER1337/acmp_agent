
def main():
    with open('INPUT.TXT', 'r') as f:
        text = f.read()
    
    in_string = False
    in_comment1 = False
    in_comment2 = False
    in_comment3 = False
    comment_count = 0
    i = 0
    n = len(text)
    
    while i < n:
        if not in_string and not in_comment1 and not in_comment2 and not in_comment3:
            if text[i] == "'":
                in_string = True
                i += 1
                continue
            elif i + 1 < n and text[i:i+2] == '//':
                comment_count += 1
                in_comment1 = True
                i += 2
                continue
            elif text[i] == '{':
                comment_count += 1
                in_comment2 = True
                i += 1
                continue
            elif i + 1 < n and text[i:i+2] == '(*':
                comment_count += 1
                in_comment3 = True
                i += 2
                continue
        
        if in_string:
            if text[i] == "'":
                in_string = False
            i += 1
        elif in_comment1:
            if text[i] == '\n':
                in_comment1 = False
            i += 1
        elif in_comment2:
            if text[i] == '}':
                in_comment2 = False
                i += 1
            else:
                i += 1
        elif in_comment3:
            if i + 1 < n and text[i:i+2] == '*)':
                in_comment3 = False
                i += 2
            else:
                i += 1
        else:
            i += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(comment_count))

if __name__ == '__main__':
    main()
