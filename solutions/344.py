
n = int(input())
points = list(map(int, input().split()))
indexed_points = [(points[i], i + 1) for i in range(n)]
indexed_points.sort()

min_distance = float('inf')
result_indices = None

for i in range(n - 1):
    distance = indexed_points[i + 1][0] - indexed_points[i][0]
    if distance < min_distance:
        min_distance = distance
        result_indices = (indexed_points[i][1], indexed_points[i + 1][1])
    elif distance == min_distance:
        if indexed_points[i][0] < indexed_points[result_indices[0] - 1][0]:
            result_indices = (indexed_points[i][1], indexed_points[i + 1][1])

print(min_distance)
if result_indices[0] < result_indices[1]:
    print(result_indices[0], result_indices[1])
else:
    print(result_indices[1], result_indices[0])
