
k, m, n = map(int, input().split())
if n <= k:
    result = 2 * m
elif n * 2 % k == 0:
    result = (n * 2 // k) * m
else:
    result = (n * 2 // k + 1) * m
print(result)
