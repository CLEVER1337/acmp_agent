
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    lines = data[1:1+n]
    
    text = '\n'.join(lines)
    stack = [{}]
    result = []
    i = 0
    
    while i < len(text):
        if text[i] == '{':
            stack.append({})
            result.append('{')
            i += 1
        elif text[i] == '}':
            stack.pop()
            result.append('}')
            i += 1
        elif i + 1 < len(text) and text[i:i+2] == '{{':
            result.append('{')
            i += 2
        elif i + 1 < len(text) and text[i:i+2] == '}}':
            result.append('}')
            i += 2
        elif text[i] == '#':
            j = i + 1
            while j < len(text) and text[j] != '#':
                j += 1
            if j < len(text) and text[j] == '#':
                parts = text[i+1:j].split()
                if len(parts) >= 2 and parts[0] == 'define':
                    macro_name = parts[1]
                    macro_value = ' '.join(parts[2:])
                    stack[-1][macro_name] = macro_value
                i = j + 1
            else:
                result.append(text[i])
                i += 1
        elif text[i] == '$':
            j = i + 1
            while j < len(text) and text[j] != '$':
                j += 1
            if j < len(text) and text[j] == '$':
                macro_name = text[i+1:j]
                for level in range(len(stack)-1, -1, -1):
                    if macro_name in stack[level]:
                        result.append(stack[level][macro_name])
                        break
                else:
                    pass
                i = j + 1
            else:
                result.append(text[i])
                i += 1
        else:
            result.append(text[i])
            i += 1
    
    output = ''.join(result)
    print(output)

if __name__ == "__main__":
    main()
