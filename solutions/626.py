
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    rules = {}
    for i in range(1, n+1):
        rule_line = data[i].split()
        if len(rule_line) < 2:
            continue
        pattern = rule_line[0]
        if len(pattern) == 2:
            c1, c2 = pattern[0], pattern[1]
            rules[c1] = c2
            rules[c2] = c1
    
    s = data[n+1].strip()
    stack = []
    
    for char in s:
        if stack and char in rules and stack[-1] == rules[char]:
            stack.pop()
        else:
            stack.append(char)
    
    print(''.join(stack))

if __name__ == "__main__":
    main()
