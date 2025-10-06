
n = int(input())
arr = list(map(int, input().split()))

max_sum = 0
max_indices = []
current_sum = 0
current_start = 0

for i in range(n):
    current_sum += arr[i]
    
    if abs(current_sum) > abs(max_sum):
        max_sum = current_sum
        max_indices = list(range(current_start, i + 1))
    
    if abs(current_sum) == abs(max_sum) and current_sum != max_sum:
        if len(range(current_start, i + 1)) < len(max_indices):
            max_sum = current_sum
            max_indices = list(range(current_start, i + 1))
    
    if current_sum == 0:
        if len(range(current_start, i + 1)) < len(max_indices) or max_sum == 0:
            max_sum = current_sum
            max_indices = list(range(current_start, i + 1))
    
    if abs(current_sum) < abs(arr[i]):
        current_sum = arr[i]
        current_start = i

print(len(max_indices))
print(' '.join(map(lambda x: str(x + 1), max_indices)))
