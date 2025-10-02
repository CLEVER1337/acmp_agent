
m, n, i, j, c = map(int, input().split())
total = m * n
if total % 2 == 0:
    print("equal")
else:
    if (i + j) % 2 == c:
        print("white")
    else:
        print("black")
