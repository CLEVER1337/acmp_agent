
def evaluate(expr):
    tokens = []
    i = 0
    n = len(expr)
    while i < n:
        if expr[i] in '+-*':
            tokens.append(expr[i])
            i += 1
        elif expr[i] == '(':
            j = i + 1
            balance = 1
            while j < n and balance > 0:
                if expr[j] == '(':
                    balance += 1
                elif expr[j] == ')':
                    balance -= 1
                j += 1
            sub_expr = expr[i+1:j-1]
            tokens.append(evaluate(sub_expr))
            i = j
        else:
            num_str = ''
            while i < n and expr[i].isdigit():
                num_str += expr[i]
                i += 1
            tokens.append(int(num_str))
    
    if not tokens:
        return 0
    
    result = tokens[0]
    for i in range(1, len(tokens), 2):
        op = tokens[i]
        num = tokens[i+1]
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
    
    return result

def solve():
    with open('input.txt', 'r') as f:
        data = f.read().strip()
    
    if not data:
        print(-1)
        return
    
    parts = data.split('=')
    if len(parts) < 2:
        print(-1)
        return
    
    target = int(parts[0].strip())
    expr_part = parts[1].strip()
    
    numbers = []
    current = ''
    in_paren = 0
    for char in expr_part:
        if char == '(':
            in_paren += 1
            if current.strip():
                numbers.append(current.strip())
                current = ''
            current += char
        elif char == ')':
            in_paren -= 1
            current += char
            if in_paren == 0:
                numbers.append(current)
                current = ''
        elif char == ' ' and in_paren == 0:
            if current.strip():
                numbers.append(current.strip())
                current = ''
        else:
            current += char
    
    if current.strip():
        numbers.append(current.strip())
    
    n = len(numbers)
    
    def backtrack(index, current_expr, current_value, last_op=None):
        if index == n:
            if current_value == target:
                return current_expr
            return None
        
        current_num = numbers[index]
        if current_num.startswith('('):
            sub_expr = current_num[1:-1]
            sub_result = evaluate(sub_expr)
            if sub_result is None:
                return None
            num_value = sub_result
            num_str = current_num
        else:
            num_value = int(current_num)
            num_str = current_num
        
        for op in ['+', '-', '*']:
            new_value = current_value
            if op == '+':
                new_value += num_value
            elif op == '-':
                new_value -= num_value
            elif op == '*':
                new_value *= num_value
            
            new_expr = current_expr + op + num_str
            result = backtrack(index + 1, new_expr, new_value, op)
            if result is not None:
                return result
        
        return None
    
    first_num = numbers[0]
    if first_num.startswith('('):
        sub_expr = first_num[1:-1]
        first_value = evaluate(sub_expr)
        if first_value is None:
            print(-1)
            return
        first_str = first_num
    else:
        first_value = int(first_num)
        first_str = first_num
    
    result = backtrack(1, first_str, first_value)
    if result is not None:
        print(f"{target}={result}")
    else:
        print(-1)

if __name__ == '__main__':
    solve()
