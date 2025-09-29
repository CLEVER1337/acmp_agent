
k = int(input().strip())
n = int((2 * k) ** 0.5)
while n * (n + 1) // 2 > k:
    n -= 1
print(n)
