
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n = int(data[0])
    lines = data[1:1+n]
    text = '\n'.join(lines)
    
    stack = [{}]
    result = []
    i = 0
    
    while i < len(text):
        if text[i] == '{':
            stack.append(stack[-1].copy())
            result.append('{')
            i += 1
        elif text[i] == '}':
            stack.pop()
            result.append('}')
            i += 1
        elif text[i] == '#':
            if i + 1 < len(text) and text[i+1] == '#':
                i += 2
                name_start = i
                while i < len(text) and text[i] != ' ' and text[i] != '\n':
                    i += 1
                macro_name = text[name_start:i]
                
                if i < len(text) and text[i] == ' ':
                    i += 1
                
                value_start = i
                while i < len(text) and text[i] != '\n':
                    i += 1
                macro_value = text[value_start:i]
                
                stack[-1][macro_name] = macro_value
            else:
                name_start = i + 1
                i += 1
                while i < len(text) and text[i] != ' ' and text[i] != '\n' and text[i] != '}' and text[i] != '{':
                    i += 1
                macro_name = text[name_start:i]
                
                if macro_name in stack[-1]:
                    result.append(stack[-1][macro_name])
                else:
                    result.append('#' + macro_name)
                    
                if i < len(text) and text[i] == ' ':
                    result.append(' ')
                    i += 1
        else:
            result.append(text[i])
            i += 1
    
    output = ''.join(result)
    with open('OUTPUT.TXT', 'w') as f:
        f.write(output)

if __name__ == '__main__':
    main()
