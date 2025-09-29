
def main():
    from collections import deque
    import sys

    def remove_balls(s):
        if len(s) < 3:
            return s
        stack = []
        for ch in s:
            if stack and stack[-1][0] == ch:
                count = stack[-1][1] + 1
                stack.pop()
                stack.append((ch, count))
            else:
                stack.append((ch, 1))
            while len(stack) >= 2 and stack[-1][0] == stack[-2][0]:
                count = stack[-1][1] + stack[-2][1]
                ch1 = stack[-1][0]
                stack.pop()
                stack.pop()
                stack.append((ch1, count))
        result = []
        for ch, cnt in stack:
            if cnt < 3:
                result.extend([ch] * cnt)
            else:
                pass
        return ''.join(result)

    def dfs(state, shots):
        nonlocal best_shots, best_count
        if not state:
            if len(shots) < best_count:
                best_count = len(shots)
                best_shots = shots[:]
            return
        if len(shots) >= best_count:
            return
        n = len(state)
        for pos in range(n + 1):
            for color in colors:
                new_state = state[:pos] + color + state[pos:]
                new_state = remove_balls(new_state)
                shots.append((color, pos))
                dfs(new_state, shots)
                shots.pop()

    data = sys.stdin.read().strip()
    colors = sorted(set(data))
    best_count = float('inf')
    best_shots = []
    dfs(data, [])
    
    output = [str(len(best_shots))]
    for color, pos in best_shots:
        output.append(f"{color}{pos}")
    sys.stdout.write(' '.join(output))

if __name__ == '__main__':
    main()
