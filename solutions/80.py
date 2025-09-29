
import re

def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
    
    if not s:
        print('ERROR')
        return
        
    pattern = r'^(-?\d+)([+\-*/])(-?\d+)=(-?\d+)$'
    match = re.fullmatch(pattern, s)
    
    if not match:
        print('ERROR')
        return
        
    num1, op, num2, result = match.groups()
    num1 = int(num1)
    num2 = int(num2)
    result = int(result)
    
    if op == '+':
        calc = num1 + num2
    elif op == '-':
        calc = num1 - num2
    elif op == '*':
        calc = num1 * num2
    elif op == '/':
        if num2 == 0:
            print('ERROR')
            return
        calc = num1 // num2
    
    if calc == result:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
