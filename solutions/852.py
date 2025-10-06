
def main():
    s = input().strip()
    n = len(s)
    stack = []
    pos = 0
    candidates = []
    
    def is_valid_tag_name(name):
        if not name:
            return False
        for c in name:
            if not 'a' <= c <= 'z':
                return False
        return True

    def try_fix(i, char):
        temp = list(s)
        temp[i] = char
        return ''.join(temp)

    def check_valid(xml):
        stack = []
        i = 0
        n = len(xml)
        while i < n:
            if xml[i] == '<':
                j = i + 1
                if j >= n:
                    return False
                if xml[j] == '/':
                    j += 1
                    if j >= n:
                        return False
                    end = j
                    while end < n and xml[end] != '>':
                        end += 1
                    if end >= n:
                        return False
                    tag_name = xml[j:end]
                    if not is_valid_tag_name(tag_name):
                        return False
                    if not stack or stack[-1] != tag_name:
                        return False
                    stack.pop()
                    i = end + 1
                else:
                    end = j
                    while end < n and xml[end] != '>':
                        end += 1
                    if end >= n:
                        return False
                    tag_name = xml[j:end]
                    if not is_valid_tag_name(tag_name):
                        return False
                    stack.append(tag_name)
                    i = end + 1
            else:
                return False
        return len(stack) == 0

    for i in range(n):
        original = s[i]
        for replacement in ['<', '>', '/', 'a']:
            if replacement == original:
                continue
            candidate = try_fix(i, replacement)
            if check_valid(candidate):
                candidates.append(candidate)
        if len(candidates) > 0:
            break

    if candidates:
        print(candidates[0])
        return

    print(s)

if __name__ == "__main__":
    main()
