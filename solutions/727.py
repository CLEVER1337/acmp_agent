
n = int(input())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

best = [0] * n
for i in range(n):
    best[i] = max(range(n), key=lambda j: a[i][j])

result = [0] * n
used = [False] * n

for i in range(n):
    max_val = -1
    candidate = -1
    for j in range(n):
        if not used[j] and a[j][best[j]] > max_val:
            max_val = a[j][best[j]]
            candidate = j
    result[candidate] = best[candidate] + 1
    used[best[candidate]] = True

print(' '.join(map(str, result)))
