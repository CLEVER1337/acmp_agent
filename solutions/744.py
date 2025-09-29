
def is_valid(s):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
    return len(stack) == 0

def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
    
    n = len(s)
    if n % 2 != 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('NO')
        return
    
    for i in range(n):
        shifted = s[i:] + s[:i]
        if is_valid(shifted):
            with open('OUTPUT.TXT', 'w') as f:
                f.write('YES')
            return
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('NO')

if __name__ == '__main__':
    main()
