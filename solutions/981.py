
import sys

def parse_expr(s):
    tokens = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == ' ':
            i += 1
            continue
        if s[i] in '()&|!':
            tokens.append(s[i])
            i += 1
        else:
            j = i
            while j < n and s[j].isalpha():
                j += 1
            tokens.append(s[i:j])
            i = j
    return tokens

def shunting_yard(tokens):
    output = []
    stack = []
    precedence = {'!': 3, '&': 2, '|': 1}
    for token in tokens:
        if token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        elif token in precedence:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
        else:
            output.append(token)
    while stack:
        output.append(stack.pop())
    return output

def build_ast(rpn):
    stack = []
    for token in rpn:
        if token == '!':
            operand = stack.pop()
            stack.append(('NOT', operand))
        elif token == '&':
            right = stack.pop()
            left = stack.pop()
            stack.append(('AND', left, right))
        elif token == '|':
            right = stack.pop()
            left = stack.pop()
            stack.append(('OR', left, right))
        else:
            stack.append(('VAR', token))
    return stack[0]

def eval_ast(ast, values):
    if ast[0] == 'VAR':
        return values.get(ast[1], 0)
    elif ast[0] == 'NOT':
        return 1 - eval_ast(ast[1], values)
    elif ast[0] == 'AND':
        return eval_ast(ast[1], values) & eval_ast(ast[2], values)
    elif ast[0] == 'OR':
        return eval_ast(ast[1], values) | eval_ast(ast[2], values)

def get_variables(ast):
    vars_set = set()
    def traverse(node):
        if node[0] == 'VAR':
            vars_set.add(node[1])
        elif node[0] == 'NOT':
            traverse(node[1])
        else:
            traverse(node[1])
            traverse(node[2])
    traverse(ast)
    return sorted(vars_set)

def is_self_dual(ast, vars_list):
    n = len(vars_list)
    for i in range(1 << n):
        values = {}
        for j, var in enumerate(vars_list):
            values[var] = (i >> j) & 1
        dual_values = {var: 1 - values[var] for var in vars_list}
        if eval_ast(ast, values) != eval_ast(ast, dual_values):
            return False
    return True

def is_monotonic(ast, vars_list):
    n = len(vars_list)
    for i in range(1 << n):
        for j in range(n):
            if not (i & (1 << j)):
                continue
            smaller = i & ~(1 << j)
            values_i = {}
            values_smaller = {}
            for k, var in enumerate(vars_list):
                values_i[var] = (i >> k) & 1
                values_smaller[var] = (smaller >> k) & 1
            if eval_ast(ast, values_smaller) > eval_ast(ast, values_i):
                return False
    return True

def median_repr(ast, vars_list):
    n = len(vars_list)
    if n == 0:
        return "0" if eval_ast(ast, {}) == 0 else "1"
    
    truth_table = []
    for i in range(1 << n):
        values = {}
        for j, var in enumerate(vars_list):
            values[var] = (i >> j) & 1
        truth_table.append(eval_ast(ast, values))
    
    def build_median_expr(mask):
        if all(truth_table[i] == 0 for i in mask):
            return "0"
        if all(truth_table[i] == 1 for i in mask):
            return "1"
        
        min_terms = []
        max_terms = []
        for i in mask:
            if truth_table[i] == 1:
                min_terms.append(i)
            else:
                max_terms.append(i)
        
        if len(min_terms) >= len(max_terms):
            if len(min_terms) == 1:
                i = min_terms[0]
                terms = []
                for j, var in enumerate(vars_list):
                    if (i >> j) & 1:
                        terms.append(var)
                    else:
                        terms.append(f"!{var}")
                if len(terms) == 1:
                    return terms[0]
                return f"<{'<'.join(terms)}>"
            else:
                parts = []
                for i in min_terms:
                    sub_mask = [idx for idx in mask if idx != i]
                    parts.append(build_median_expr(sub_mask))
                return f"<{'<'.join(parts)}>"
        else:
            if len(max_terms) == 1:
                i = max_terms[0]
                terms = []
                for j, var in enumerate(vars_list):
                    if (i >> j) & 1:
                        terms.append(f"!{var}")
                    else:
                        terms.append(var)
                if len(terms) == 1:
                    return terms[0]
                return f"<{'<'.join(terms)}>"
            else:
                parts = []
                for i in max_terms:
                    sub_mask = [idx for idx in mask if idx != i]
                    parts.append(build_median_expr(sub_mask))
                return f"<{'<'.join(parts)}>"
    
    full_mask = list(range(1 << n))
    return build_median_expr(full_mask)

def main():
    with open('INPUT.TXT', 'r') as f:
        formula = f.read().strip()
    
    tokens = parse_expr(formula)
    rpn = shunting_yard(tokens)
    ast = build_ast(rpn)
    vars_list = get_variables(ast)
    
    if not is_self_dual(ast, vars_list) or not is_monotonic(ast, vars_list):
        with open('OUTPUT.TXT', 'w') as f:
            f.write("0")
        return
    
    median_expr = median_repr(ast, vars_list)
    with open('OUTPUT.TXT', 'w') as f:
        f.write(median_expr)

if __name__ == '__main__':
    main()
