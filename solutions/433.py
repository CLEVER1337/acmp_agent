
n = int(input())
s = input().strip()

count = 0
prefix_sum = 0
freq = {0: 1}

for char in s:
    if char == 'a':
        prefix_sum += 1
    else:
        prefix_sum -= 1
        
    if prefix_sum in freq:
        count += freq[prefix_sum]
        freq[prefix_sum] += 1
    else:
        freq[prefix_sum] = 1

print(count)
