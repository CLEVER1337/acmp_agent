
a, b = map(int, input().split())

if a == b:
    min_n = (a + 1) // 2
    max_n = a
    print(min_n, max_n)
else:
    min_n = max((a + 1) // 2, (b + 1) // 2, max(a, b) - min(a, b))
    max_n = a + b
    print(min_n, max_n)
