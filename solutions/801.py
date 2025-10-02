
import math

def line_from_points(x1, y1, x2, y2):
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    return A, B, C

def distance_point_to_line(A, B, C, x, y):
    return abs(A * x + B * y + C) / math.sqrt(A * A + B * B)

def distance_point_to_segment(x1, y1, x2, y2, px, py):
    line_len_sq = (x2 - x1)**2 + (y2 - y1)**2
    if line_len_sq == 0:
        return math.sqrt((px - x1)**2 + (py - y1)**2)
    
    t = max(0, min(1, ((px - x1) * (x2 - x1) + (py - y1) * (y2 - y1)) / line_len_sq))
    proj_x = x1 + t * (x2 - x1)
    proj_y = y1 + t * (y2 - y1)
    return math.sqrt((px - proj_x)**2 + (py - proj_y)**2)

def ternary_search(f, left, right, eps=1e-8, max_iter=100):
    for _ in range(max_iter):
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        if f(mid1) > f(mid2):
            left = mid1
        else:
            right = mid2
        if abs(right - left) < eps:
            break
    return (left + right) / 2

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    segments = []
    for i in range(n):
        idx = 1 + i * 4
        x1 = int(data[idx]); y1 = int(data[idx+1])
        x2 = int(data[idx+2]); y2 = int(data[idx+3])
        segments.append((x1, y1, x2, y2))
    
    min_x = min(min(x1, x2) for x1, y1, x2, y2 in segments)
    max_x = max(max(x1, x2) for x1, y1, x2, y2 in segments)
    min_y = min(min(y1, y2) for x1, y1, x2, y2 in segments)
    max_y = max(max(y1, y2) for x1, y1, x2, y2 in segments)
    
    def f(x, y):
        max_dist = 0.0
        for seg in segments:
            x1, y1, x2, y2 = seg
            dist = distance_point_to_segment(x1, y1, x2, y2, x, y)
            if dist > max_dist:
                max_dist = dist
        return max_dist
    
    def f_x(x):
        def f_y(y):
            return f(x, y)
        y_opt = ternary_search(f_y, min_y, max_y)
        return f(x, y_opt)
    
    x_opt = ternary_search(f_x, min_x, max_x)
    
    def f_y(y):
        return f(x_opt, y)
    
    y_opt = ternary_search(f_y, min_y, max_y)
    
    print(f"{x_opt:.10f} {y_opt:.10f}")

if __name__ == "__main__":
    main()
