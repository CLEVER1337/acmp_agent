
n = int(input().strip())
if n == 0:
    print(1)
else:
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 10
    print(b)
