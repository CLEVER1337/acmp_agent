
def evaluate_polynomial(poly_str, x_val):
    terms = []
    current_term = ''
    for char in poly_str:
        if char in '+-' and current_term:
            terms.append(current_term)
            current_term = char
        else:
            current_term += char
    if current_term:
        terms.append(current_term)
    
    if not terms or terms[0] == '':
        terms = poly_str.split('+')
    
    total = 0
    for term in terms:
        term = term.strip()
        if not term:
            continue
            
        sign = 1
        if term[0] == '-':
            sign = -1
            term = term[1:]
        elif term[0] == '+':
            term = term[1:]
        
        if 'x' in term:
            if '^' in term:
                parts = term.split('x^')
                if parts[0] == '':
                    coeff = 1
                elif parts[0] == '*':
                    coeff = 1
                else:
                    if parts[0].endswith('*'):
                        coeff_str = parts[0][:-1]
                    else:
                        coeff_str = parts[0]
                    coeff = int(coeff_str) if coeff_str else 1
                exponent = int(parts[1])
            else:
                parts = term.split('x')
                if parts[0] == '':
                    coeff = 1
                elif parts[0] == '*':
                    coeff = 1
                else:
                    if parts[0].endswith('*'):
                        coeff_str = parts[0][:-1]
                    else:
                        coeff_str = parts[0]
                    coeff = int(coeff_str) if coeff_str else 1
                exponent = 1
        else:
            coeff = int(term)
            exponent = 0
        
        total += sign * coeff * (x_val ** exponent)
    
    return total

with open('INPUT.TXT', 'r') as f:
    poly_str = f.readline().strip()
    x_val = int(f.readline().strip())

result = evaluate_polynomial(poly_str, x_val)

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
