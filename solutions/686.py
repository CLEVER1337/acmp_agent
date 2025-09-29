
n = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(arr)
result = [0] * n

left, right = 0, n - 1
for i in range(n):
    if i % 2 == 0:
        result[left] = sorted_arr[i]
        left += 1
    else:
        result[right] = sorted_arr[i]
        right -= 1

print(' '.join(map(str, result)))
