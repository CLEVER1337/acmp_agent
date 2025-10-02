
n, k = map(int, input().split())
if k == 1:
    print(n)
else:
    total = n
    for i in range(2, k + 1):
        rooms_per_side = i + 1
        total += n * (rooms_per_side - 2)
    print(total)
