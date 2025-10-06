
import sys

def parse_expression(s):
    s = s.replace(' ', '')
    tokens = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] in '()&|!':
            tokens.append(s[i])
            i += 1
        elif s[i].isalpha():
            j = i
            while j < n and s[j].isalpha():
                j += 1
            tokens.append(s[i:j])
            i = j
        else:
            i += 1
    return tokens

def shunting_yard(tokens):
    output = []
    stack = []
    precedence = {'!': 3, '&': 2, '|': 1}
    
    for token in tokens:
        if token.isalpha():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(token, 0):
                output.append(stack.pop())
            stack.append(token)
    
    while stack:
        output.append(stack.pop())
    
    return output

def evaluate_rpn(rpn, var_values):
    stack = []
    variables = set()
    for token in rpn:
        if token.isalpha():
            variables.add(token)
    
    var_map = {var: var_values.get(var, 0) for var in variables}
    
    for token in rpn:
        if token.isalpha():
            stack.append(var_map[token])
        elif token == '!':
            a = stack.pop()
            stack.append(1 - a)
        elif token == '&':
            b = stack.pop()
            a = stack.pop()
            stack.append(a & b)
        elif token == '|':
            b = stack.pop()
            a = stack.pop()
            stack.append(a | b)
    return stack[0]

def get_truth_table(formula):
    tokens = parse_expression(formula)
    rpn = shunting_yard(tokens)
    
    variables = set()
    for token in rpn:
        if token.isalpha():
            variables.add(token)
    variables = sorted(variables)
    n = len(variables)
    
    truth_table = {}
    for i in range(1 << n):
        values = {}
        for j, var in enumerate(variables):
            values[var] = (i >> (n - 1 - j)) & 1
        result = evaluate_rpn(rpn, values)
        truth_table[tuple(values[var] for var in variables)] = result
    return truth_table, variables

def is_self_dual(truth_table, variables):
    n = len(variables)
    for inputs, output in truth_table.items():
        complemented_inputs = tuple(1 - x for x in inputs)
        complemented_output = truth_table.get(complemented_inputs)
        if complemented_output is None or complemented_output != 1 - output:
            return False
    return True

def is_monotonic(truth_table, variables):
    n = len(variables)
    for inputs1, output1 in truth_table.items():
        for inputs2, output2 in truth_table.items():
            if all(x <= y for x, y in zip(inputs1, inputs2)) and output1 > output2:
                return False
    return True

def median(x, y, z):
    return (x & y) | (y & z) | (z & x)

def build_median_circuit(truth_table, variables):
    n = len(variables)
    if n == 0:
        return "0" if truth_table[()] == 0 else "1"
    
    def recursive_construction(sub_vars, assignment):
        if len(sub_vars) == 0:
            key = tuple(assignment[var] for var in variables)
            return str(truth_table[key])
        
        var = sub_vars[0]
        rest_vars = sub_vars[1:]
        
        assignment0 = assignment.copy()
        assignment0[var] = 0
        expr0 = recursive_construction(rest_vars, assignment0)
        
        assignment1 = assignment.copy()
        assignment1[var] = 1
        expr1 = recursive_construction(rest_vars, assignment1)
        
        if expr0 == expr1:
            return expr0
        
        return f"<{var}{expr0}{expr1}>"
    
    return recursive_construction(variables, {})

def main():
    with open('INPUT.TXT', 'r') as f:
        formula = f.read().strip()
    
    truth_table, variables = get_truth_table(formula)
    
    if not is_self_dual(truth_table, variables) or not is_monotonic(truth_table, variables):
        with open('OUTPUT.TXT', 'w') as f:
            f.write("")
        return
    
    result = build_median_circuit(truth_table, variables)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
