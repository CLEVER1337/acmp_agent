
def evaluate_expression(tokens):
    stack = []
    for token in tokens:
        if token == ')':
            inner_tokens = []
            while stack and stack[-1] != '(':
                inner_tokens.append(stack.pop())
            stack.pop()
            inner_tokens.reverse()
            result = evaluate_no_parentheses(inner_tokens)
            stack.append(result)
        else:
            stack.append(token)
    return evaluate_no_parentheses(stack)

def evaluate_no_parentheses(tokens):
    if not tokens:
        return 0
    result = int(tokens[0])
    for i in range(1, len(tokens), 2):
        op = tokens[i]
        num = int(tokens[i+1])
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
    return result

def solve():
    data = input().strip()
    parts = data.split('=')
    if len(parts) < 2:
        print(-1)
        return
        
    target = int(parts[0].strip())
    expr_str = parts[1].strip()
    
    tokens = []
    i = 0
    n = len(expr_str)
    
    while i < n:
        if expr_str[i] == ' ':
            i += 1
            continue
        if expr_str[i] == '(':
            tokens.append('(')
            i += 1
        elif expr_str[i] == ')':
            tokens.append(')')
            i += 1
        else:
            j = i
            while j < n and expr_str[j].isdigit():
                j += 1
            num = expr_str[i:j]
            tokens.append(num)
            i = j
    
    numbers = [token for token in tokens if token not in ['(', ')']]
    num_count = len(numbers)
    ops_count = num_count - 1
    
    if ops_count == 0:
        if int(numbers[0]) == target:
            print(f"{target}={numbers[0]}")
        else:
            print(-1)
        return
    
    operators = ['+', '-', '*']
    total_combinations = 3 ** ops_count
    
    found_solution = None
    
    for comb in range(total_combinations):
        temp_comb = comb
        ops_list = []
        for _ in range(ops_count):
            ops_list.append(operators[temp_comb % 3])
            temp_comb //= 3
        
        expression_tokens = []
        idx = 0
        for token in tokens:
            if token == '(' or token == ')':
                expression_tokens.append(token)
            else:
                expression_tokens.append(token)
                if idx < len(ops_list):
                    expression_tokens.append(ops_list[idx])
                    idx += 1
        
        try:
            result = evaluate_expression(expression_tokens)
            if result == target:
                output_expr = f"{target}="
                for token in expression_tokens:
                    if token in ['+', '-', '*', '(', ')']:
                        output_expr += token
                    else:
                        output_expr += str(token)
                found_solution = output_expr
                break
        except:
            continue
    
    if found_solution:
        print(found_solution)
    else:
        print(-1)

solve()
