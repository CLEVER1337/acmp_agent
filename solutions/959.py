
import math

def readints():
    return list(map(int, input().split()))

def point_in_triangle(p, v1, v2, v3):
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    
    d1 = sign(p, v1, v2)
    d2 = sign(p, v2, v3)
    d3 = sign(p, v3, v1)
    
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    
    return not (has_neg and has_pos)

def can_form_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def perimeter(points):
    return sum(distance(points[i], points[(i+1)%3]) for i in range(3))

def main():
    n = int(input().strip())
    a, b, c = readints()
    points = []
    for _ in range(n):
        points.append(tuple(readints()))
    
    max_count = 0
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                v1, v2, v3 = points[i], points[j], points[k]
                side1 = distance(v1, v2)
                side2 = distance(v2, v3)
                side3 = distance(v3, v1)
                
                if can_form_triangle(side1, side2, side3):
                    perim = side1 + side2 + side3
                    if perim <= a + b + c:
                        count = 3
                        for p in points:
                            if p != v1 and p != v2 and p != v3:
                                if point_in_triangle(p, v1, v2, v3):
                                    count += 1
                        if count > max_count:
                            max_count = count
    
    print(max_count)

if __name__ == "__main__":
    main()
