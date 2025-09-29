
n = int(input())
if n == 0:
    print(0)
else:
    k = int(n**0.5)
    if k * k >= n:
        res = 2 * k * (k + 1)
        print(res)
    else:
        k += 1
        res = 2 * k * (k + 1)
        extra = (k * k - n) * 2
        if n > k * (k - 1):
            res -= extra
        else:
            res -= extra + 1
        print(res)
