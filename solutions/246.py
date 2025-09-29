
n = int(input())
arr = list(map(int, input().split()))

target = list(range(1, n+1))
current_pos = {val: idx for idx, val in enumerate(arr)}

length = 0
max_length = 0

for i in range(1, n+1):
    if i == 1 or current_pos[i] > current_pos[i-1]:
        length += 1
    else:
        max_length = max(max_length, length)
        length = 1
max_length = max(max_length, length)

result = n - max_length
print(result)
