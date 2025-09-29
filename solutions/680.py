
n = int(input().strip())
if n == 1:
    print(3)
else:
    a, b = 3, 6
    for i in range(2, n):
        a, b = b, 2 * a + 4 * b
    print(b)
