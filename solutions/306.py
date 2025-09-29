
n = int(input())
result = [''] * n
left, right = 0, n - 1
for i in range(n):
    if i % 2 == 0:
        result[left] = 'B' if i % 2 == 0 else 'R'
        left += 1
    else:
        result[right] = 'R' if i % 2 == 1 else 'B'
        right -= 1
print(''.join(result))
