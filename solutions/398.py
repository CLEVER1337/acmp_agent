
x = int(input().strip())
count = 0
for a in range(1, x + 1):
    for b in range(a, x + 1):
        rem = x - a - b
        if rem < b:
            continue
        min_c = max(b, (rem + 2) // 3)
        max_c = rem // 2
        if min_c <= max_c:
            count += max_c - min_c + 1
print(count)
