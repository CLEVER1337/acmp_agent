
m, n = map(int, input().split())
if m == 0:
    print('G' * n)
elif n == 0:
    print('B' * m)
else:
    res = []
    if m > n:
        for i in range(n):
            res.append('B')
            res.append('G')
        res.append('B')
        for i in range(m - n - 1):
            res.append('B')
    else:
        for i in range(m):
            res.append('G')
            res.append('B')
        for i in range(n - m):
            res.append('G')
    print(''.join(res))
