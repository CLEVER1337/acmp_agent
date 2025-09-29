
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    rules = {}
    for i in range(1, n + 1):
        line = data[i].split()
        if len(line) < 2:
            continue
        pattern = line[0]
        if len(pattern) == 2:
            c1, c2 = pattern[0], pattern[1]
            rules[(c1, c2)] = True
    
    s = data[n + 1].strip()
    stack = []
    
    for char in s:
        stack.append(char)
        while len(stack) >= 2:
            c2 = stack[-1]
            c1 = stack[-2]
            if (c1, c2) in rules:
                stack.pop()
                stack.pop()
            else:
                break
                
    result = ''.join(stack)
    print(result)

if __name__ == "__main__":
    main()
