
import math

def readints():
    return list(map(int, input().split()))

n = int(input())
xp1, yp1, xp2, yp2 = readints()
plates = []

for i in range(n):
    data = readints()
    plates.append((data[0], data[1], data[2], i + 1))

def distance_from_point_to_line(x0, y0, x1, y1, x2, y2):
    numerator = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    denominator = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    return numerator / denominator

def point_in_segment(x0, y0, x1, y1, x2, y2):
    cross = (x2 - x1) * (y0 - y1) - (y2 - y1) * (x0 - x1)
    if abs(cross) > 1e-10:
        return False
    dot1 = (x0 - x1) * (x2 - x1) + (y0 - y1) * (y2 - y1)
    dot2 = (x0 - x2) * (x1 - x2) + (y0 - y2) * (y1 - y2)
    return dot1 >= 0 and dot2 >= 0

destroyed = []
for x, y, r, idx in plates:
    dist = distance_from_point_to_line(x, y, xp1, yp1, xp2, yp2)
    
    if dist <= r + 1e-10:
        if point_in_segment(x, y, xp1, yp1, xp2, yp2):
            destroyed.append(idx)
        else:
            d1 = math.sqrt((x - xp1) ** 2 + (y - yp1) ** 2)
            d2 = math.sqrt((x - xp2) ** 2 + (y - yp2) ** 2)
            if d1 <= r or d2 <= r:
                destroyed.append(idx)
            else:
                dot1 = (x - xp1) * (xp2 - xp1) + (y - yp1) * (yp2 - yp1)
                dot2 = (x - xp2) * (xp1 - xp2) + (y - yp2) * (yp1 - yp2)
                if dot1 > 0 and dot2 > 0:
                    destroyed.append(idx)

destroyed.sort()
print(len(destroyed))
if destroyed:
    print(' '.join(map(str, destroyed)))
else:
    print()
