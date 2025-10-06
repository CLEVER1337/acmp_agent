
import math

def readints():
    return list(map(int, input().split()))

def distance_point_to_line(x0, y0, x1, y1, x2, y2):
    numerator = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    denominator = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    return numerator / denominator

def distance_point_to_segment(x0, y0, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    segment_length_squared = dx * dx + dy * dy
    
    if segment_length_squared == 0:
        return math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
    
    t = max(0, min(1, ((x0 - x1) * dx + (y0 - y1) * dy) / segment_length_squared))
    
    projection_x = x1 + t * dx
    projection_y = y1 + t * dy
    
    return math.sqrt((x0 - projection_x) ** 2 + (y0 - projection_y) ** 2)

def ternary_search(f, left, right, eps=1e-8, max_iter=100):
    for _ in range(max_iter):
        if abs(right - left) < eps:
            break
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3
        if f(m1) > f(m2):
            left = m1
        else:
            right = m2
    return (left + right) / 2

def solve():
    n = int(input().strip())
    lines = []
    for i in range(n):
        data = readints()
        lines.append(data)
    
    left_x = -1e9
    right_x = 1e9
    left_y = -1e9
    right_y = 1e9
    
    def f_x(x):
        def f_y(y):
            max_dist = 0.0
            for line in lines:
                x1, y1, x2, y2 = line
                dist = distance_point_to_line(x, y, x1, y1, x2, y2)
                max_dist = max(max_dist, dist)
            return max_dist
        
        y_opt = ternary_search(f_y, left_y, right_y)
        return f_y(y_opt)
    
    x_opt = ternary_search(f_x, left_x, right_x)
    
    def f_y_final(y):
        max_dist = 0.0
        for line in lines:
            x1, y1, x2, y2 = line
            dist = distance_point_to_line(x_opt, y, x1, y1, x2, y2)
            max_dist = max(max_dist, dist)
        return max_dist
    
    y_opt = ternary_search(f_y_final, left_y, right_y)
    
    print(f"{x_opt:.10f} {y_opt:.10f}")

if __name__ == "__main__":
    solve()
