
def main():
    s = input().strip()
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
                    if tag and all(c.isalpha() for c in tag):
                        tags.append(('close', tag, i, j))
                    i = j
            else:
                while j < n and s[j] != '>':
                    j += 1
                if j < n:
                    tag = s[i+1:j]
                    if tag and all(c.isalpha() for c in tag):
                        tags.append(('open', tag, i, j))
                    i = j
        i += 1

    def is_valid_sequence(tags_list):
        stack = []
        for typ, tag, start, end in tags_list:
            if typ == 'open':
                stack.append(tag)
            else:
                if not stack or stack[-1] != tag:
                    return False
                stack.pop()
        return len(stack) == 0

    candidates = []
    for pos in range(n):
        original_char = s[pos]
        for new_char in ['<', '>', '/', 'a']:
            if new_char == original_char:
                continue
            new_s = s[:pos] + new_char + s[pos+1:]
            if check_xml(new_s):
                candidates.append(new_s)
        if candidates:
            break

    if candidates:
        print(candidates[0])
        return

    for i in range(len(tags)):
        for j in range(i+1, len(tags)):
            temp_tags = tags.copy()
            temp_tags[i], temp_tags[j] = temp_tags[j], temp_tags[i]
            if is_valid_sequence(temp_tags):
                new_s = list(s)
                for idx, (_, _, start, end) in enumerate(temp_tags):
                    if idx == i or idx == j:
                        new_s[start:end+1] = list(tags[idx][1])
                print(''.join(new_s))
                return

    print(s)

def check_xml(s):
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
                if j >= n or j == start:
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
                if j >= n or j == start:
                    return False
                tag = s[start:j]
                stack.append(tag)
                i = j + 1
        else:
            return False
    return len(stack) == 0

if __name__ == '__main__':
    main()
