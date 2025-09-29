
n, m = map(int, input().split())
if n == 1 and m == 1:
    print(4)
else:
    result = n * m * 2 + 2
    if n % 2 == 0 or m % 2 == 0:
        result += 2
    print(result * 100)
