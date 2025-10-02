
a, b = map(int, input().split())
if a == b:
    min_n = (a + 1) // 2
    max_n = a
    print(f"{min_n} {max_n}")
else:
    max_n = a + b
    min_n = max((a + 1) // 2, (b + 1) // 2, (a + b + 2) // 3)
    print(f"{min_n} {max_n}")
