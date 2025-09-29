
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

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

def point_in_triangle(p, a, b, c):
    d1 = cross(p, a, b)
    d2 = cross(p, b, c)
    d3 = cross(p, c, a)
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    return not (has_neg and has_pos)

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    points = []
    for i in range(1, n+1):
        x, y = map(int, data[i].split())
        points.append((x, y))
    
    total = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                a, b, c = points[i], points[j], points[k]
                valid = True
                for l in range(n):
                    if l == i or l == j or l == k:
                        continue
                    if point_in_triangle(points[l], a, b, c):
                        valid = False
                        break
                if valid:
                    total += 1
                    
    print(total)

if __name__ == "__main__":
    main()
