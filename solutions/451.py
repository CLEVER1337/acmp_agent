
import math
import re

def evaluate_expression(expr):
    try:
        # Удаляем пробелы
        expr = expr.replace(' ', '')
        # Проверяем на наличие недопустимых символов
        if re.search(r'[^0-9+\-*/().cossin]', expr):
            return "Error"
        
        # Заменяем функции на их математические эквиваленты
        expr = expr.replace('cos', 'math.cos')
        expr = expr.replace('sin', 'math.sin')
        
        # Проверяем сбалансированность скобок
        stack = []
        for char in expr:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return "Error"
                stack.pop()
        if stack:
            return "Error"
        
        # Вычисляем выражение
        result = eval(expr, {'math': math, '__builtins__': {}})
        return f"{result:.10f}".rstrip('0').rstrip('.') if '.' in f"{result:.10f}" else f"{result}"
    
    except Exception:
        return "Error"

with open('INPUT.TXT', 'r') as f:
    expression = f.readline().strip()

result = evaluate_expression(expression)

with open('OUTPUT.TXT', 'w') as f:
    f.write(result)
