
n = int(input())
arr = list(map(int, input().split()))

max_sum = 0
max_indices = []
current_sum = 0
start_index = 0

for i in range(n):
    current_sum += arr[i]
    
    if abs(current_sum) > abs(max_sum):
        max_sum = current_sum
        max_indices = list(range(start_index, i + 1))
    
    if abs(current_sum) == abs(max_sum) and current_sum != max_sum:
        if len(range(start_index, i + 1)) > len(max_indices):
            max_indices = list(range(start_index, i + 1))
    
    if abs(current_sum) < abs(arr[i]):
        current_sum = arr[i]
        start_index = i

print(len(max_indices))
print(' '.join(map(lambda x: str(x + 1), max_indices)))
