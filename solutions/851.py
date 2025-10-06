
def main():
    m, n = map(int, input().split())
    res = []
    if m == 0:
        res = ['G'] * n
    elif n == 0:
        res = ['B'] * m
    else:
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
