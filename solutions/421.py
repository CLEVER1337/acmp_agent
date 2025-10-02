
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

def distance_sq(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return dx*dx + dy*dy

def get_side_lengths(triangle):
    a = distance_sq(triangle[0], triangle[1])
    b = distance_sq(triangle[1], triangle[2])
    c = distance_sq(triangle[2], triangle[0])
    return sorted([a, b, c])

def are_congruent(t1, t2):
    sides1 = get_side_lengths(t1)
    sides2 = get_side_lengths(t2)
    return sides1 == sides2

def main():
    triangles = read_triangles()
    
    if len(triangles) == 0:
        print("YES")
        return
        
    base = triangles[0]
    
    for i in range(1, len(triangles)):
        if not are_congruent(base, triangles[i]):
            print("NO")
            return
            
    print("YES")

if __name__ == "__main__":
    main()
