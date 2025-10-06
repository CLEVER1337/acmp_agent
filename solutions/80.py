
import sys

def main():
    s = sys.stdin.readline().strip()
    if not s:
        print("ERROR")
        return
        
    parts = []
    current = ""
    for char in s:
        if char in '+-*/=':
            if current:
                parts.append(current)
                current = ""
            parts.append(char)
        else:
            current += char
    if current:
        parts.append(current)
        
    if len(parts) < 5 or parts[1] not in '+-*/' or parts[3] != '=':
        print("ERROR")
        return
        
    try:
        a_str, op, b_str, eq, c_str = parts[0], parts[1], parts[2], parts[3], parts[4]
        if len(parts) > 5:
            print("ERROR")
            return
            
        if not a_str or not b_str or not c_str:
            print("ERROR")
            return
            
        if (a_str[0] == '-' and len(a_str) == 1) or (b_str[0] == '-' and len(b_str) == 1) or (c_str[0] == '-' and len(c_str) == 1):
            print("ERROR")
            return
            
        a = int(a_str)
        b = int(b_str)
        c = int(c_str)
        
        if abs(a) > 30000 or abs(b) > 30000 or abs(c) > 30000:
            print("ERROR")
            return
            
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                print("ERROR")
                return
            result = a // b
        else:
            print("ERROR")
            return
            
        if result == c:
            print("YES")
        else:
            print("NO")
            
    except ValueError:
        print("ERROR")
    except:
        print("ERROR")

if __name__ == "__main__":
    main()
