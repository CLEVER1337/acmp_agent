
import math
import sys

sys.setrecursionlimit(100000)

def main():
    try:
        with open('INPUT.TXT', 'r') as f:
            s = f.readline().strip()
        if not s:
            with open('OUTPUT.TXT', 'w') as f:
                f.write('Error')
            return
        tokens = tokenize(s)
        parser = Parser(tokens)
        expr = parser.parse_expression()
        if parser.current < len(tokens) and tokens[parser.current] != ')': 
            raise Exception("Unexpected token")
        result = evaluate(expr)
        with open('OUTPUT.TXT', 'w') as f:
            f.write(str(result))
    except Exception as e:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('Error')

def tokenize(s):
    tokens = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] in ' \t':
            i += 1
            continue
        if s[i] in '+-*/()':
            tokens.append(s[i])
            i += 1
        elif s[i].isdigit() or s[i] == '.':
            j = i
            while j < n and (s[j].isdigit() or s[j] == '.'):
                j += 1
            tokens.append(s[i:j])
            i = j
        elif s[i].isalpha():
            j = i
            while j < n and s[j].isalpha():
                j += 1
            token = s[i:j]
            tokens.append(token)
            i = j
        else:
            i += 1
    return tokens

class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def peek(self):
        if self.current < len(self.tokens):
            return self.tokens[self.current]
        return None

    def eat(self, token):
        if self.peek() == token:
            self.current += 1
        else:
            raise Exception("Unexpected token")

    def parse_expression(self):
        return self.parse_add_sub()

    def parse_add_sub(self):
        left = self.parse_mul_div()
        while self.peek() in ('+', '-'):
            op = self.peek()
            self.eat(op)
            right = self.parse_mul_div()
            left = Node('op', op, left, right)
        return left

    def parse_mul_div(self):
        left = self.parse_factor()
        while self.peek() in ('*', '/'):
            op = self.peek()
            self.eat(op)
            right = self.parse_factor()
            left = Node('op', op, left, right)
        return left

    def parse_factor(self):
        if self.peek() == '(':
            self.eat('(')
            expr = self.parse_expression()
            self.eat(')')
            return expr
        elif self.peek() in ('+', '-'):
            op = self.peek()
            self.eat(op)
            if op == '+':
                return self.parse_factor()
            else:
                node = self.parse_factor()
                return Node('op', '-', None, node)
        elif self.peek().isdigit() or self.peek().startswith('.') or (self.peek()[0] == '-' and len(self.peek()) > 1 and self.peek()[1:].isdigit()):
            num = self.peek()
            self.eat(num)
            return Node('num', float(num))
        elif self.peek() in ('sin', 'cos'):
            func = self.peek()
            self.eat(func)
            self.eat('(')
            arg = self.parse_expression()
            self.eat(')')
            return Node('func', func, arg)
        else:
            raise Exception("Unexpected token")

def evaluate(node):
    if node.type == 'num':
        return node.value
    elif node.type == 'op':
        left_val = evaluate(node.left)
        right_val = evaluate(node.right)
        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            return left_val / right_val
    elif node.type == 'func':
        arg = evaluate(node.left)
        if node.value == 'sin':
            return math.sin(arg)
        elif node.value == 'cos':
            return math.cos(arg)

if __name__ == '__main__':
    main()
