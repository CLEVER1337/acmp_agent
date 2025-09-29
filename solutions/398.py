
x = int(input())
count = 0
for a in range(1, x + 1):
    for b in range(a, x + 1):
        for c in range(b, x + 1):
            d = x - a - b - c
            if d >= c:
                count += 1
print(count)
