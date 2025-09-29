
n = int(input())
inv = list(map(int, input().split()))

arr = [0] * n
for i in range(n-1, -1, -1):
    count = 0
    for j in range(n-1, -1, -1):
        if arr[j] == 0:
            count += 1
            if count == inv[i] + 1:
                arr[j] = i + 1
                break

print(' '.join(map(str, arr)))
