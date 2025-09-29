
n = int(input())
matrix = [[0] * n for _ in range(n)]
num = 1

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            matrix[i][j] = num
            num += 1
    else:
        for j in range(n-1, -1, -1):
            matrix[i][j] = num
            num += 1

with open('OUTPUT.TXT', 'w') as f:
    for row in matrix:
        f.write(' '.join(map(str, row)) + '\n')
