
import sys

def readints():
    return list(map(int, sys.stdin.read().split()))

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

def point_in_triangle(a, b, c, p):
    d1 = cross(a, b, p)
    d2 = cross(b, c, p)
    d3 = cross(c, a, p)
    return (d1 >= 0 and d2 >= 0 and d3 >= 0) or (d1 <= 0 and d2 <= 0 and d3 <= 0)

def main():
    data = readints()
    n = data[0]
    points = []
    index = 1
    for i in range(n):
        x = data[index]
        y = data[index+1]
        index += 2
        points.append((x, y))
    
    total = n * (n-1) * (n-2) // 6
    hull = convex_hull(points)
    hull_set = set(hull)
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                a, b, c = points[i], points[j], points[k]
                count_inside = 0
                for p in points:
                    if p == a or p == b or p == c:
                        continue
                    if point_in_triangle(a, b, c, p):
                        count_inside += 1
                if count_inside > 0:
                    total -= 1
    print(total)

if __name__ == "__main__":
    main()
