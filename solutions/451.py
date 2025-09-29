
import math
import re

def evaluate_expression(expr):
    try:
        # Удаляем пробелы
        expr = expr.replace(' ', '')
        
        # Проверяем на наличие недопустимых символов
        if re.search(r'[^0-9+\-*/().cosin]', expr):
            return "Error"
        
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
        
        # Заменяем функции на их математические эквиваленты
        expr = expr.replace('cos', 'math.cos')
        expr = expr.replace('sin', 'math.sin')
        
        # Обрабатываем случаи с отрицательными числами в начале выражения
        if expr.startswith('-'):
            expr = '0' + expr
        
        # Обрабатываем случаи с отрицательными числами после операторов
        expr = re.sub(r'([+\-*/])-', r'\1(0-', expr)
        
        # Добавляем недостающие закрывающие скобки для отрицательных чисел
        count_open = expr.count('(')
        count_close = expr.count(')')
        expr += ')' * (count_open - count_close)
        
        # Вычисляем выражение
        result = eval(expr)
        
        # Проверяем на деление на ноль
        if math.isinf(result) or math.isnan(result):
            return "Error"
            
        return result
        
    except:
        return "Error"

def main():
    with open('INPUT.TXT', 'r') as f:
        expression = f.readline().strip()
    
    result = evaluate_expression(expression)
    
    with open('OUTPUT.TXT', 'w') as f:
        if result == "Error":
            f.write("Error")
        else:
            f.write(f"{result:.10f}")

if __name__ == "__main__":
    main()
