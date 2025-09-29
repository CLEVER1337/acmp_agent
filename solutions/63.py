
s, p = map(int, input().split())
for x in range(1, s + 1):
    y = s - x
    if x * y == p:
        print(min(x, y), max(x, y))
        break
