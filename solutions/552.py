
n = int(input().strip())
counts = list(map(int, input().split()))
total = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            total += counts[i] * counts[j] * counts[k]
print(total)
