
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

lower_value = max(min(row) for row in matrix)
upper_value = min(max(matrix[i][j] for i in range(n)) for j in range(m))

print(lower_value, upper_value)
