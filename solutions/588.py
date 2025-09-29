
b = int(input())
if b == 1:
    print(-1)
else:
    n = [0] * b
    n[0] = b - 4
    n[1] = 2
    n[2] = 1
    n[b - 4] = 1
    if b >= 4 and n[0] >= 0 and n[0] < b:
        for digit in n:
            print(digit)
    else:
        print(-1)
