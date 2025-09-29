
import math

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def point_to_line_dist(point, line):
    x0, y0 = point
    (x1, y1), (x2, y2) = line
    if x1 == x2 and y1 == y2:
        return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)
    num = abs((y2 - y1)*x0 - (x2 - x1)*y0 + x2*y1 - y2*x1)
    den = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
    return num / den

def find_farthest_point(lines, point):
    max_dist = 0.0
    farthest_line = None
    for line in lines:
        dist = point_to_line_dist(point, line)
        if dist > max_dist:
            max_dist = dist
            farthest_line = line
    return farthest_line, max_dist

def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    lines = []
    index = 1
    for i in range(n):
        x1, y1, x2, y2 = map(int, data[index:index+4])
        index += 4
        lines.append(((x1, y1), (x2, y2)))
    
    best_point = (0.0, 0.0)
    best_max_dist = float('inf')
    
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            intersection = line_intersection(lines[i], lines[j])
            if intersection is not None:
                _, max_dist = find_farthest_point(lines, intersection)
                if max_dist < best_max_dist:
                    best_max_dist = max_dist
                    best_point = intersection
    
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            for k in range(j+1, len(lines)):
                intersections = []
                inter1 = line_intersection(lines[i], lines[j])
                inter2 = line_intersection(lines[j], lines[k])
                inter3 = line_intersection(lines[i], lines[k])
                
                if inter1: intersections.append(inter1)
                if inter2: intersections.append(inter2)
                if inter3: intersections.append(inter3)
                
                for point in intersections:
                    _, max_dist = find_farthest_point(lines, point)
                    if max_dist < best_max_dist:
                        best_max_dist = max_dist
                        best_point = point
    
    print(f"{best_point[0]:.15f} {best_point[1]:.15f}")

if __name__ == "__main__":
    solve()
