
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def point_in_triangle(p, a, b, c):
    d1 = cross(a, b, p)
    d2 = cross(b, c, p)
    d3 = cross(c, a, p)
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    return not (has_neg and has_pos)

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    points = []
    for i in range(1, n+1):
        x, y = map(int, data[i].split())
        points.append((x, y))
    
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                a, b, c = points[i], points[j], points[k]
                valid = True
                for l in range(n):
                    if l == i or l == j or l == k:
                        continue
                    p = points[l]
                    if point_in_triangle(p, a, b, c):
                        valid = False
                        break
                if valid:
                    count += 1
                    
    print(count)

if __name__ == "__main__":
    main()
