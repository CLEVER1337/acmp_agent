
def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
    
    n = len(s)
    stack = []
    tags = []
    i = 0
    
    while i < n:
        if s[i] == '<':
            j = i + 1
            if j < n and s[j] == '/':
                j += 1
                while j < n and s[j] != '>':
                    j += 1
                if j < n:
                    tag = s[i+2:j]
                    if stack and stack[-1] == tag:
                        stack.pop()
                    else:
                        tags.append((i, 'closing', tag))
                    i = j
                else:
                    tags.append((i, 'incomplete'))
            else:
                while j < n and s[j] != '>':
                    j += 1
                if j < n:
                    tag = s[i+1:j]
                    if all(c.isalpha() for c in tag) and tag:
                        stack.append(tag)
                        tags.append((i, 'opening', tag))
                    else:
                        tags.append((i, 'invalid'))
                    i = j
                else:
                    tags.append((i, 'incomplete'))
        i += 1
    
    if not stack and len(tags) > 0:
        for i, typ, *rest in tags:
            if typ == 'invalid':
                if rest:
                    tag = rest[0]
                    if not all(c.isalpha() for c in tag):
                        for j in range(i+1, i+1+len(tag)):
                            if not s[j].isalpha():
                                new_s = s[:j] + 'a' + s[j+1:]
                                if is_valid_xml(new_s):
                                    with open('OUTPUT.TXT', 'w') as f:
                                        f.write(new_s)
                                    return
                else:
                    j = i + 1
                    while j < n and s[j] != '>':
                        j += 1
                    if j < n:
                        tag = s[i+1:j]
                        for k in range(i+1, j):
                            if not s[k].isalpha():
                                new_s = s[:k] + 'a' + s[k+1:]
                                if is_valid_xml(new_s):
                                    with open('OUTPUT.TXT', 'w') as f:
                                        f.write(new_s)
                                    return
        for i in range(n):
            if s[i] not in '<>/' and not s[i].isalpha():
                for c in 'abcdefghijklmnopqrstuvwxyz<>/':
                    new_s = s[:i] + c + s[i+1:]
                    if is_valid_xml(new_s):
                        with open('OUTPUT.TXT', 'w') as f:
                            f.write(new_s)
                        return
    else:
        for i in range(n):
            for c in 'abcdefghijklmnopqrstuvwxyz<>/':
                new_s = s[:i] + c + s[i+1:]
                if is_valid_xml(new_s):
                    with open('OUTPUT.TXT', 'w') as f:
                        f.write(new_s)
                    return

def is_valid_xml(s):
    stack = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '<':
            j = i + 1
            if j >= n:
                return False
            if s[j] == '/':
                j += 1
                if j >= n:
                    return False
                start = j
                while j < n and s[j] != '>':
                    if not s[j].isalpha():
                        return False
                    j += 1
                if j >= n:
                    return False
                tag = s[start:j]
                if not stack or stack[-1] != tag:
                    return False
                stack.pop()
                i = j + 1
            else:
                start = j
                while j < n and s[j] != '>':
                    if not s[j].isalpha():
                        return False
                    j += 1
                if j >= n:
                    return False
                tag = s[start:j]
                if not tag:
                    return False
                stack.append(tag)
                i = j + 1
        else:
            return False
    return len(stack) == 0

if __name__ == '__main__':
    main()
