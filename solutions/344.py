
n = int(input())
points = list(map(int, input().split()))
indexed_points = [(points[i], i + 1) for i in range(n)]
indexed_points.sort(key=lambda x: x[0])

min_dist = float('inf')
left_idx = -1
right_idx = -1

for i in range(n - 1):
    dist = indexed_points[i + 1][0] - indexed_points[i][0]
    if dist < min_dist:
        min_dist = dist
        left_idx = indexed_points[i][1]
        right_idx = indexed_points[i + 1][1]
    elif dist == min_dist:
        current_left = min(indexed_points[i][1], indexed_points[i + 1][1])
        current_right = max(indexed_points[i][1], indexed_points[i + 1][1])
        existing_left = min(left_idx, right_idx)
        existing_right = max(left_idx, right_idx)
        
        if current_left < existing_left or (current_left == existing_left and current_right < existing_right):
            left_idx = indexed_points[i][1]
            right_idx = indexed_points[i + 1][1]

print(min_dist)
print(f"{min(left_idx, right_idx)} {max(left_idx, right_idx)}")
