
import math

def readints():
    return list(map(int, input().split()))

def point_in_triangle(p, A, B, C):
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    
    d1 = sign(p, A, B)
    d2 = sign(p, B, C)
    d3 = sign(p, C, A)
    
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    
    return not (has_neg and has_pos)

def point_on_segment(p, a, b):
    cross = (p[1] - a[1]) * (b[0] - a[0]) - (p[0] - a[0]) * (b[1] - a[1])
    if abs(cross) > 1e-12:
        return False
        
    dot = (p[0] - a[0]) * (b[0] - a[0]) + (p[1] - a[1]) * (b[1] - a[1])
    if dot < 0:
        return False
        
    squared_length = (b[0] - a[0])**2 + (b[1] - a[1])**2
    if dot > squared_length:
        return False
        
    return True

def point_in_polygon(p, poly):
    n = len(poly)
    inside = False
    
    for i in range(n):
        j = (i + 1) % n
        if point_on_segment(p, poly[i], poly[j]):
            return True
            
        if ((poly[i][1] > p[1]) != (poly[j][1] > p[1])):
            intersect = (poly[j][0] - poly[i][0]) * (p[1] - poly[i][1]) / (poly[j][1] - poly[i][1]) + poly[i][0]
            if p[0] < intersect:
                inside = not inside
                
    return inside

def can_form_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def get_triangle_vertices(a, b, c):
    if not can_form_triangle(a, b, c):
        return None
        
    x1, y1 = 0, 0
    x2, y2 = a, 0
    
    cos_angle = (b*b + a*a - c*c) / (2*b*a)
    sin_angle = math.sqrt(1 - cos_angle*cos_angle)
    
    x3 = b * cos_angle
    y3 = b * sin_angle
    
    return [(x1, y1), (x2, y2), (x3, y3)]

def transform_triangle(vertices, angle, scale, dx, dy):
    result = []
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    
    for x, y in vertices:
        x_scaled = x * scale
        y_scaled = y * scale
        
        x_rotated = x_scaled * cos_a - y_scaled * sin_a
        y_rotated = x_scaled * sin_a + y_scaled * cos_a
        
        result.append((x_rotated + dx, y_rotated + dy))
        
    return result

def main():
    n = int(input().strip())
    a, b, c = readints()
    trees = []
    
    for _ in range(n):
        trees.append(tuple(readints()))
    
    base_triangle = get_triangle_vertices(a, b, c)
    if base_triangle is None:
        print(0)
        return
        
    max_count = 0
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if i == k or j == k:
                    continue
                    
                p1, p2, p3 = trees[i], trees[j], trees[k]
                
                dx1 = p2[0] - p1[0]
                dy1 = p2[1] - p1[1]
                side1 = math.sqrt(dx1*dx1 + dy1*dy1)
                
                if abs(side1 - a) < 1e-9:
                    scale1 = 1.0
                else:
                    scale1 = a / side1
                
                dx2 = p3[0] - p1[0]
                dy2 = p3[1] - p1[1]
                side2 = math.sqrt(dx2*dx2 + dy2*dy2)
                
                if abs(side2 - b) < 1e-9:
                    scale2 = 1.0
                else:
                    scale2 = b / side2
                
                dx3 = p3[0] - p2[0]
                dy3 = p3[1] - p2[1]
                side3 = math.sqrt(dx3*dx3 + dy3*dy3)
                
                if abs(side3 - c) < 1e-9:
                    scale3 = 1.0
                else:
                    scale3 = c / side3
                
                if abs(scale1 - scale2) < 1e-9 and abs(scale1 - scale3) < 1e-9:
                    scale = scale1
                    angle = math.atan2(dy1, dx1)
                    
                    transformed = transform_triangle(base_triangle, angle, scale, p1[0], p1[1])
                    
                    count = 0
                    for tree in trees:
                        if point_in_triangle(tree, transformed[0], transformed[1], transformed[2]) or point_on_segment(tree, transformed[0], transformed[1]) or point_on_segment(tree, transformed[1], transformed[2]) or point_on_segment(tree, transformed[2], transformed[0]):
                            count += 1
                    
                    max_count = max(max_count, count)
    
    print(max_count)

if __name__ == "__main__":
    main()
