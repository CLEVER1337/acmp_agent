
def evaluate_expression(expr, variables):
    stack = []
    i = 0
    while i < len(expr):
        if expr[i] == '(':
            stack.append('(')
            i += 1
        elif expr[i] == ')':
            args = []
            while stack and stack[-1] != '(':
                args.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
            if args:
                func = args.pop()
                if func == 'AND':
                    result = all(args)
                    stack.append(result)
                elif func == 'OR':
                    result = any(args)
                    stack.append(result)
                elif func == 'NOT':
                    result = not args[0]
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
        elif expr[i:i+4] == 'TRUE':
            stack.append(True)
            i += 4
        elif expr[i:i+5] == 'FALSE':
            stack.append(False)
            i += 5
        elif expr[i].isalpha():
            var_name = ''
            while i < len(expr) and expr[i].isalpha():
                var_name += expr[i]
                i += 1
            if var_name in variables:
                stack.append(variables[var_name])
            else:
                stack.append(False)
        else:
            i += 1
    return stack[0] if stack else False

def main():
    with open('INPUT.TXT', 'r') as f:
        expr = f.readline().strip()
        n, k = map(int, f.readline().split())
        blocks = []
        for _ in range(n):
            block = {}
            for _ in range(k):
                line = f.readline().strip()
                var, value = line.split('=')
                var = var.strip()
                value = value.strip()
                block[var] = (value == 'TRUE')
            blocks.append(block)
    
    results = []
    for block in blocks:
        result = evaluate_expression(expr, block)
        results.append('TRUE' if result else 'FALSE')
    
    with open('OUTPUT.TXT', 'w') as f:
        for res in results:
            f.write(res + '\n')

if __name__ == '__main__':
    main()
