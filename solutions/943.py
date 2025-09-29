
with open("INPUT.TXT", "r") as f:
    N, M, Y, X = map(int, f.read().split())

matrix = [[0] * M for _ in range(N)]
num = 1

for layer in range(min(N, M) // 2 + 1):
    for j in range(layer, M - layer):
        matrix[layer][j] = num
        num += 1
    for i in range(layer + 1, N - layer):
        matrix[i][M - layer - 1] = num
        num += 1
    if layer < N - layer - 1:
        for j in range(M - layer - 2, layer - 1, -1):
            matrix[N - layer - 1][j] = num
            num += 1
    if layer < M - layer - 1:
        for i in range(N - layer - 2, layer, -1):
            matrix[i][layer] = num
            num += 1

with open("OUTPUT.TXT", "w") as f:
    f.write(str(matrix[Y-1][X-1]))
