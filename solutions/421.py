
import sys

def read_triangles():
    data = sys.stdin.read().split()
    n = int(data[0])
    triangles = []
    index = 1
    for i in range(n):
        points = []
        for j in range(3):
            x = int(data[index])
            y = int(data[index+1])
            index += 2
            points.append((x, y))
        triangles.append(points)
    return triangles

def vector(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])

def vector_length(v):
    return (v[0]**2 + v[1]**2)**0.5

def dot_product(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def cross_product(v1, v2):
    return v1[0]*v2[1] - v1[1]*v2[0]

def angle_between_vectors(v1, v2):
    dot = dot_product(v1, v2)
    cross = cross_product(v1, v2)
    return abs(round(dot / (vector_length(v1) * vector_length(v2)), 10)), abs(round(cross / (vector_length(v1) * vector_length(v2)), 10))

def get_triangle_signature(triangle):
    p1, p2, p3 = triangle
    
    v1 = vector(p1, p2)
    v2 = vector(p1, p3)
    v3 = vector(p2, p3)
    
    lengths = sorted([
        round(vector_length(v1), 10),
        round(vector_length(v2), 10),
        round(vector_length(v3), 10)
    ])
    
    cos1, sin1 = angle_between_vectors(v1, v2)
    cos2, sin2 = angle_between_vectors(v1, v3)
    cos3, sin3 = angle_between_vectors(v2, v3)
    
    angles = sorted([cos1, cos2, cos3])
    
    return (tuple(lengths), tuple(angles))

def main():
    triangles = read_triangles()
    
    if len(triangles) == 0:
        print("YES")
        return
        
    base_signature = get_triangle_signature(triangles[0])
    
    for i in range(1, len(triangles)):
        current_signature = get_triangle_signature(triangles[i])
        
        if current_signature != base_signature:
            print("NO")
            return
            
    print("YES")

if __name__ == "__main__":
    main()
