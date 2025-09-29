
def count_roads(matrix):
    roads = 0
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            if matrix[i][j] == 1:
                roads += 1
    return roads

with open('INPUT.TXT', 'r') as file:
    N = int(file.readline())
    matrix = []
    for _ in range(N):
        row = list(map(int, file.readline().split()))
        matrix.append(row)

roads_count = count_roads(matrix)
with open('OUTPUT.TXT', 'w') as file:
    file.write(str(roads_count))
