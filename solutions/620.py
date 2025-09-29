
import sys

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def polygon_area(points):
    area = 0.0
    n = len(points)
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    return abs(area) / 2.0

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    index = 1
    max_area = 0.0
    
    for _ in range(n):
        k = int(data[index]); index += 1
        points = []
        for i in range(k):
            x = float(data[index]); y = float(data[index+1]); index += 2
            points.append((x, y))
        
        hull = convex_hull(points)
        area = polygon_area(hull)
        max_area = max(max_area, area)
    
    print("{:.2f}".format(max_area))

if __name__ == "__main__":
    main()
