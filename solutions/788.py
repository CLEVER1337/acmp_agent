
n = int(input())
columns = []
for _ in range(n):
    a, b = map(int, input().split())
    columns.append((a, b))

columns.sort(key=lambda x: x[0] + x[1], reverse=True)

dp = 0
for i in range(n):
    a, b = columns[i]
    if i % 2 == 0:
        dp += a
    else:
        dp -= b

print(dp)
