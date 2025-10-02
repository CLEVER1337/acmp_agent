
w, h = map(int, input().split())
n = int(input())
rectangles = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    rectangles.append((x1, y1, x2, y2))

canvas = [[False] * w for _ in range(h)]

for rect in rectangles:
    x1, y1, x2, y2 = rect
    for y in range(y1, y2):
        for x in range(x1, x2):
            canvas[y][x] = True

unpainted = 0
for i in range(h):
    for j in range(w):
        if not canvas[i][j]:
            unpainted += 1

print(unpainted)
