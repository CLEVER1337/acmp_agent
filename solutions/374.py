
import math

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    if len(points) <= 1:
        return points
    
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

def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    points = []
    index = 1
    for i in range(n):
        x = int(data[index]); y = int(data[index+1]); index += 2
        points.append((x, y))
    
    hull = convex_hull(points)
    perimeter = 0.0
    m = len(hull)
    for i in range(m):
        j = (i + 1) % m
        perimeter += distance(hull[i], hull[j])
    
    print("{0:.1f}".format(perimeter))

if __name__ == "__main__":
    main()
