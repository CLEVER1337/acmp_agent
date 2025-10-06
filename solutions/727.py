
n = int(input())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

max_vals = [0] * n
max_indices = [0] * n
for j in range(n):
    max_val = -1
    max_idx = -1
    for i in range(n):
        if a[i][j] > max_val:
            max_val = a[i][j]
            max_idx = i
    max_vals[j] = max_val
    max_indices[j] = max_idx

result = [0] * n
used = [False] * n
for i in range(n):
    best_j = -1
    for j in range(n):
        if not used[j] and (best_j == -1 or a[i][j] > a[i][best_j]):
            best_j = j
    result[i] = best_j + 1
    used[best_j] = True

for i in range(n):
    print(result[i], end=' ')
