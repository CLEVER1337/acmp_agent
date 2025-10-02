
import re

def main():
    with open("INPUT.TXT", "r") as f:
        s = f.readline().strip()
    
    pattern = r'^(-?\d+)([+\-*/])(-?\d+)=(-?\d+)$'
    match = re.fullmatch(pattern, s)
    
    if not match:
        print("ERROR")
        return
        
    num1_str, op, num2_str, result_str = match.groups()
    
    try:
        num1 = int(num1_str)
        num2 = int(num2_str)
        result = int(result_str)
    except ValueError:
        print("ERROR")
        return
        
    if op == '/' and num2 == 0:
        print("ERROR")
        return
        
    if op == '+':
        calc_result = num1 + num2
    elif op == '-':
        calc_result = num1 - num2
    elif op == '*':
        calc_result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("ERROR")
            return
        calc_result = num1 // num2
        
    if calc_result == result:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
