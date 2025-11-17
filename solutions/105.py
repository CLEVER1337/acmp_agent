
import sys
import itertools

# ------------------------------------------------------------
#  tokenisation, tree, evaluation
# ------------------------------------------------------------

class Leaf:
    __slots__ = ('value', 'token_idx', 'start_idx', 'end_idx')
    def __init__(self, value, token_idx):
        self.value = value
        self.token_idx = token_idx
        self.start_idx = token_idx
        self.end_idx = token_idx

class Node:
    __slots__ = ('start_idx', 'end_idx', 'children', 'adj_gaps')
    def __init__(self, start_idx=-1):
        self.start_idx = start_idx
        self.end_idx = None
        self.children = []          # list of Leaf or Node
        self.adj_gaps = []          # gap indices between children (left‑to‑right)

def parse_tokens(s):
    """return (tokens list, gaps list) – gaps[i] = True iff at least one space
       existed between token i and token i+1."""
    tokens = []
    gaps = []
    i = 0
    n = len(s)
    seen_space = False
    while i < n:
        ch = s[i]
        if ch == ' ':
            seen_space = True
            i += 1
            continue
        if ch.isdigit():
            start = i
            while i < n and s[i].isdigit():
                i += 1
            token = s[start:i]
            if tokens:
                gaps.append(seen_space)
            tokens.append(token)
            seen_space = False
            continue
        if ch == '(' or ch == ')':
            if tokens:
                gaps.append(seen_space)
            tokens.append(ch)
            seen_space = False
            i += 1
            continue
        # any other character is impossible according to the statement
        i += 1
    return tokens, gaps

def build_tree(tokens):
    """build the expression tree, return the root Node."""
    root = Node()                     # virtual root for top level
    stack = []                        # stack of currently open Nodes
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t == '(':
            node = Node(start_idx=i)
            stack.append(node)
            i += 1
        elif t == ')':
            node = stack.pop()
            node.end_idx = i
            if stack:
                stack[-1].children.append(node)
            else:
                root.children.append(node)
            i += 1
        else:                         # number
            leaf = Leaf(int(t), i)
            if stack:
                stack[-1].children.append(leaf)
            else:
                root.children.append(leaf)
            i += 1

    # fill adjacency gap lists for every node (post‑order)
    def fill(node):
        if isinstance(node, Leaf):
            return
        # gaps between consecutive children
        node.adj_gaps = [ch.end_idx for ch in node.children[:-1]]
        for ch in node.children:
            fill(ch)

    fill(root)
    return root

def evaluate(node, assign):
    """value of node under given assignment of gaps -> operator."""
    if isinstance(node, Leaf):
        return node.value
    # evaluate children first
    vals = [evaluate(ch, assign) for ch in node.children]
    res = vals[0]
    for idx, gap_idx in enumerate(node.adj_gaps):
        op = assign[gap_idx]
        nxt = vals[idx + 1]
        if op == '+':
            res = res + nxt
        elif op == '-':
            res = res - nxt
        else:          # '*'
            res = res * nxt
    return res

# ------------------------------------------------------------
#  main solving routine
# ------------------------------------------------------------
def solve() -> None:
    data = sys.stdin.read()
    if not data:
        return
    lines = data.splitlines()
    line = lines[0]                 # the whole equation

    left_part, _, right_part = line.partition('=')
    left_part = left_part.strip()
    try:
        target = int(left_part)
    except ValueError:
        print("-1")
        return

    tokens, gaps = parse_tokens(right_part)

    # which gaps are operator places?
    operator_slots = [i for i in range(len(gaps))
                      if gaps[i] and tokens[i] != '(' and tokens[i+1] != ')']

    root = build_tree(tokens)

    # --------------------------------------------------------
    #  no operator places – evaluate once
    # --------------------------------------------------------
    if not operator_slots:
        val = evaluate(root, {})
        if val == target:
            expr = ''.join(tokens)
            print(f"{target}={expr}")
        else:
            print("-1")
        return

    # --------------------------------------------------------
    #  try all assignments
    # --------------------------------------------------------
    found = False
    solution_assign = None
    M = len(operator_slots)

    for ops in itertools.product('+-*', repeat=M):
        assign = dict(zip(operator_slots, ops))
        if evaluate(root, assign) == target:
            found = True
            solution_assign = assign
            break

    if not found:
        print("-1")
        return

    # --------------------------------------------------------
    #  rebuild the whole equality with inserted symbols
    # --------------------------------------------------------
    out_parts = []
    for i, tok in enumerate(tokens):
        out_parts.append(tok)
        if i < len(gaps) and gaps[i] and tokens[i] != '(' and tokens[i+1] != ')':
            # this gap is an operator place
            out_parts.append(solution_assign[i])
    expr = ''.join(out_parts)
    print(f"{target}={expr}")

if __name__ == '__main__':
    solve()
