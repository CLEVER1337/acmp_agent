
n = int(input())
inversion_table = list(map(int, input().split()))

arr = [0] * n
for i in range(n-1, -1, -1):
    count = inversion_table[i]
    pos = n - 1
    while count > 0 or arr[pos] != 0:
        if arr[pos] == 0:
            count -= 1
        pos -= 1
    arr[pos] = i + 1

print(' '.join(map(str, arr)))
