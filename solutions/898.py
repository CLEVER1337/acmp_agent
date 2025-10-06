n = int(input().strip())
folds = input().strip()
k_data = list(map(int, input().split()))
k = k_data[0]
edges = k_data[1:1+k]

result = []
for edge in edges:
    pos = edge - 1
    l = 0
    r = (1 << n) - 1
    direction = 0
    
    for i in range(n):
        mid = (l + r) // 2
        if pos <= mid:
            r = mid
            if folds[i] == 'P':
                direction ^= 0
            else:
                direction ^= 1
        else:
            l = mid + 1
            if folds[i] == 'P':
                direction ^= 1
            else:
                direction ^= 0
    
    result.append('K' if direction == 0 else 'O')

print(''.join(result))