
n = int(input())
arr = list(map(int, input().split()))

max_sum = 0
current_sum = 0
start = 0
end = -1
best_start = 0
best_end = -1

for i in range(n):
    current_sum += arr[i]
    
    if abs(current_sum) > abs(max_sum):
        max_sum = current_sum
        best_start = start
        best_end = i
    
    if abs(current_sum) == abs(max_sum) and (i - start) > (best_end - best_start):
        best_start = start
        best_end = i
    
    if current_sum == 0 and i > end:
        start = i + 1

if best_end >= best_start:
    length = best_end - best_start + 1
    indices = [str(i + 1) for i in range(best_start, best_end + 1)]
    print(length)
    print(' '.join(indices))
else:
    print("0")
