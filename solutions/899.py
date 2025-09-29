
import sys

def is_possible(s):
    stack = []
    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
    return len(stack) == 0

def main():
    data = sys.stdin.read().splitlines()
    results = []
    for line in data:
        if is_possible(line):
            results.append('0')
        else:
            results.append('1')
    print(''.join(results))

if __name__ == "__main__":
    main()
