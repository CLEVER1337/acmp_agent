
n = int(input())
s = input().strip()

count = 0
prefix_sum = 0
prefix_map = {0: 1}

for char in s:
    if char == 'a':
        prefix_sum += 1
    else:
        prefix_sum -= 1
        
    if prefix_sum in prefix_map:
        count += prefix_map[prefix_sum]
        prefix_map[prefix_sum] += 1
    else:
        prefix_map[prefix_sum] = 1

print(count)
