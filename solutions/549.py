
p, q = map(int, input().split())
n = 2
result = []
while p > 0:
    p *= n
    a = p // q
    result.append(a)
    p -= a * q
    n += 1
print(n - 2)
for a in result:
    print(a)
