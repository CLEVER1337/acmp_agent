
import sys

def median_expr(a, b, c):
    return f"<{a}{b}{c}>"

def parse_expression(s, variables):
    stack = []
    i = 0
    n = len(s)
    
    while i < n:
        if s[i] == ' ':
            i += 1
            continue
            
        if s[i] == '(':
            stack.append('(')
            i += 1
        elif s[i] == ')':
            expr = []
            while stack and stack[-1] != '(':
                expr.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
            if expr:
                if len(expr) == 1:
                    stack.append(expr[0])
                else:
                    op = expr.pop()
                    if op == '!':
                        operand = expr.pop()
                        stack.append(f"!{operand}")
                    else:
                        right = expr.pop()
                        left = expr.pop()
                        if op == '&':
                            stack.append(f"({left}&{right})")
                        elif op == '|':
                            stack.append(f"({left}|{right})")
            i += 1
        elif s[i] in variables:
            var = s[i]
            stack.append(var)
            i += 1
        elif s[i] == '!':
            stack.append('!')
            i += 1
        elif s[i] == '&':
            stack.append('&')
            i += 1
        elif s[i] == '|':
            stack.append('|')
            i += 1
        else:
            i += 1

    while len(stack) > 1:
        expr = []
        while stack and stack[-1] != '(':
            expr.append(stack.pop())
        if expr:
            if len(expr) == 1:
                stack.append(expr[0])
            else:
                op = expr.pop()
                if op == '!':
                    operand = expr.pop()
                    stack.append(f"!{operand}")
                else:
                    right = expr.pop()
                    left = expr.pop()
                    if op == '&':
                        stack.append(f"({left}&{right})")
                    elif op == '|':
                        stack.append(f"({left}|{right})")
    
    return stack[0] if stack else ""

def to_median(expr):
    if len(expr) == 0:
        return ""
    
    if expr[0] == '!':
        inner = to_median(expr[1:])
        return median_expr(inner, inner, inner)
    
    if expr[0] == '(' and expr[-1] == ')':
        inner = expr[1:-1]
        if '&' in inner or '|' in inner:
            parts = []
            current = ""
            level = 0
            op = None
            for char in inner:
                if char == '(':
                    level += 1
                    current += char
                elif char == ')':
                    level -= 1
                    current += char
                elif level == 0 and (char == '&' or char == '|'):
                    if op is None:
                        op = char
                    parts.append(current)
                    current = ""
                else:
                    current += char
            if current:
                parts.append(current)
            
            if len(parts) == 2 and op:
                left = to_median(parts[0])
                right = to_median(parts[1])
                if op == '&':
                    return median_expr(left, right, "0")
                elif op == '|':
                    return median_expr(left, right, "1")
        return to_median(inner)
    
    if '&' in expr or '|' in expr:
        parts = []
        current = ""
        level = 0
        op = None
        for char in expr:
            if char == '(':
                level += 1
                current += char
            elif char == ')':
                level -= 1
                current += char
            elif level == 0 and (char == '&' or char == '|'):
                if op is None:
                    op = char
                parts.append(current)
                current = ""
            else:
                current += char
        if current:
            parts.append(current)
        
        if len(parts) == 2 and op:
            left = to_median(parts[0])
            right = to_median(parts[1])
            if op == '&':
                return median_expr(left, right, "0")
            elif op == '|':
                return median_expr(left, right, "1")
    
    return expr

def main():
    with open('input.txt', 'r') as f:
        formula = f.readline().strip()
    
    variables = set()
    for char in formula:
        if 'a' <= char <= 'z':
            variables.add(char)
    
    parsed = parse_expression(formula, variables)
    result = to_median(parsed)
    
    with open('output.txt', 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()
