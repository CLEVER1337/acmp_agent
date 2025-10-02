
def evaluate_expression(expr, variables):
    stack = []
    i = 0
    while i < len(expr):
        if expr[i] == ' ':
            i += 1
            continue
            
        if expr[i] == '(':
            stack.append('(')
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
        elif expr[i] == ')':
            args = []
            while stack and stack[-1] != '(':
                args.append(stack.pop())
            stack.pop()  # remove '('
            
            if args:
                op = args.pop()
                if op == 'NOT':
                    result = not args[0]
                    stack.append(result)
                elif op == 'AND':
                    result = args[1] and args[0]
                    stack.append(result)
                elif op == 'OR':
                    result = args[1] or args[0]
                    stack.append(result)
            i += 1
        else:
            var_name = ''
            while i < len(expr) and expr[i].isalpha():
                var_name += expr[i]
                i += 1
            if var_name in variables:
                stack.append(variables[var_name])
            else:
                stack.append(False)
    
    return stack[0] if stack else False

def main():
    with open('INPUT.TXT', 'r') as f:
        expr = f.readline().strip()
        n, k = map(int, f.readline().split())
        
        results = []
        for _ in range(n):
            variables = {}
            for _ in range(k):
                line = f.readline().strip()
                if '=' in line:
                    var, val = line.split('=', 1)
                    var = var.strip()
                    val = val.strip()
                    variables[var] = (val == 'TRUE')
            
            result = evaluate_expression(expr, variables)
            results.append('TRUE' if result else 'FALSE')
    
    with open('OUTPUT.TXT', 'w') as f:
        for res in results:
            f.write(res + '\n')

if __name__ == '__main__':
    main()
