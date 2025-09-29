
def evaluate_expression(tokens):
    stack = []
    for token in tokens:
        if token in ['+', '-', '*']:
            if len(stack) < 2:
                return None
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            stack.append(result)
        else:
            stack.append(int(token))
    return stack[0] if len(stack) == 1 else None

def generate_expressions(numbers, target):
    n = len(numbers)
    if n == 1:
        if numbers[0] == target:
            return [str(numbers[0])]
        return []
    
    results = []
    for i in range(1, n):
        left_nums = numbers[:i]
        right_nums = numbers[i:]
        
        for op in ['+', '-', '*']:
            left_exprs = generate_expressions(left_nums, target)
            if not left_exprs:
                continue
                
            if op == '+':
                right_target = target - evaluate_expression(left_nums)
                right_exprs = generate_expressions(right_nums, right_target)
            elif op == '-':
                right_target = evaluate_expression(left_nums) - target
                right_exprs = generate_expressions(right_nums, right_target)
            elif op == '*':
                if target % evaluate_expression(left_nums) != 0:
                    continue
                right_target = target // evaluate_expression(left_nums)
                right_exprs = generate_expressions(right_nums, right_target)
            
            for left_expr in left_exprs:
                for right_expr in right_exprs:
                    expr = f"{left_expr}{op}{right_expr}"
                    if evaluate_expression(expr.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').split()) == target:
                        results.append(expr)
    
    return results

def main():
    import sys
    data = sys.stdin.read().strip()
    
    if '=' not in data:
        print(-1)
        return
        
    parts = data.split('=')
    if len(parts) != 2:
        print(-1)
        return
        
    target = int(parts[0].strip())
    expression_part = parts[1].strip()
    
    numbers = []
    current_num = ''
    for char in expression_part:
        if char.isdigit():
            current_num += char
        elif current_num:
            numbers.append(int(current_num))
            current_num = ''
    if current_num:
        numbers.append(int(current_num))
    
    results = generate_expressions(numbers, target)
    if results:
        print(f"{target}={results[0]}")
    else:
        print(-1)

if __name__ == "__main__":
    main()
