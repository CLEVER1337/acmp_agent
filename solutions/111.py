
k = int(input().strip())

if k <= 2:
    print(0)
else:
    found = False
    for l in range(2, k):
        if k % (l + 1) == 1:
            print(l)
            found = True
            break
    if not found:
        print(0)
