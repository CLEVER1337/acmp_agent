
def next_lexicographic(n, parts):
    i = len(parts) - 1
    while i >= 0 and parts[i] == n:
        parts[i] = 0
        i -= 1
    if i < 0:
        return [0 for _ in range(len(parts))] + [n + 1]
    else:
        parts[i] += 1
        return parts[:i+1] + [n-sum(parts[:i+1])] + sorted([x - 1 for x in parts[i+1:]])

if __name__ == '__main__':
    with open('INPUT.TXT', 'r') as f:
        lines = f.read().split("\n")
    output = []
    while len(lines) > 0:
        n, k = map(int, lines[0].split())
        parts = list(map(int, lines[1:k+1])) + [0 for _ in range(k)]
        lines = lines[k+1:]
        next_parts = next_lexicographic(n, sorted([x + 1 for x in parts[:-1]]))
        output.append((next_parts[:-1], next_parts[-1]))
    with open('OUTPUT.TXT', 'w') as f:
        for n, k in output:
            f.write(str(n) + "\n")
