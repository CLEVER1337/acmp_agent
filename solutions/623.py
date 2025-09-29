
n = int(input())
if n == 0 or n == 1:
    print(1)
else:
    a, b = 1, 1
    for i in range(2, n + 1):
        a, b = b, (a + b) % 10
    print(b)
