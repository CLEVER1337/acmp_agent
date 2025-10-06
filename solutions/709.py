
import sys

def evaluate(expr, variables):
    stack = []
    i = 0
    while i < len(expr):
        if expr[i] == ' ':
            i += 1
            continue
            
        if expr[i] == '(':
            stack.append('(')
            i += 1
        elif expr[i] == ')':
            args = []
            while stack and stack[-1] != '(':
                args.append(stack.pop())
            stack.pop()
            
            op = stack.pop()
            if op == 'NOT':
                result = not args[0]
            elif op == 'AND':
                result = args[1] and args[0]
            elif op == 'OR':
                result = args[1] or args[0]
            stack.append(result)
            i += 1
        elif expr[i:i+3] == 'AND':
            stack.append('AND')
            i += 3
        elif expr[i:i+2] == 'OR':
            stack.append('OR')
            i += 2
        elif expr[i:i+3] == 'NOT':
            stack.append('NOT')
            i += 3
        elif expr[i].isalpha():
            j = i
            while j < len(expr) and expr[j].isalpha():
                j += 1
            token = expr[i:j]
            if token in variables:
                stack.append(variables[token])
            else:
                stack.append(token)
            i = j
        else:
            i += 1
            
    return stack[0]

def main():
    data = sys.stdin.read().splitlines()
    expr = data[0].strip()
    n, k = map(int, data[1].split())
    
    blocks = []
    index = 2
    for _ in range(n):
        variables = {}
        for i in range(k):
            parts = data[index].split('=')
            var_name = parts[0].strip()
            value = parts[1].strip()
            variables[var_name] = value == 'TRUE'
            index += 1
        blocks.append(variables)
    
    results = []
    for block in blocks:
        result = evaluate(expr, block)
        results.append('TRUE' if result else 'FALSE')
    
    with open('OUTPUT.TXT', 'w') as f:
        for res in results:
            f.write(res + '\n')

if __name__ == "__main__":
    main()
