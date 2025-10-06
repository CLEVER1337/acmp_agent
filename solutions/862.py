
n, m = map(int, input().split())
total = 0
for i in range(1, m):
    total += (n % i)
print(total)
