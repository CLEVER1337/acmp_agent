
n, m = map(int, input().split())
total = 0
for i in range(1, m):
    total += (n % i) - (n // i) * i
print(total)
