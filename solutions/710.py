
import sys

def evaluate(expr, variables):
    stack = []
    i = 0
    while i < len(expr):
        if expr[i] == ' ':
            i += 1
            continue
            
        if expr[i] == ')':
            args = []
            while stack and stack[-1] != '(':
                args.append(stack.pop())
            stack.pop()  # remove '('
            
            operator = stack.pop()
            if operator == 'AND':
                result = True
                for arg in args:
                    if not arg:
                        result = False
                        break
                stack.append(result)
            elif operator == 'OR':
                result = False
                for arg in args:
                    if arg:
                        result = True
                        break
                stack.append(result)
            elif operator == 'NOT':
                stack.append(not args[0])
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
        elif expr[i] == '(':
            stack.append('(')
            i += 1
        elif expr[i] == ',':
            i += 1
        else:
            var_name = ''
            while i < len(expr) and expr[i].isalpha():
                var_name += expr[i]
                i += 1
            stack.append(variables.get(var_name, False))
    
    return stack[0]

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
        
    expr = data[0].strip()
    n, k = map(int, data[1].split())
    
    results = []
    block_start = 2
    
    for _ in range(n):
        variables = {}
        for i in range(block_start, block_start + k):
            parts = data[i].split('=')
            var_name = parts[0].strip()
            value = parts[1].strip()
            variables[var_name] = (value == 'TRUE')
        
        block_start += k
        result = evaluate(expr, variables)
        results.append('TRUE' if result else 'FALSE')
    
    for res in results:
        print(res)

if __name__ == '__main__':
    main()
