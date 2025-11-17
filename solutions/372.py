import sys

def generate(N):
    total_pairs = N // 2
    result = []
    stack = []          # current opening brackets
    s = []              # current characters of the partial expression

    def backtrack(open_used):
        # open_used – number of opening brackets already placed
        if len(s) == N:
            if not stack:               # fully balanced
                result.append(''.join(s))
            return

        # Option 1: open a new pair (if we still have pairs left)
        if open_used < total_pairs:
            # '('
            s.append('(')
            stack.append('(')
            backtrack(open_used + 1)
            s.pop()
            stack.pop()

            # '['
            s.append('[')
            stack.append('[')
            backtrack(open_used + 1)
            s.pop()
            stack.pop()

        # Option 2: close the most recent opened pair
        if stack:
            top = stack[-1]
            s.append(')' if top == '(' else ']')
            stack.pop()
            backtrack(open_used)
            s.pop()
            stack.append(top)   # restore the state for other branches

    backtrack(0)
    return result


def solve():
    data = sys.stdin.read().strip()
    if not data:
        return
    N = int(data)
    # The problem guarantees that N is an even positive integer ≤ 14
    strings = generate(N)
    sys.stdout.write('\n'.join(strings))


if __name__ == '__main__':
    solve()