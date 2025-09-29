
n = int(input().strip())
if n == 1:
    print(45)
else:
    count = 9 * (10 ** (n - 1))
    first = 10 ** (n - 1)
    last = (10 ** n) - 1
    total = (first + last) * count // 2
    print(total)
