
n = int(input().strip())
result = [''] * n
left = 0
right = n - 1
for i in range(n):
    if i % 2 == 0:
        result[left] = 'B' if (left % 2 == 0) else 'R'
        left += 1
    else:
        result[right] = 'B' if (right % 2 == 0) else 'R'
        right -= 1
print(''.join(result))
