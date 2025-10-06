
def format_term(coefficient, variable, is_first):
    if coefficient == 0:
        return ""
    sign = ''
    if coefficient > 0:
        if not is_first:
            sign = '+'
    else:
        sign = '-'
        coefficient = -coefficient
        
    if coefficient == 1:
        if variable:
            return f"{sign}{variable}"
        else:
            return f"{sign}1"
    else:
        if variable:
            return f"{sign}{coefficient}{variable}"
        else:
            return f"{sign}{coefficient}"

def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
    a, b, c = map(int, data)
    
    parts = []
    parts.append(format_term(a, '', True))
    parts.append(format_term(b, 'x', len(parts) == 0))
    parts.append(format_term(c, 'y', len(parts) == 0))
    
    result = ''.join(parts)
    
    if result == '':
        result = '0'
    elif result[0] == '+':
        result = result[1:]
        
    with open("OUTPUT.TXT", "w") as f:
        f.write(result)

if __name__ == "__main__":
    main()
