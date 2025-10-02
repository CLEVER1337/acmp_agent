
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    rules = {}
    for i in range(1, n + 1):
        parts = data[i].split()
        if len(parts) >= 3 and parts[1] == '→':
            c1, c2 = parts[0][0], parts[0][1]
            rules[c1 + c2] = True
    
    s = data[n + 1].strip()
    stack = []
    
    for char in s:
        stack.append(char)
        while len(stack) >= 2:
            pair = stack[-2] + stack[-1]
            if pair in rules:
                stack.pop()
                stack.pop()
            else:
                break
    
    result = ''.join(stack)
    print(result)

if __name__ == "__main__":
    main()
