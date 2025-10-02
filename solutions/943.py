
with open('INPUT.TXT', 'r') as f:
    N, M, Y, X = map(int, f.read().split())

matrix = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if (i + j) % 2 == 0:
            matrix[i][j] = (i + j) * (i + j + 1) // 2 + i + 1
        else:
            matrix[i][j] = (i + j) * (i + j + 1) // 2 + j + 1

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(matrix[Y-1][X-1]))
