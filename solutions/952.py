
n, m = map(int, input().split())

if m > 0 and n == 0:
    print("Impossible")
else:
    min_cost = max(m, n)
    max_cost = max(0, m - n) + n
    print(f"{min_cost} {max_cost}")
