
x1, y1, x2, y2 = map(int, input().split())
x3, y3, r = map(int, input().split())

count = 0
r_sq = r * r

for x in range(max(x1, x3 - r), min(x2, x3 + r) + 1):
    dx = x - x3
    max_dy_sq = r_sq - dx * dx
    if max_dy_sq < 0:
        continue
    max_dy = int(max_dy_sq**0.5)
    y_min = max(y1, y3 - max_dy)
    y_max = min(y2, y3 + max_dy)
    if y_min <= y_max:
        count += y_max - y_min + 1

print(count)
