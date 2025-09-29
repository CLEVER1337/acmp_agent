
n = int(input())
for k in range(n // 5 + 1):
    if (n - 5 * k) % 3 == 0:
        a = (n - 5 * k) // 3
        print(k, a)
        break
else:
    print(0, 0)
