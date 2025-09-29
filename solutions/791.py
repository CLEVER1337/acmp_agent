
n = int(input())
row = (n - 1) // 8 + 1
col = (n - 1) % 8 + 1
neighbors = []
if row > 1:
    neighbors.append(n - 8)
if row < 8:
    neighbors.append(n + 8)
if col > 1:
    neighbors.append(n - 1)
if col < 8:
    neighbors.append(n + 1)
print(' '.join(map(str, sorted(neighbors))))
