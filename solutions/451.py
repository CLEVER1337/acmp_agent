
import math
import sys

def main():
    s = sys.stdin.readline().strip()
    if not s:
        print("Error")
        return
        
    try:
        tokens = tokenize(s)
        if tokens is None:
            print("Error")
            return
            
        rpn = shunting_yard(tokens)
        if rpn is None:
            print("Error")
            return
            
        result = evaluate_rpn(rpn)
        if result is None:
            print("Error")
        else:
            print("{:.15g}".format(result).rstrip('0').rstrip('.'))
    except:
        print("Error")

def tokenize(s):
    tokens = []
    i = 0
    n = len(s)
    
    while i < n:
        if s[i].isspace():
            i += 1
            continue
            
        if s[i] in '+-*/()':
            tokens.append(s[i])
            i += 1
            continue
            
        if s[i:i+3].lower() == 'sin':
            tokens.append('sin')
            i += 3
            continue
            
        if s[i:i+3].lower() == 'cos':
            tokens.append('cos')
            i += 3
            continue
            
        if s[i].isdigit() or s[i] == '.':
            j = i
            dot_seen = False
            while j < n and (s[j].isdigit() or s[j] == '.'):
                if s[j] == '.':
                    if dot_seen:
                        return None
                    dot_seen = True
                j += 1
                
            if j > i:
                try:
                    num = float(s[i:j])
                    tokens.append(num)
                    i = j
                    continue
                except:
                    return None
                    
        return None
        
    return tokens

def shunting_yard(tokens):
    output = []
    stack = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, 'sin': 3, 'cos': 3}
    
    for token in tokens:
        if isinstance(token, float):
            output.append(token)
        elif token in ['sin', 'cos']:
            stack.append(token)
        elif token in ['+', '-', '*', '/']:
            while (stack and stack[-1] != '(' and 
                   precedence.get(stack[-1], 0) >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack or stack[-1] != '(':
                return None
            stack.pop()
            if stack and stack[-1] in ['sin', 'cos']:
                output.append(stack.pop())
                
    while stack:
        if stack[-1] == '(':
            return None
        output.append(stack.pop())
        
    return output

def evaluate_rpn(rpn):
    stack = []
    
    for token in rpn:
        if isinstance(token, float):
            stack.append(token)
        elif token in ['sin', 'cos']:
            if len(stack) < 1:
                return None
            a = stack.pop()
            if token == 'sin':
                stack.append(math.sin(a))
            else:
                stack.append(math.cos(a))
        else:
            if len(stack) < 2:
                return None
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if abs(b) < 1e-15:
                    return None
                stack.append(a / b)
                
    if len(stack) != 1:
        return None
        
    return stack[0]

if __name__ == "__main__":
    main()
