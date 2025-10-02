
n, m = map(int, input().split())

if m > 0 and n == 0:
    print("Impossible")
else:
    min_cost = max(n, m)
    max_cost = n + max(0, m - n)
    print(f"{min_cost} {max_cost}")
