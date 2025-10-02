
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
        
    n = int(data[0])
    lines = data[1:1+n]
    text = '\n'.join(lines)
    
    stack = [{}]
    output = []
    i = 0
    n = len(text)
    
    def parse_block():
        nonlocal i
        block_macros = stack[-1].copy()
        content = []
        
        while i < n and text[i] != '}':
            if text[i] == '{':
                i += 1
                sub_content, sub_macros = parse_block()
                content.append(sub_content)
                block_macros.update(sub_macros)
            elif text[i] == '#':
                i += 1
                if i < n and text[i] == '#':
                    i += 1
                    name_start = i
                    while i < n and text[i] != ' ' and text[i] != '\n' and text[i] != '}':
                        i += 1
                    macro_name = text[name_start:i]
                    if i < n and text[i] == ' ':
                        i += 1
                    def_start = i
                    brace_count = 0
                    while i < n and (brace_count > 0 or text[i] != '#'):
                        if text[i] == '{':
                            brace_count += 1
                        elif text[i] == '}':
                            brace_count -= 1
                        i += 1
                    if i < n and text[i] == '#':
                        macro_def = text[def_start:i].strip()
                        i += 1
                        block_macros[macro_name] = macro_def
                    else:
                        i = def_start
                else:
                    name_start = i
                    while i < n and text[i] != ' ' and text[i] != '\n' and text[i] != '}':
                        i += 1
                    macro_name = text[name_start:i]
                    if macro_name in block_macros:
                        content.append(expand_macro(block_macros[macro_name], block_macros))
                    else:
                        content.append('#' + macro_name)
            else:
                content.append(text[i])
                i += 1
        
        if i < n and text[i] == '}':
            i += 1
        
        return ''.join(content), block_macros
    
    def expand_macro(macro_def, macros):
        result = []
        j = 0
        m_len = len(macro_def)
        
        while j < m_len:
            if macro_def[j] == '#':
                j += 1
                if j < m_len and macro_def[j] == '#':
                    j += 1
                    name_start = j
                    while j < m_len and macro_def[j] != ' ' and macro_def[j] != '\n':
                        j += 1
                    macro_name = macro_def[name_start:j]
                    if macro_name in macros:
                        result.append(expand_macro(macros[macro_name], macros))
                    else:
                        result.append('##' + macro_name)
                else:
                    name_start = j
                    while j < m_len and macro_def[j] != ' ' and macro_def[j] != '\n':
                        j += 1
                    macro_name = macro_def[name_start:j]
                    if macro_name in macros:
                        result.append(expand_macro(macros[macro_name], macros))
                    else:
                        result.append('#' + macro_name)
            else:
                result.append(macro_def[j])
                j += 1
        
        return ''.join(result)
    
    result, _ = parse_block()
    print(result)

if __name__ == '__main__':
    main()
